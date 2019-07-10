import datetime
import pymongo

class DB(object):
          
    URI = "mongodb://127.0.0.1:27017"
          
    @staticmethod
    def init():
        client = pymongo.MongoClient(DB.URI)
        DB.DATABASE = client['sample_app']
          
    @staticmethod
    def insert(collection, data):
        DB.DATABASE[collection].insert(data)
          
    @staticmethod
    def find_one(collection, query):
        return DB.DATABASE[collection].find_one(query)

class Job(object):
 
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.datetime.utcnow()
 
    def insert(self):
        if not DB.find_one("jobs", {"name": self.name}):
            DB.insert(collection='jobs', data=self.json())
 
    def json(self):
        return {
            'name': self.name,
            'created_at': self.created_at
        }
