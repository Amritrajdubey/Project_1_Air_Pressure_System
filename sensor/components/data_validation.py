from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity import config_entity,artifact_entity
from scipy.stats import ks_2samp
import os,sys

class DataValidation:
    def __init__ (self,data_validation_config : config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(e, sys)
            

