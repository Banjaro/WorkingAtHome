from pymongo import MongoClient
import json


client = MongoClient("mongodb://127.0.0.1:27017")
db = client["placeholder"]

schema = db.command('listCollections')

pgs = schema['cursor']['firstBatch']
target_collection = json.dumps('Tests')

for dictionary in pgs:
    if dictionary['name'] == target_collection:
        print(dictionary['options']['validator'])