from ..server import sentenceEmbeddingTransformer
from ..server import Database
import json

with open('data_embeddings.json') as f:
    # Load JSON data from file
    data = json.load(f)


db = Database("mongodb://localhost:27017/", "FakeNewsDB", "PoliticalData")
db.insert_many(data)