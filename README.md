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
8. Repeat as often as specified