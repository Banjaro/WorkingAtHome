"""@package AM_GUI
Documentation "coming soon"

"""
 
from pymongo import MongoClient

class Helper():

    def __init__(self):
        super().__init__()

        # This can be changed later but localhost
        #  should be default. I think
        myclient = "localhost:27017"
        self.client = MongoClient('mongodb://'+ myclient)

    def changedb(self, dbname):
        self.client = MongoClient('mongodb://'+ dbname)
 
    def createdb(self,dbname, colname):
        temp = {"temp":"temp"}
        if dbname in self.client.list_database_names():
            pass
        else:
            self.client[dbname][colname].insert_one(temp)
            self.client[dbname][colname].delete_one(temp)

    def deletedb(self, dbname):
        deleteme = self.client[dbname].list_collection_names()
        if dbname in self.client.list_database_names():
            for collection in deleteme:
                self.client[dbname][collection].drop()

    def createcol(self, dbname, colname):
        temp = {"temp":"temp"}
        if colname in self.client[dbname].list_collection_names():
            pass
        else:
            self.client[dbname][colname].insert_one(temp)
            self.client[dbname][colname].delete_one(temp)

    # Some functions, like these, might seem redundant but I'm trying to keep the
    #  syntax consistent and succinct throughtout the code 

    def deletecol(self, dbname, colname):
        self.client[dbname][colname].drop()

    def createdoc(self, dbname, colname, doc):
        self.client[dbname][colname].insert_one(doc)

    def deletedoc(self, dbname, colname, doc):
        self.client[dbname][colname].delete_one(doc)

    # Gets the schema for the object in the form of a json object

    def getjsonschema(self, dbname,colname):
        pgs = self.client[dbname].command('listCollections')['cursor']['firstBatch']
        target_collection = colname

        for dictionary in pgs:
            if dictionary['name'] == target_collection:
                return (dictionary['options']['validator'])

    # This gets the schema from vue and hands it to mongo
    def schemamtv(self, schema):
        formatedschema = None # for now
        return formatedschema
    
    def editschema(self, dbname, colname, schema): 
        if dbname not in self.client.list_database_names():
            self.createdb(dbname,colname)
        #db.runCommand({collMod:"nameofcollection", {validator: {schema}}})
        self.client[dbname].command({'collMod':str(colname),'validator':schema})
