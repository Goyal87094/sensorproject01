from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#create a  new client and connect to server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME = "INEURON"
COLLECTION_NAME = "SENSOR"

df = pd.read_csv("C:\Users\goyal\Desktop\sensor_fault\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)