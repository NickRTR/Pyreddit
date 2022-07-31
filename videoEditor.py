import moviepy.editor as movie

inputVideo = "./background/testBackground.mp4"
inputAudio = f"./audio/question.mp3"
outputVideo = f"./output/question.mp4"

videoClip = movie.VideoFileClip(inputVideo)

# change resolution to 1080x1920
videoClip = videoClip.resize((1080, 1920))

audioClip = movie.AudioFileClip(inputAudio)
finalClip = videoClip.set_audio(audioClip)

def createVideo():
    finalClip.write_videofile(outputVideo, fps=30)
