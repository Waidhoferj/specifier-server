import os

from flask import Flask, request
from flask_cors import CORS
import spacy

app = Flask(__name__)
CORS(app)
nlp = spacy.load("en_core_web_sm")


@app.route("/parts-of-speech", methods=["POST"])
def get_parts_of_speech():
    data = request.json
    sentence = data["text"]
    parts_of_speech = [{"token":str(token) , "pos":str(token.pos_)} for token in nlp(sentence)]
    return {"tokens": parts_of_speech}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
