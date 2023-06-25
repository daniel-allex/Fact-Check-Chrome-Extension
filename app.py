from flask import Flask, render_template, url_for, request, redirect, json
from flask_cors import CORS
from server.sentence_tokenizer import SentenceTokenizer
from server.database import Database
from server.sentence_embeddings import sentenceEmbeddingTransformer
from server.vector_search import VectorSearcher

app = Flask(__name__)
CORS(app)
tk = SentenceTokenizer()
embedding_transformer = sentenceEmbeddingTransformer()
db = Database("mongodb://localhost:27017/", "FakeNewsDB", "PoliticalData")
vs = VectorSearcher(384, 100, "ANNTree.ann", db)

@app.route("/")
def index():
    return "Running Successfully"

@app.route("/request", methods=["POST"])
def handleRequest():
    print("requested")
    text = request.get_json()["contents"]
    sentences = tk.tokenize_raw(text)

    embeddings = embedding_transformer.transformSentences(sentences)
    misinfo_dict = []

    for i in range(len(embeddings)):
        sentence = sentences[i]
        embedding = embeddings[i]
        ids, distances = vs.search_vector(embedding, 10)

        for i in range(len(ids)):
            if distances[i] < 0.45:
                row = db.find_row('Index', ids[i])

                misinfo_dict.append({"sentence" : sentence,
                                     "results" : [{
                                         "error" : row['Fakenews'],
                                         "source" : row['source'],
                                         "correct" : "Politifact | " + row['Truenews']
                                     }]})
            else:
                break

    return json.dumps(misinfo_dict)

if __name__ == "__main__":
    app.run(debug=True)

