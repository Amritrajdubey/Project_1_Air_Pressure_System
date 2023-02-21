from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity import config_entity,artifact_entity
from scipy.stats import ks_2samp
import os,sys
import pandas as pd 
import numpy as np 
from sensor import utils
from typing import Optional
from sensor.config import TARGET_COLUMN

class DataValidation:

    def __init__ (self,data_validation_config : config_entity.DataValidationConfig,
                    data_ingestion_artifact: artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact =data_ingestion_artifact
            self.validation_error = dict()
        except Exception as e:
            raise SensorException(e, sys)


    def drop_missing_values_columns(self,df:pd.DataFrame,report_key_name:str) -> Optional[pd.DataFrame]:
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

            self.validation_error[report_key_name] = list(drop_column_names) 
            df.drop(list(drop_column_names),axis=1,inplace=True)
            logging.info(f"Droping columns :{list(drop_column_names)}")

            if len(df.columns) == 0: 
                return None
            return df

        except Exception as e:
            raise SensorException(e, sys)

    def does_Required_column_exist(self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str ) ->bool:
        try:
            base_column = base_df.columns
            current_column = current_df.columns

            missing_column =[]
            for base_column in base_column :
                if base_column not in current_column:
                    logging.info(f"column :[{base} is not available]")
                    missing_column.append(base_column)

            if len(missing_column) >0:
                self.validation_error['Missing columns'] = missing_column
                return False
            return True
        except Exception as e:
            raise SensorException(e, sys)

    def data_drift (self,base_df:pd.DataFrame,current_df:pd.DataFrame,report_key_name:str):
        try: 
            drift_report = dict()
            base_column = base_df.columns
            current_column = current_df.columns

            for base_column in base_column:
                base_data,current_data = base_df[base_column],current_df[base_column]
                # To verify null hypothesis we have drawn data from same distribution
                logging.info(f"Hypothesis {base_column}: {base_data.dtype}, {current_data.dtype} ")
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

            self.validation_error[report_key_name] = drift_report
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_validation(self) -> artifact_entity.DataValidationArtifact:
        try:
            logging.info(f'Reading base df')
            base_df = pd.read_csv(self.data_validation_config.base_file_path)
            base_df.replace({'na':np.NAN},inplace = True)
            logging.info(f"Replacing ns with NAN in base df")
            # Base df has na values as null
            logging.info(f"Droping null value column from base df")
            base_df = self.drop_missing_values_columns(df=base_df,report_key_name ="Missing_values_within_base_df")

            logging.info(f"Reading train df")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            logging.info(f'Reading test df')
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            logging.info(f'Droping null value column from train df')
            train_df = self.drop_missing_values_columns(df=train_df,report_key_name ="Missing_values_within_Train_df")
            logging.info(f'Droping null value column from test df')
            test_df= self.drop_missing_values_columns(df=test_df,report_key_name='Missing_values_within_test_df')

            exclude_columns = [TARGET_COLUMN]
            base_df = utils.convert_column_float(df=base_df, exclude_columns= exclude_columns)
            train_df = utils.convert_column_float(df= train_df, exclude_columns= exclude_columns)
            test_df = utils.convert_column_float(df=test_df, exclude_columns=exclude_columns)

            logging.info(f'All required column present in train df')
            train_df_missing_column = self.does_Required_column_exist(base_df= base_df, current_df=train_df,report_key_name='Missing_columns_within_train_df')
            logging.info(f'All requirend column present in test df')
            test_df_missing_column = self.does_Required_column_exist(base_df= base_df, current_df=test_df,report_key_name='Missing_columns_within_test_df')

            if train_df_missing_column:
                logging.info(f'As all columns are present in train df thus checking for data drift')
                self.data_drift(base_df=base_df, current_df=train_df,report_key_name='Data_drift_within_train_df')
            if test_df_missing_column :
                logging.info(f'As all columns are present in test df thus checking fro data drift')
                self.data_drift(base_df =base_df, current_df=test_df,report_key_name='Data_drift_within_test_df')

            # Write the report
            logging.info(f'Writing report in yaml file')
            utils.write_yaml_file(file_path= self.data_validation_config.report_file_path,
             data = self.validation_error)

            data_validation_artifact = artifact_entity.DataValidationArtifact(report_file_path = self.data_validation_config.report_file_path)
            logging.info(f'Data Validation Artifact :{data_validation_artifact}')
            return data_validation_artifact


        except Exception as e:
            raise SensorException(e, sys)
            













       



