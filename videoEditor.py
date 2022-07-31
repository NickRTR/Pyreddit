import moviepy.editor as movie
import glob

audioComments = glob.glob("./audio/comment-*.mp3")

inputVideo = "./background/testBackground.mp4"
questionAudio = f"./audio/question.mp3"
outputVideo = f"./output/output.mp4"

def joinQuestionWithComments():
    # join all comments
    commentClips = [movie.AudioFileClip(c) for c in audioComments]
    comments = movie.concatenate_audioclips(commentClips)

    # join question with comments
    questionClip = movie.AudioFileClip(questionAudio)
    return movie.concatenate_audioclips([questionClip, comments])


def joinAudioWithVideo(audioClip):
    videoClip = movie.VideoFileClip(inputVideo)
    # change resolution to 1080x1920
    videoClip = videoClip.resize((1080, 1920))

    return videoClip.set_audio(audioClip)

def createVideo():
    audio = joinQuestionWithComments()
    finalVideo = joinAudioWithVideo(audio)
    finalVideo.write_videofile(outputVideo, fps=30)