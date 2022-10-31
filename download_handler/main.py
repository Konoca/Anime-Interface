from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv
import logging

from functions.search import search

load_dotenv()
logging.basicConfig(filename="error.log", level=logging.DEBUG)

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/search', methods = ['PUT'])
@cross_origin(supports_credentials=True)
def search_anime():
    data = json.loads(request.data)
    query = data.get('query')
    results = search(query)
    return jsonify(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8008)

