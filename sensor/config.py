import pymongo
import pandas as pd 
import numpy
from dataclasses import dataclass
import os

# Provide local mongodb url for connection
@dataclass
class EnvironmentVariable:
    mongo_db_url : str = os.getenv('MONGO_DB_URL')
    
env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "class"
