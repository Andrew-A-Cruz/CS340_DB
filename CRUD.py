from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47363' % ("aacUser", "password123"))
        # where xxxx is your unique port number
        self.database = self.client['aac']
# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
        else:
            raise Exception("Nothing to save, because data parameter is empty")
# Create method to implement the R in CRUD.

    def read(self, query):
        if query is not None:
            return self.database.animals.find_one(query)
        else:
            raise Exception("Unable to find query.")

# Create method to implement the U in CRUD.
    def update(self, query, update):
        if query is not None:
            return self.database.animals.update_one(query, {"$set": update}, upsert=False)
        else:
            raise Exception("unable to update query.")

# Create method to implement the D in CRUD.
    def destroy(self, query):
        if query is not None:
            return self.database.animals.delete_one(query)
        else:
            raise Exception("unable to destroy query.")