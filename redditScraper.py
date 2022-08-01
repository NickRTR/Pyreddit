import os
from dotenv import load_dotenv
import praw
from TTS import tts

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
 
def createAudioFiles():
    removeOldAudio()
    for post in subreddit.hot(limit=1):
        tts(post.title, "question")
        print("Created Title audio file")
        submission = reddit.submission(post.id)
        submission.comments.replace_more(limit = 0)
        for index, comment in enumerate(submission.comments):
            # limit to 3 comments
            if (index >= 3):
                break
            tts(comment.body, f"comment-{index}")
            print(f"Created audio file for comment {index + 1}")
