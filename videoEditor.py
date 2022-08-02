import moviepy.editor as movie
import moviepy.video as video
import moviepy.audio as audio
import glob
import random

audioComments = glob.glob("./audio/comment-*.mp3")
commentImages = glob.glob("./images/comment-*.png")
backgroundVideos = glob.glob("./background/video/*.mp4")
backgroundMusic = glob.glob("./background/music/*.mp3")

questionAudio = f"./audio/question.mp3"

def createAudioWithImages():
    comments = []
    for index, audioComment in enumerate(audioComments):
        commentClip = movie.AudioFileClip(audioComment)
        imageClip = movie.ImageClip(commentImages[index])
        videoClip = imageClip.set_audio(commentClip)
        videoClip.duration = commentClip.duration
        comments.append(videoClip)

    # join all comments together
    commentsClip = movie.concatenate_videoclips(comments)

    questionClip = movie.AudioFileClip(questionAudio)
    imageClip = movie.ImageClip("./images/question.png")
    question = imageClip.set_audio(questionClip)
    question.duration = questionClip.duration

    # join question with comments
    return movie.concatenate_videoclips([question, commentsClip])

def addBackgroundVideo(videoClip):
    backgroundClip = movie.VideoFileClip(random.choice(backgroundVideos))
    return movie.CompositeVideoClip([backgroundClip, videoClip.set_position("center").set_opacity(0.85)])

def addBackgroundMusic(videoClip):
    music = movie.AudioFileClip(random.choice(backgroundMusic))
    music = audio.fx.all.volumex(music, 0.2)
    joinedAudio = movie.CompositeAudioClip([videoClip.audio, music])
    videoClip.audio = joinedAudio
    return videoClip

def editVideo(finalVideo, audioDuration):
    editedVideo = finalVideo.resize((1080, 1920))
    # loop background video to fit audio length
    editedVideo = video.fx.all.loop(finalVideo, duration=audioDuration)
    # fade in
    editedVideo = video.fx.all.fadein(editedVideo, .1)
    # fade out
    editedVideo = video.fx.all.fadeout(editedVideo, .2)

    return editedVideo

def createVideo(videoNumber):
    rawVideo = createAudioWithImages()
    video = addBackgroundVideo(rawVideo)
    video = addBackgroundMusic(video)
    video = editVideo(video, rawVideo.duration)
    video.write_videofile(f"./output/output-{videoNumber}.mp4", fps=30)