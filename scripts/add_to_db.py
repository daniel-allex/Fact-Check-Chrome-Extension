import sentence_embeddings
import database
import json

with open('data_embeddings.json') as f:
    # Load JSON data from file
    data = json.load(f)

db = database.Database("mongodb://localhost:27017/", "FakeNewsDB", "PoliticalData")
db.insert_many(data)