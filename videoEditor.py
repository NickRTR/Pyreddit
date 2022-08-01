import moviepy.editor as movie
import moviepy.video as video
import moviepy.audio as audio
import glob
import random

audioComments = glob.glob("./audio/comment-*.mp3")
backgroundVideos = glob.glob("./background/video/*.mp4")
backgroundMusic = glob.glob("./background/music/*.mp3")

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

def addBackgroundMusic(videoClip):
    music = movie.AudioFileClip(random.choice(backgroundMusic))
    music = audio.fx.all.volumex(music, 0.5)
    joinedAudio = movie.CompositeAudioClip([videoClip.audio, music])
    videoClip.audio = joinedAudio
    return videoClip

def editVideo(finalVideo, audioDuration):
    editedVideo = finalVideo.resize((1080, 1920))
    # loop background video to fit audio length
    editedVideo = video.fx.all.loop(finalVideo, duration=audioDuration)
    # fade in
    editedVideo = video.fx.all.fadein(editedVideo, 0.1)
    # fade out
    editedVideo = video.fx.all.fadeout(editedVideo, .1)

    # # add text
    # textClip = movie.TextClip("Test", fontsize = 75, color = 'black') 
        
    # # setting position of text in the center and duration will be 10 seconds 
    # textClip= textClip.set_pos('center').set_duration(10) 
        
    # # Overlay the text clip on the first video clip 
    # editedVideo = movie.CompositeVideoClip([editedVideo, textClip]) 

    return editedVideo

def createVideo():
    audio = joinQuestionWithComments()
    finalVideo = joinAudioWithVideo(audio)
    finalVideo = addBackgroundMusic(finalVideo)
    finalVideo = editVideo(finalVideo, audio.duration)
    finalVideo.write_videofile(outputVideo, fps=30)