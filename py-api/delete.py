import json
import os
from os.path import abspath, dirname

from get import find_file

file_path = f'{dirname(abspath(__file__))}/anime.json'

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