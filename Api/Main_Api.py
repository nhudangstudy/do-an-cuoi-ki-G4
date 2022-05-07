from pymongo import MongoClient 
import os
from dotenv import load_dotenv, find_dotenv

class Api: 
    def __init__(self):
        self.connector()

    #connect to mongodb 
    def connector(self):
        load_dotenv(find_dotenv())
        host = os.getenv("HOSTNAME")
        client = MongoClient(host)
        db = client['G4KTLT']
        self.collection = db['users']   