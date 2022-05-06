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

    #user login api
    def check_user_login(self, username, password): 
        if username == "" or password == "": 
            return -1 #error 1: username or password is empty
        user = self.collection.find_one({'username': username})
        if user == None: 
            return -2 #error 2: user not found 
        if user["password"] != password: 
            return -3 #error 3: password is wrong 
        return user["roles"]

    #user sign up api
    def check_user_signup(self, username, password, reenterpassword):
        if username == "" or password == "" or reenterpassword == "":
            return -1 #error 1: username or password is empty 
        if password != reenterpassword:
            return -2 #error 2: password is not the same
        user = self.collection.find_one({'username': username})
        if user != None: 
            return -3 #error 3: username is already exist 
        self.collection.insert_one({'username': username, 'password': password, 'role': "User"})
        return 0 #success 