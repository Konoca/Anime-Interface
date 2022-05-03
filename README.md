# Anime Interface
A local website that allows you to manage anime files you have downloaded onto your computer. Allows you to mark episodes as watched, open the episode and start watching, and delete the episode from your computer. Also let's you keep note of any descriptions you might have of an Anime, as well as when that Anime broadcasts a new episode (if it is still airing)

<img src="https://i.imgur.com/w5VMBfJ.jpg" width=75% height=75%>
<img src="https://i.imgur.com/hVOxHuQ.jpg" width=50% height=50%>

# How to set up

## Frontend
### Windows / Mac
1. Download nodejs: https://nodejs.org/en/download/
2. Install angular: `npm install -g @angular/cli`
3. Go into ng_frontend directory: `cd ng_frontend`
4. Install dependencies: `npm install`
5. Start frontend using: `ng serve`

### Linux
```
$ sudo apt update
$ sudo apt install nodejs
$ npm install -g @angular/cli
$ cd ng_frontend
$ npm install
$ ng serve
```

## Backend
### Windows / Mac
1. Download python: https://www.python.org/downloads/
2. Go into py-api directory: `cd py-api`
3. Create virtual environment: `python -m venv venv`
4. Enable venv: `/venv/Scripts/activate` (Mac -> `source venv/bin/activate`)
5. Install dependencies: `pip install -r requirements.txt`
6. Create .env (look below)
7. Run backend using: `python main.py`

### Linux
```
$ sudo apt-get install python3.8
$ cd py-api
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 main.py
```

# .env file
Create copy of .env-template and rename as ".env". Below are descriptions of all the variables

| Key | Description |
|:--- |:----------- |
| ANIME_DIR | Directory to where all Anime files on computer are stored |
| VLC_PATH | Path to where "vlc.exe" is located on computer, typically looks something similar to "C:/Program Files/VideoLAN/VLC/vlc.exe" for windows |
| DB_MODE | If true, neither of the above values need to be set. Sets system into Database mode rather than Interface mode.

# TODO
- Ability to add anime when in DB mode
- Maybe add a way to store JSON into some external DB, and fetch on startup?