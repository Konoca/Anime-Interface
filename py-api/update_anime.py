import json
from os.path import abspath, dirname
from get import get_files

file_path = f'{dirname(abspath(__file__))}/anime.json'

def update_anime_watched(anime_name, episode, watched):
    with open(file_path, 'r') as f:
            data = json.load(f)

    with open(file_path, 'w') as f:
        if (int(episode) in data.get(anime_name).get('watched')) and (watched == False or watched.lower() == 'false'):
            data.get(anime_name).get('watched').remove(int(episode))
        elif (int(episode) not in data.get(anime_name).get('watched')) and (watched == True or watched.lower() == 'true'):
            data.get(anime_name).get('watched').append(int(episode))

        f.write(json.dumps(data, indent = 4))


def update_anime_broadcast(anime_name, broadcast):
    with open(file_path, 'r') as f:
            data = json.load(f)

    with open(file_path, 'w') as f:
        data[anime_name]['broadcast'] = broadcast

        f.write(json.dumps(data, indent = 4))


def update_anime_description(anime_name, description):
    with open(file_path, 'r') as f:
            data = json.load(f)

    with open(file_path, 'w') as f:
        data[anime_name]['description'] = description

        f.write(json.dumps(data, indent = 4))


def update_anime_list():
    anime_dict = get_files()
    with open(file_path, 'w') as f:
        f.write(json.dumps(anime_dict, indent = 4))
    return anime_dict