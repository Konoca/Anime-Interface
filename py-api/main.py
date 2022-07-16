from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import json
import os
from os.path import abspath, dirname
from dotenv import load_dotenv
import logging

from functions.update_anime import update_anime_list, update_anime_watched, update_anime_broadcast, update_anime_description
from functions.get import find_file, launch_file, get_files
from functions.delete import delete_file
from functions.post import add_new_anime
from functions.search import search

load_dotenv()
logging.basicConfig(filename="error.log", level=logging.DEBUG)

app = Flask(__name__)
CORS(app, support_credentials=True)

file_path = '/anime/anime.json'


@app.route('/watch', methods = ['GET'])
@cross_origin(supports_credentials=True)
def open_anime():
    if os.getenv('DB_MODE').lower() == 'true': return jsonify({"Status": False})

    anime_dict = update_anime_list(file_path)

    anime_name = request.args.get('name')
    episode = request.args.get('episode')

    print(anime_name, '-', episode)
    status = launch_file(file_path, anime_name, episode)
    return jsonify({"Status": status})


@app.route('/mode', methods = ['GET'])
@cross_origin(supports_credentials=True)
def get_mode():
    db_mode = os.getenv('DB_MODE')

    if db_mode.lower() == 'true':
        mode = "DB"
    else:
        mode = "Interface"

    return jsonify({"Mode": mode})


@app.route('/search', methods = ['PUT'])
@cross_origin(supports_credentials=True)
def search_anime():
    data = json.loads(request.data)

    query = data.get('query')
    
    results = search(query)

    return jsonify(results)


@app.route('/anime', methods = ['GET'])
@cross_origin(supports_credentials=True)
def get_anime_details():
    anime_dict = update_anime_list(file_path)

    anime_name = request.args.get('name')

    if not anime_name:
        return jsonify(anime_dict)
    if anime_name:
        return jsonify(anime_dict.get(anime_name))


@app.route('/anime', methods = ['DELETE'])
@cross_origin(supports_credentials=True)
def delete_anime():
    anime_dict = update_anime_list(file_path)

    anime_name = request.args.get('name')
    episode = request.args.get('episode')

    if not anime_name or not episode:
        return jsonify({"Error": "Missing information"})
    else:
        print(anime_name, '-', episode)
        status = delete_file(file_path, anime_name, episode)
        return jsonify({"Status": status})


@app.route('/anime', methods = ['PUT'])
@cross_origin(supports_credentials=True)
def update_anime_data():
    anime_dict = update_anime_list(file_path)

    anime_info = json.loads(request.data)

    anime_name = anime_info.get('name')
    episode = anime_info.get('episode')
    watched = anime_info.get('watched')
    broadcast = anime_info.get('broadcast')
    description = anime_info.get('description')

    print(anime_info)

    if not anime_name:
        return jsonify({"Error": "Missing information"})

    if episode and (watched == True or watched == False):
        print(anime_name, episode, watched)
        update_anime_watched(file_path, anime_name, episode, watched)

    if broadcast:
        update_anime_broadcast(file_path, anime_name, broadcast)

    if description or description == '':
        update_anime_description(file_path, anime_name, description)

    anime_dict = update_anime_list(file_path)
    return jsonify(anime_dict.get(anime_name))


@app.route('/anime', methods = ['POST'])
@cross_origin(supports_credentials=True)
def add_anime():
    anime_dict = update_anime_list(file_path)

    anime_info = json.loads(request.data)

    anime_name = anime_info.get('name')

    print(anime_info)

    if not anime_name:
        return jsonify({"Error": "Missing information"})

    add_new_anime(file_path, anime_info)

    anime_dict = update_anime_list(file_path)
    return jsonify(anime_dict.get(anime_name))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
    update_anime_list(file_path)
