from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from corridor_boilerplate.settings import MONGODB_CONFIG

class MongoConnection:

    def __init__(self):
        # Creating a new connection
        self.open()

    def open(self):
        try:
            self.client = MongoClient(host=MONGODB_CONFIG['host'] , 
                                    port=int(MONGODB_CONFIG['port'],),
                                    username=MONGODB_CONFIG['username'],
                                    password=MONGODB_CONFIG['password'])
        except ConnectionFailure:
            print("MongoDB Server could not be connected !")
    
    def getDatabase(self):
        return self.client[MONGODB_CONFIG['database']]
    
    def selectDatabase(self):
        self.db = self.getDatabase()

    def getDatabaseList(self):
        return self.client.list_database_names()

    def close(self):
        self.client.close()

