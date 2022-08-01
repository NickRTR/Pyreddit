import moviepy.editor as movie
import moviepy.video as video
import glob
import random

audioComments = glob.glob("./audio/comment-*.mp3")
backgroundVideos = glob.glob("./background/*.mp4")

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
    videoClip = movie.VideoFileClip(random.choice(backgroundVideos))
    # change resolution to 1080x1920
    return videoClip.set_audio(audioClip)

def editVideo(finalVideo, audioDuration):
    editedVideo = finalVideo.resize((1080, 1920))
    # loop background video to fit audio length
    editedVideo = video.fx.all.loop(finalVideo, duration=audioDuration)
    # fade in
    editedVideo = video.fx.all.fadein(editedVideo, 0.1)
    # fade out
    editedVideo = video.fx.all.fadeout(editedVideo, .1)

    return editedVideo

def createVideo():
    audio = joinQuestionWithComments()
    finalVideo = joinAudioWithVideo(audio)
    finalVideo = editVideo(finalVideo, audio.duration)
    finalVideo.write_videofile(outputVideo, fps=30)