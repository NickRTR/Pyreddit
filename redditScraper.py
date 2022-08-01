import os
from dotenv import load_dotenv
import praw
from TTS import tts
from postImage import createImage
from videoEditor import createVideo

load_dotenv()

clientId = os.getenv("clientId")
clientSecret = os.getenv("clientSecret")
userAgent = os.getenv("userAgent")

reddit = praw.Reddit(client_id=clientId, client_secret=clientSecret, user_agent=userAgent)

subreddit = reddit.subreddit("askreddit")

def removeOldAudio():
    filelist = [ f for f in os.listdir("./audio") if f.endswith(".mp3") ]
    for f in filelist:
        os.remove(os.path.join("./audio", f))

def removeOldImages():
    filelist = [ f for f in os.listdir("./images") if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join("./images", f))
 
def getContent(limit):
    removeOldImages()
    removeOldAudio()
    run = 1
    for post in subreddit.hot(limit=limit):
        tts(post.title, "question")
        print("Created Title audio file")
        createImage(post.title, "question")
        submission = reddit.submission(post.id)
        submission.comments.replace_more(limit = 0)
        index = 0
        for comment in submission.comments:
            # limit character count
            if (len(comment.body) > 300):
                continue
            # limit to 3 comments
            if (index >= 5):
                break
            tts(comment.body, f"comment-{index}")
            createImage(comment.body, f"comment-{index}")
            print(f"Created audio file for comment {index + 1}")
            index += 1

        createVideo(run)
        run += 1
