from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import json
import os
from os.path import abspath, dirname
import subprocess
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, support_credentials=True)

anime_dir = os.getenv('ANIME_DIR')
vlc_path = os.getenv('VLC_PATH')

file_path = f'{dirname(abspath(__file__))}/anime.json'


def find_file(anime_name, episode):
    file_name = f'{anime_name} - {int(episode):02d}'
    for file in os.listdir(anime_dir):
            if file.startswith(file_name):
                return f'{anime_dir}/{file}'
    raise Exception('File not found', file_name)


def launch_file(anime_name, episode):
    try:
        anime = find_file(anime_name, episode)
        
        subprocess.Popen([vlc_path, f'\\{anime}'])
        return True
    except Exception as e:
        print(e)
        return False


def get_files():
    dir_list = os.listdir(anime_dir)
    new = {}

    for item in dir_list:
        split = item.rsplit('-', 1)
        anime_name = split[0].rstrip()

        if not new.get(anime_name):
            new[anime_name] = {}
            new[anime_name]['name'] = anime_name

        for str in split[1].split(' '):
            if str.isdigit():
                ep = int(str)
                break

        if new[anime_name].get('episodes'):
            new[anime_name]['episodes'].append(ep)
        else:
            new[anime_name]['episodes'] = [ep]

        with open(file_path, 'r') as f:
            data = json.load(f)

        if data.get(anime_name):
            watched = []
            for w in data[anime_name]['watched']:
                if w in new[anime_name]['episodes']:
                    watched.append(w)

            new[anime_name]['watched'] = watched
            new[anime_name]['broadcast'] = data[anime_name].get('broadcast') or ''
        else:
            new[anime_name]['watched'] = []
            new[anime_name]['broadcast'] = ''

    return new


def delete_file(anime_name, episode):
    try:
        file = find_file(anime_name, episode)
        os.remove(file)

        with open(file_path, 'r') as f:
            data = json.load(f)

        with open(file_path, 'w') as f:
            data.get(anime_name).get('watched').remove(int(episode))
            f.write(json.dumps(data, indent = 4))

        return True
    except Exception as e:
        print(e)
        return False


def update_anime_watched(anime_name, episode, watched):
    with open(file_path, 'r') as f:
            data = json.load(f)

    with open(file_path, 'w') as f:
        if (int(episode) in data.get(anime_name).get('watched')) and (watched.lower() == 'false' or watched == False):
            data.get(anime_name).get('watched').remove(int(episode))
        elif (int(episode) not in data.get(anime_name).get('watched')) and (watched.lower() == 'true' or watched == True):
            data.get(anime_name).get('watched').append(int(episode))

        f.write(json.dumps(data, indent = 4))


def update_anime_broadcast(anime_name, broadcast):
    with open(file_path, 'r') as f:
            data = json.load(f)

    with open(file_path, 'w') as f:
        data[anime_name]['broadcast'] = broadcast

        f.write(json.dumps(data, indent = 4))


def update_anime_list():
    anime_dict = get_files()
    with open(file_path, 'w') as f:
        f.write(json.dumps(anime_dict, indent = 4))
    return anime_dict


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
