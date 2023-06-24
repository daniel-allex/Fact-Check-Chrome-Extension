from flask import Flask, render_template, url_for, request, redirect, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Running Successfully"

@app.route("/request", methods=["POST"])
def handleRequest():
    print("requested")
    text = request.get_json()["contents"]
    print(text)
    example = [{
       "sentence": "maker of launch vehicles",
        "results": [{
            "error": "He did not make an AI",
            "source": "https://www.politifact.com/factchecks/2020/jul/28/stella-immanuel/dont-fall-video-hydroxychloroquine-not-covid-19-cu/",
           "correct": "PolitiFact | Hydroxychloroquine is not a COVID-19 cure"
        }]
        }]

    return json.dumps(example)

if __name__ == "__main__":
    app.run(debug=True)

