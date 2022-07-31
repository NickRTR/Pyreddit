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
 
def createAudioFiles():
    for post in subreddit.hot(limit=1):
        tts(post.title, "question")
        print("Created Title audio file")
        submission = reddit.submission(post.id)
        submission.comments.replace_more(limit = 0)
        for index, comment in enumerate(submission.comments):
            if (index >= 3):
                break
            tts(comment.body, f"comment-{index}")
            print(f"Created audio file for comment {index + 1}")
