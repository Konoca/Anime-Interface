# Anime Interface
A local website that allows you to manage anime files you have downloaded onto your computer. Allows you to mark episodes as watched, open the episode and start watching, and delete the episode from your computer. Also let's you keep note of any descriptions you might have of an Anime, as well as when that Anime broadcasts a new episode (if it is still airing).

# Prerequisites
- Docker
- WSL2 (if using Windows)
- Ubuntu on Windows (if using Windows)

# How to run (Windows)
Create .env file using the template below, then run the following commands inside project folder inside of Powershell:
```
docker-compose up -d --build --force-rebuild
```
Afterwards, open up an Ubuntu terminal, navigate to where the code is located (mnt/<drive>/<path>) and type(will have to be repeated every time you turn on your computer):
```
./pipe.sh &
disown
```
You can close both Powershell and Ubuntu afterwards.

# How to run (Mac/Linux)
Create .env file using the template below, then run the following commands inside project folder:
```
docker-compose up -d --build --force-rebuild
./pipe.sh & ; disown
```
'```./pipe.sh & ; disown```' will need to be retyped after machine restarts

# .env file
Create copy of .env-template and rename as ".env". Below are descriptions of all the variables

| Key | Description |
|:--- |:----------- |
| ANIME_DIR | Directory to where all Anime files on computer are stored.
| DB_MODE  | Sets system into Database mode rather than Interface mode. If true, ANIME_DIR_ON_COMPUTER does not need to be set.

# Modes (pictures not updated)
## Interface Mode
Manages files on computer

<img src="https://i.imgur.com/WyUzrkG.jpg" width=75% height=75%>
<img src="https://i.imgur.com/A5locmV.jpg" width=75% height=75%>
<img src="https://i.imgur.com/hVOxHuQ.jpg" width=50% height=50%>

## Database Mode
Only keeps track of anime information

<img src="https://i.imgur.com/4ZyIfk0.jpg" width=75% height=75%>
<img src="https://i.imgur.com/pwEejsG.jpg" width=50% height=50%>
<img src="https://i.imgur.com/YjVzCEB.jpg" width=50% height=50%>
