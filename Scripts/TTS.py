import re
from gtts import gTTS
from mutagen.mp3 import MP3

def tts(text, title):
    # test = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
    text = re.sub('http[s]?://\S+', '', text)
    print(text)
    speech = gTTS(text=text, lang="en", slow=False)
    speech.save(f"../assets/audio/{title}.mp3")
    return MP3(f"../assets/audio/{title}.mp3").info.length # return length to calculate comments
