from sensor import utils
from sensor.entity import config_entity
from sensor.entity import artifact_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split

class DataIngestion:
    
    def __init__(self,data_ingestion_config:config_entity.DataIngestionConfig ):
        try:
            logging.info(f"{'>>'*20} Data Ingestion {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self)->artifact_entity.DataIngestionArtifact:
            try:
                logging.info(f"Exporting collection data as pandas dataframe")
                #Exporting collection data as pandas dataframe
                df:pd.DataFrame  = utils.get_collection_as_dataframe(
                    database_name=self.data_ingestion_config.database_name, 
                    collection_name=self.data_ingestion_config.collection_name)
                
            except Exception as e:
                raise SensorException(e,sys)
