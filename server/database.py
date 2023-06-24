import pymongo
class database:
    def __init__(self, host, database_name, collection_name):
        self.host = host
        self.database_name = database_name
        self.collection_name = collection_name
        self.connect_to_database()

    def connect_to_database(self):
        client = pymongo.MongoClient(self.host)
        self.database = client[self.database_name]
        self.collection = self.database[self.collection_name]

    def insert_row(self, row):
        self.collection.insert_one(row)

    def insert_many(self, rows):
        self.collection.insert_many(rows)

    def find_row(self, column_name, target):
        return self.collection.find_one({column_name : target})
