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
        self.client = MongoClient(host)
        self.db = self.client['G4KTLT']
        self.users_collection = self.db['users']   
        self.warehouse_collection = self.db['warehouse'] 
        self.invoices_collection = self.db['invoices']
        