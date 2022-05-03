import json

def add_new_anime(file_path, anime_data):
    with open(file_path, 'r') as f:
        data = json.load(f)

    data[anime_data.get('name')] = anime_data

    with open(file_path, 'w') as f:
        f.write(json.dumps(data, indent = 4))