import sentence_embeddings
import database
import json

with open('data_embeddings.json') as f:
    # Load JSON data from file
    data = json.load(f)

#for i in range(len(data)):
    #data[key]


db = database.Database("mongodb://localhost:27017/", "FakeNewsDB", "PoliticalData")
db.insert_many(data)