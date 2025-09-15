import os
from pymongo import MongoClient

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = os.getenv("MONGO_URI")
        self.__client = None
        self.__db_connection = None
    
    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client.get_default_database()

    def get_db_connection(self):
        return self.__db_connection

db_connection_handler = DBConnectionHandler()
