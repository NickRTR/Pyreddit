import moviepy.editor as movie
import moviepy.video as video
import moviepy.audio as audio
import glob
import random

backgroundVideos = glob.glob("../assets/background/video/*.mp4")
backgroundMusic = glob.glob("../assets/background/music/*.mp3")

def createAudioWithImages():
    questionAudio = movie.AudioFileClip(f"../assets/audio/question.mp3")
    questionImage = movie.ImageClip("../assets/images/question.png").set_duration(questionAudio.duration)
    questionVideo = questionImage.set_audio(questionAudio)

    comments = []
    audioFiles = glob.glob("../assets/audio/comment-*.mp3")
    for index, audioFile in enumerate(audioFiles):
        commentAudio = movie.AudioFileClip(audioFile)
        commentImage = movie.ImageClip(f"../assets/images/comment-{index}.png").set_duration(commentAudio.duration)
        commentVideo = commentImage.set_audio(commentAudio)
        comments.append(commentVideo)

    # join all comments together
    commentsClip = movie.concatenate_videoclips(comments)

    # join question with comments
    return movie.concatenate_videoclips([questionVideo, commentsClip])

def addBackgroundVideo(videoClip):
    print("adding background video")
    # loop background video to fit audio length
    backgroundClip = movie.VideoFileClip(random.choice(backgroundVideos))
    # adapt duration to audio (by looping or cutting)
    backgroundClip = video.fx.all.loop(backgroundClip, None, videoClip.duration)
    return movie.CompositeVideoClip([backgroundClip, videoClip.set_position("center").set_opacity(0.85)])

def addBackgroundMusic(videoClip, duration):
    print("adding background music")
    music = movie.AudioFileClip(random.choice(backgroundMusic))
    # adapt duration to video (by looping or cutting)
    music = video.fx.all.loop(music, None, duration)
    music = audio.fx.all.volumex(music, 0.2)
    joinedAudio = movie.CompositeAudioClip([videoClip.audio, music])
    videoClip.audio = joinedAudio
    return videoClip

def editVideo(finalVideo):
    editedVideo = finalVideo.resize((1080, 1920))
    # fade out
    editedVideo = video.fx.all.fadeout(editedVideo, .2)

    return editedVideo

def createVideo(videoNumber):
    rawVideo = createAudioWithImages()
    video = addBackgroundVideo(rawVideo)
    video = addBackgroundMusic(video, rawVideo.duration)
    video = editVideo(video)
    video.write_videofile(f"../output/output-{videoNumber}.mp4", fps=30)