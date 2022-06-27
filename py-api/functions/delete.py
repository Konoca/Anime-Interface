import json
import os
import logging

from functions.get import find_file

def delete_file(file_path, anime_name, episode):
    try:
        if os.getenv('DB_MODE').lower() == 'false':
            file = find_file(anime_name, episode, path="/anime")
            os.remove(file)

        with open(file_path, 'r') as f:
            data = json.load(f)

        if (int(episode) in data.get(anime_name).get('episodes')):
            data.get(anime_name).get('episodes').remove(int(episode))
        if (int(episode) in data.get(anime_name).get('watched')):
            data.get(anime_name).get('watched').remove(int(episode))

        if (data.get(anime_name).get('episodes') == []):
            data.pop(anime_name)

        with open(file_path, 'w') as f:
            f.write(json.dumps(data, indent = 4))

        return True
    except Exception as e:
        logging.debug(e)
        return False