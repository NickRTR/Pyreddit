from gtts import gTTS

def tts(text):
    language = "en"
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("speech.mp3")