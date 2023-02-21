from sensor .entity import config_entity,artifact_entity
from sensor.exception import SensorException
from sensor.logger import logging
from sensor import utils
import os,sys
import pandas as pd 
from sklearn.prepocessing import Pipeline
import numpy as np 
from typing import Optional
from sklearn.prepocessing import LabelEncoder
from imblearn.combine import SMOTETomek
from sklearn.prepocessing import RobustScaler
from sklearn.impute import SimpleImputer
from sensor.config import TARGET_COLUMN




class Datatransformation:

    def __init__ (self,data_transformation_config : config_entity.DataTransformationConfig,
                    data_ingestion_artifact: artifact_entity.DataIngestionArtifact):

        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise SensorException(e, sys)

    @classmethod
    def get_data_transformer_object(cls)->Pipeline:
        try:
            simple_imputer = SimpleImputer(strategy='constant', fill_value=0)
            robust_scaler =  RobustScaler()
            pipeline = Pipeline(steps=[
                    ('Imputer',simple_imputer),
                    ('RobustScaler',robust_scaler)
                ])
            return pipeline
        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_transformation(self) -> artifact_entity.DataTransformationArtifact:

        try:
            # Reading train and test file
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            # Selecting input feature for train and test df 
            input_feature_train_df = train_df.drop(TARGET_COLUMN,axis = 1)
            input_feature_test_df = test_df.drop(TARGET_COLUMN,axis = 1)

            # Selecting target feature of train and test df
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_test_df = test_df[TARGET_COLUMN]

            label_encoder = LabelEncoder()
            label_encoder.fit(target_feature_train_df)

            # Transformatio on target column
            target_feature_train_arr = label_encoder.transform(target_feature_train_df)
            target_feature_test_arr = label_encoder.transform(target_feature_test_df)

            transformation_pipleine = DataTransformation.get_data_transformer_object()
            transformation_pipleine.fit(input_feature_train_df)

            #transforming input features
            input_feature_train_arr = transformation_pipleine.transform(input_feature_train_df)
            input_feature_test_arr = transformation_pipleine.transform(input_feature_test_df)

            smt = SMOTETomek(sampling_strategy = 'minority')
            logging.info(f"Before resampling the training df set Input: {input_feature_train_arr.shape} Target:{target_feature_train_arr.shape}")
            input_feature_train_arr , target_feature_train_arr =smt.fit_resample(input_feature_train_arr,target_feature_train_arr)
            logging.info(f"After resampling in training df set Input: {input_feature_train_arr.shape} Target:{target_feature_train_arr.shape}")

            logging.info(f"Before resampling the test df set Input: {input_feature_test_arr.shape} Target:{target_feature_test_arr.shape}")
            input_feature_test_arr , target_feature_test_arr =smt.fit_resample(input_feature_test_arr,target_feature_test_arr)
            logging.info(f"After resampling in test df set Input: {input_feature_test_arr.shape} Target:{target_feature_test_arr.shape}")













