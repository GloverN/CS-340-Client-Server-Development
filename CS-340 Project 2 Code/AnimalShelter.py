from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, usr='aacuser', pwd='SNHU5062'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database and the 
        # animals collection.
        # If the object is not instantiated with a 
        # username or password, the object will use the 
        # aacuser account by default.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        USER = usr
        PASS = pwd
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31978
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Method to implement the C in CRUD operations
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary
            return result.acknowledged  # Returns whether or not the insert was successful or not
        else:
            raise Exception('Nothing to save, because data parameter is empty')

    # Method to implement the R in CRUD operations
    def read(self, data):
        result_list = []
        if data is not None:
            result_list = list(self.database.animals.find(data))  # data should be a dictionary
        return result_list

    # Method to implement the U in CRUD operations
    def update(self, data, new_data):
        if data and new_data is not None:
            result = self.database.animals.update_many(data, new_data)  # data and new_data should be dictionaries
            return result.modified_count  # Returns the number of entries that were modified
        else:
            raise Exception('Nothing to update, because data or new_data parameter is empty')

    # Method to implement the D in CRUD operations
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)  # data should be a dictionary
            return result.deleted_count  # Returns the number of entries that were deleted
        else:
            raise Exception('Nothing to delete, because data parameter is empty')