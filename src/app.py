from flask import Flask, request, jsonify

app = Flask(__name__)

import config as CONFIG

@app.route('/', methods=['GET'])
def index():
    api_docs = open(f"docs/api_{CONFIG.API_VERSION}.html", "r")
    return api_docs.read()