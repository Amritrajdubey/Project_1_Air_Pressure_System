from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
import pandas as pd 
import numpy as np 

class DataIngestion:
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e :
            raise SensorException(e, sys)
    
    def initiate_data_ingestition(self) -> artifact_entity.DataIngestionArtifact:
        try:
            #Exporting collection data as pandas dataframe
            logging.info('Exporting collection data as pandas dataframe')
            df : pd.dataframe = utils.get_collections_as_dataframe(
                database_name = self.data_ingestion_config.database_name, 
                collection_name = self.data_ingestion_config.collection_name)
            logging.info('Data saved in feature store')

            # Replace na with NAN
            df.replace(to_replace ='na',value=np.NAN,inplace= True)
            logging.info('na value replace to NAN')

            logging.info('Creating feature store if not available')
            # Create feature store folder if not available
            os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exit_ok =True)
            logging.info('saved df to feature store')

            # Save df to feature store folder
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)

            # split the train test data 
            train_df,test_df =train_test_split(df,test_size = self.data_ingestion_config.test_size,random_state = 40)
            logging.info('Data set splitted in train and test set')

            # create dataset directory
            dataset_dir =os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir,exit_ok =True)
            logging.info('Creating Dataset directory')

            # saving df to feature store folder
            train_df.to_csv(path_or_buf = self.data_ingestion_config.feature_store_file_path,index=False,header=True)
            test_df.to_csv(path_or_buf = self.data_ingestion_config.feature_store_file_path,index = False,header=True)
            logging.info('Saving train and test dataset and saving it to feature store')

            # Prepare artifact
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path = self.data_ingestion_config.feature_store_file_path,
                train_file_path = self.data_ingestion_config.train_file_path ,
                test_file_path = self.data_ingestion_config.test_file_path)

            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
            

        except Exception as e:
            raise SensorException(e,sys)