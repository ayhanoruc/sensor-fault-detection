
import pymongo
from sensor.constants.database import DATABASE_NAME
from sensor.constants.env_variables import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()
URL= "mongodb://localhost:27017"
class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                #print(mongo_db_url)
                if "localhost" in URL:
                    MongoDBClient.client = pymongo.MongoClient(URL) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(URL, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

