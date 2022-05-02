import json
import os

from functions.get import find_file

def delete_file(file_path, anime_name, episode):
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