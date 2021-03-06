import json
import os
from functions.get import get_files


def update_anime_watched(file_path, anime_name, episode, watched:bool=False):
    with open(file_path, 'r') as f:
            data = json.load(f)

    if (int(episode) in data.get(anime_name).get('watched')) and (watched == False):
        data.get(anime_name).get('watched').remove(int(episode))
    elif (int(episode) not in data.get(anime_name).get('watched')) and (watched == True):
        data.get(anime_name).get('watched').append(int(episode))       

    with open(file_path, 'w') as f:
        f.write(json.dumps(data, indent = 4))


def update_anime_broadcast(file_path, anime_name, broadcast):
    with open(file_path, 'r') as f:
            data = json.load(f)

    with open(file_path, 'w') as f:
        data[anime_name]['broadcast'] = broadcast

        f.write(json.dumps(data, indent = 4))


def update_anime_description(file_path, anime_name, description):
    with open(file_path, 'r') as f:
        data = json.load(f)

    with open(file_path, 'w') as f:
        data[anime_name]['description'] = description

        f.write(json.dumps(data, indent = 4))


def update_anime_list(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('{}')

    if os.getenv('DB_MODE').lower() == 'false':
        anime_dict = get_files(file_path)
        with open(file_path, 'w') as f:
            f.write(json.dumps(anime_dict, indent = 4))
    else:
        with open(file_path, 'r') as f:
            anime_dict = json.load(f)

    return anime_dict