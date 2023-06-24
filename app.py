from flask import Flask, render_template, url_for, request, redirect, json
from flask_cors import CORS
<<<<<<< HEAD
=======
from server.sentence_tokenizer import SentenceTokenizer
from server.database import Database
from server.sentence_embeddings import sentenceEmbeddingTransformer
from server.vector_search import VectorSearcher
>>>>>>> c2a6fd9 (updated connections)

app = Flask(__name__)
CORS(app)
tk = SentenceTokenizer()
embedding_transformer = sentenceEmbeddingTransformer()
db = Database("mongodb://localhost:27017/", "FakeNewsDB", "PoliticalData")
vs = VectorSearcher(384, 100, "ANNTree.ann", db)
"""
a = embedding_transformer.transformSentence("We have plans to build a railroad from the Pacific all the way across the Indian Ocean.")
b = embedding_transformer.transformSentence("Work is ongoing constructing Joe Biden's 8,000 mile long 'ocean train'")
print(embedding_transformer.compareSentences(a, b))
"""

@app.route("/")
def index():
    return "Running Successfully"

@app.route("/request", methods=["POST"])
def handleRequest():
    print("requested")
    text = request.get_json()["contents"]
<<<<<<< HEAD
    print(text)
    example = [{
       "sentence": "maker of launch vehicles",
        "results": [{
            "error": "He did not make an AI",
            "source": "https://www.politifact.com/factchecks/2020/jul/28/stella-immanuel/dont-fall-video-hydroxychloroquine-not-covid-19-cu/",
           "correct": "PolitiFact | Hydroxychloroquine is not a COVID-19 cure"
        }]
        }]
=======
    
    sentences = tk.tokenize_raw(text)
    embeddings = embedding_transformer.transformSentences(sentences)
    misinfo_dict = []

    for i in range(len(embeddings)):
        sentence = sentences[i]
        embedding = embeddings[i]
        ids, similarities = vs.search_vector(embedding, 100)

        for i in range(len(ids)):
            if similarities[i] != -1:
                row = db.find_row('Index', ids[i])
>>>>>>> c2a6fd9 (updated connections)

                misinfo_dict.append({"sentence" : sentence,
                                     "results" : [{
                                         "error" : row['Truenews'],
                                         "source" : row['source'],
                                         "correct" : "Politifact | " + row['Truenews']
                                     }]})

    return json.dumps(misinfo_dict)

if __name__ == "__main__":
    app.run(debug=True)

