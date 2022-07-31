from gtts import gTTS

def tts(text, title):
    language = "en"
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(f"./audio/{title}.mp3")
