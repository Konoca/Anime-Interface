from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import json
import os
import subprocess

app = Flask(__name__)
CORS(app, support_credentials=True)
anime_dir = 'D:/PicturesVideos/Anime'


def find_file(anime_path, anime_name, episode):
    file_name = f'{anime_name} - {int(episode):02d}'
    for file in os.listdir(anime_path):
            if file.startswith(file_name):
                return f'{anime_path}/{file}'
    raise Exception('File not found', file_name)


def launch_file(anime_path, anime_name, episode):
    # anime_path='/Boruto/[Erai-raws] Boruto - Naruto Next Generations - 241 [1080p][Multiple Subtitle][7D8C4212]'
    try:
        anime = find_file(anime_path, anime_name, episode)
        
        subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe", f'\\{anime}'])
        return True
    except Exception as e:
        print(e)
        return False


def get_files(anime_path):
    # anime_path='/AOT final pt2/watched'
    dir = anime_dir + anime_path
    dir_list = os.listdir(dir)
    new = {}

    for item in dir_list:
        split = item.rsplit('-', 1)
        anime_name = split[0].rstrip()

        if not new.get(anime_name):
            new[anime_name] = {}
            new[anime_name]['name'] = anime_name
            new[anime_name]['path'] = dir

        for str in split[1].split(' '):
            if str.isdigit():
                ep = int(str)
                break

        if new[anime_name].get('episodes'):
            new[anime_name]['episodes'].append(ep)
        else:
            new[anime_name]['episodes'] = [ep]

        with open('anime.json', 'r') as f:
            data = json.load(f)

        if data.get(anime_name):
            watched = []
            for w in data[anime_name]['watched']:
                if w in new[anime_name]['episodes']:
                    watched.append(w)

            new[anime_name]['watched'] = watched
        else:
            new[anime_name]['watched'] = []

    return new


def delete_file(anime_path, anime_name, episode):
    try:
        file = find_file(anime_path, anime_name, episode)
        os.remove(file)

        with open('anime.json', 'r') as f:
            data = json.load(f)

        with open('anime.json', 'w') as f:
            data.get(anime_name).get('watched').remove(int(episode))
            f.write(json.dumps(data, indent = 4))

        return True
    except Exception as e:
        print(e)
        return False


def update_anime(anime_name, episode, watched):
    with open('anime.json', 'r') as f:
            data = json.load(f)

    with open('anime.json', 'w') as f:
        print(episode, type(episode), watched, type(watched))
        if (int(episode) in data.get(anime_name).get('watched')) and (watched.lower() == 'false' or watched == False):
            data.get(anime_name).get('watched').remove(int(episode))
        elif (int(episode) not in data.get(anime_name).get('watched')) and (watched.lower() == 'true' or watched == True):
            data.get(anime_name).get('watched').append(int(episode))

        f.write(json.dumps(data, indent = 4))


def update_anime_list():
    anime_dict = get_files('')
    with open('anime.json', 'w') as f:
        f.write(json.dumps(anime_dict, indent = 4))
    return anime_dict


@app.route('/anime', methods = ['GET'])
@cross_origin(supports_credentials=True)
def get_anime():
    anime_dict = update_anime_list()

    anime_name = request.args.get('name')
    episode = request.args.get('episode')

    if not anime_name and not episode:
        return jsonify(anime_dict)
    if anime_name and not episode:
        return jsonify(anime_dict.get(anime_name))
    else:
        print(anime_name, '-', episode)
        status = launch_file(anime_dict.get(anime_name).get('path'), anime_name, episode)
        return jsonify({"Status": status})


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
        status = delete_file(anime_dict.get(anime_name).get('path'), anime_name, episode)
        return jsonify({"Status": status})


@app.route('/anime', methods = ['PUT'])
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
        update_anime(anime_name, episode, watched)
        anime_dict = update_anime_list()
        return jsonify(anime_dict.get(anime_name))


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    update_anime_list()
