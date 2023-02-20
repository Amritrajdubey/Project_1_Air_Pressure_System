from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity import config_entity,artifact_entity
from scipy.stats import ks_2samp
import os,sys
import pandas as pd 
import numpy as np 

class DataValidation:

    def __init__ (self,data_validation_config : config_entity.DataValidationConfig,
                    data_ingestion_artifact: artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact =data_ingestion_artifact
            self.validation_error :dict()
        except Exception as e:
            raise SensorException(e, sys)


    def drop_missing_values_columns(self,df:pd.DataFrame):
        """
        This function will drop columns which contains missing values more than 30% 
        
        df: Accept a pandas dataframe
        threshold : Percentage criteria to drop the columns
        
        return pandas DataFrame if even single column is left after droping the missing values cloumn
        """

        try:
            threshold = self.data_validation_config.missing_threshold
            null_report = df.isnull().sum()/df.shape[0]
            # Segregating columns with null values
            logging.info(f"Selecting column with null values more than {threshold}")
            drop_column_names = null_report[null_report>threshold].index

            self.validation_error['Dropped columns'] = drop_column_names 
            df.drop(list(drop_column_names,axis=1,inplace=True))
            logging.info(f"Droping columns :{list(drop_column_names)}")
            if len(df.columns) == 0:
                return None
            return df

        except Exception as e:
            raise SensorException(e, sys)

    def does_Required_column_exist(self,base_df:pd.DataFrame,current_df:pd.DataFrame) ->bool:
        try:
            base_column = base_df.columns
            current_column = current_df.columns

            missing_column =[]
            for base_column in base_column :
                if base_column not in current_column:
                    missing_column.append(base_column)

            if len(missing_column) >0:
                self.validation_error['Missing columns'] = missing_column
                return False
            return True
        except Exception as e:
            raise SensorException(e, sys)

    def data_drift (self,base_df:pd.DataFrame,current_df:pd.DataFrame):
        try: 
            drift_report = dict()
            base_column = base_df.columns
            current_column = current_df.columns

            for base_column in base_column:
                base_data,current_data = base_df[base_column],current_df[base_column]
                # To verify null hypothesis we have drawn data from same distribution
                same_distribution = ks_2samp(base_data,current_data)
                # We will accept null hypothesis
                if same_distribution.pvalue > .05:
                    drift_report[base_column] = {
                        "pvalues":float(same_distribution.pvalue),
                        "same_distribution" : True
                    }
                else:
                    drift_report[base_column] = {
                        "pvalues":float(same_distribution.pvalue),
                        "same_distribution" :False
                    }
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self) -> artifact_entity.DataValidationArtifact:
        try:
            base_df = pd.read_csv(self.data_validation_config.base_file_path)
            base_df.replace({'na':np.NAN},inplace = True)
            # Base df has na values as null
            base_df = self.drop_missing_values_columns(df=base_df,report_key_name ="Missing_values_within_base_df")

            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            train_df = self.drop_missing_values_columns(df=train_df,report_key_name ="Missing_values_within_Train_df")
            test_df= self.drop_missing_values_columns(df=test_df,report_key_name='Missing_values_within_test_df')

            








       



