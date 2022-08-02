from gtts import gTTS
from mutagen.mp3 import MP3

def tts(text, title):
    language = "en"
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(f"../assets/audio/{title}.mp3")
    return MP3(f"../assets/audio/{title}.mp3").info.length # return length to calculate comments
