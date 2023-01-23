# Pyreddit

Pyreddit is a Reddit Bot that creates short videos about popular reddit posts in /r/AskReddit.

## How it works

1. fetch popular posts from /r/askreddit using the **Reddit Api**
2. Create screenshot's of fetched posts using **playwright**
3. Convert post text to audio file using Google's Text to Speech Package **gtts**
4. Concatenate Post images with corresponding audio files
5. Add random background music
6. Add random background video
7. Render video
8. Repeat this process as often as specified

## How to use it

1. git clone https://github.com/NickRTR/Pyreddit
2. cd Pyreddit
3. Populate the .env file with the secrets of your Reddit API instance
4. cd scripts
5. edit the `getContent(2)` parameter in main.py with the number of videos you want to create.
6. run `py .\main.py`
