import pandas as pd 
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys

def get_collections_as_dataframe(database_name:str,collection_name:str) -> pd.DataFrame:
    ''' This function return collections as DataFrame
    =================================================
    Params:

    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas DataFrame of a collection '''

    try:
        logging.info(f'Reading data from dataframe :{database_name} and collection "{collection_name}')
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f'Found columns :{df.columns}')
        if '_id' in df.columns:
            df = df.drop('_id',axis =1)
        logging.info(f'Rows and columns')
        return df
    except Exception as e:
        raise SensorException(e,sys)

    
    
