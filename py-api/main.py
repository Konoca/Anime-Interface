from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from update_anime import update_anime_list, update_anime_watched, update_anime_broadcast
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


@app.route('/watch', methods = ['PUT'])
@cross_origin(supports_credentials=True)
def watch_anime():
    anime_dict = update_anime_list()

    anime_name = request.args.get('name')
    episode = request.args.get('episode')
    watched = request.args.get('watched')

    if not anime_name or not episode or not watched:
        return jsonify({"Error": "Missing information"})
    else:
        print(anime_name, '-', episode, '-', watched)
        update_anime_watched(anime_name, episode, watched)
        anime_dict = update_anime_list()
        return jsonify(anime_dict.get(anime_name))


@app.route('/broadcast', methods = ['PUT'])
@cross_origin(supports_credentials=True)
def broadcast_anime():
    anime_dict = update_anime_list()

    anime_name = request.args.get('name')
    broadcast = request.args.get('broadcast')

    if not anime_name or not broadcast:
        return jsonify({"Error": "Missing information"})
    else:
        update_anime_broadcast(anime_name, broadcast)
        anime_dict = update_anime_list()
        return jsonify(anime_dict.get(anime_name))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    update_anime_list()
