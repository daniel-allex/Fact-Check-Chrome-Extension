from ..server import sentenceEmbeddingTransformer
import json

with open('server/data.json') as f:
    # Load JSON data from file
    data = json.load(f)

sentences = [data_block['Fakenews'] for data_block in data]
embeddingTransformer = sentenceEmbeddingTransformer()
vectors = embeddingTransformer.transformSentences(sentences).tolist()

for i in range(len(vectors)):
    data[i]['Embedding'] = vectors[i]
    data[i]['Index'] = i

with open('data_embeddings.json', 'w') as f:
    json.dump(data, f)
