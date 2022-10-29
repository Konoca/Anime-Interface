import json
import os


def find_file(anime_name, episode, path=os.getenv('ANIME_DIR')):
    for i in range(1, 4):
        file_name = f'{anime_name} - {int(episode):0{i}d} '
        for file in os.listdir('/anime'):
                if file.startswith(file_name):
                    return f"{path}/{file}"
    raise Exception('File not found', file_name)


def launch_file(file_path, anime_name, episode):
    try:
        anime_path = find_file(anime_name, episode)

        with open('/pipe/file.txt', 'w') as f:
            f.write(anime_path)

        return True
    except Exception as e:
        print(e, flush=True)
        return False


def get_files(file_path):
    dir_list = os.listdir('/anime')
    new = {}

    for item in dir_list:
        if item == 'anime.json' or item[:1] == '.':
            continue

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
            new[anime_name]['description'] = data[anime_name].get('description') or ''
        else:
            new[anime_name]['watched'] = []
            new[anime_name]['broadcast'] = ''
            new[anime_name]['description'] = ''

    for k,v in new.items():
        new[k]['episodes'] = sorted(new[k]['episodes'])

    return new
