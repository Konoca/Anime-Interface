from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv

from update_anime import update_anime_list, update_anime_watched, update_anime_broadcast, update_anime_description
from get import find_file, launch_file, get_files
from delete import delete_file

load_dotenv()

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/watch', methods = ['GET'])
@cross_origin(supports_credentials=True)
def open_anime():
    anime_dict = update_anime_list()

    anime_name = request.args.get('name')
    episode = request.args.get('episode')

    print(anime_name, '-', episode)
    status = launch_file(anime_name, episode)
    return jsonify({"Status": status})


@app.route('/anime', methods = ['GET'])
@cross_origin(supports_credentials=True)
def get_anime_details():
    anime_dict = update_anime_list()

    anime_name = request.args.get('name')
    episode = request.args.get('episode')

    if not anime_name and not episode:
        return jsonify(anime_dict)
    if anime_name and not episode:
        return jsonify(anime_dict.get(anime_name))
    else:
        return jsonify({"Error": "Missing information"})


@app.route('/anime', methods = ['DELETE'])
@cross_origin(supports_credentials=True)
def delete_anime():
    anime_dict = update_anime_list()

    anime_name = request.args.get('name')
    episode = request.args.get('episode')

    if not anime_name or not episode:
        return jsonify({"Error": "Missing information"})
    else:
        print(anime_name, '-', episode)
        status = delete_file(anime_name, episode)
        return jsonify({"Status": status})


@app.route('/anime', methods = ['PUT'])
@cross_origin(supports_credentials=True)
def update_anime_data():
    anime_dict = update_anime_list()

    anime_info = json.loads(request.data)

    anime_name = anime_info.get('name')
    episode = anime_info.get('episode')
    watched = anime_info.get('watched')
    broadcast = anime_info.get('broadcast')
    description = anime_info.get('description')

    print(anime_info)

    if not anime_name:
        return jsonify({"Error": "Missing information"})

    if episode and watched:
        update_anime_watched(anime_name, episode, watched)

    if broadcast:
        update_anime_broadcast(anime_name, broadcast)

    if description:
        update_anime_description(anime_name, description)

    anime_dict = update_anime_list()
    return jsonify(anime_dict.get(anime_name))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    update_anime_list()
