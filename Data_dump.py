import pymongo
import pandas  as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_PATH ='/config/workspace/aps_failure_training_set1.csv'
DATABASE_NAME ="APS_FAULT"
COLLECTION_NAME = "SENSOR"


if __name__ == "__main__":
    df=pd.read_csv(DATA_PATH)
    print(f"Rows and columns :{df.shape}")

    # Convert datafrane to jsaon format so that we can dump the in mangodb
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)