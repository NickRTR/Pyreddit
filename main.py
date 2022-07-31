from TTS import tts
import moviepy.editor as movie

title = "Test"

tts("This is a test...", title)

inputVideo = "./background/testBackground.mp4"
inputAudio = f"./audio/{title}.mp3"
outputVideo = f"./output/{title}.mp4"

videoClip = movie.VideoFileClip(inputVideo)

# change resolution to 1080x1920
videoClip = videoClip.resize((1080, 1920))

audioClip = movie.AudioFileClip(inputAudio)
finalClip = videoClip.set_audio(audioClip)
finalClip.write_videofile(outputVideo, fps=30)
