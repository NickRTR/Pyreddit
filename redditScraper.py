import os
from dotenv import load_dotenv
import praw
from requests import delete
from TTS import tts
from postImage import createImages
from videoEditor import createVideo

load_dotenv()

clientId = os.getenv("clientId")
clientSecret = os.getenv("clientSecret")
userAgent = os.getenv("userAgent")

reddit = praw.Reddit(client_id=clientId, client_secret=clientSecret, user_agent=userAgent)

subreddit = reddit.subreddit("askreddit")

def deleteFiles(directory):
    filelist = [ f for f in os.listdir(directory) ]
    for f in filelist:
        os.remove(os.path.join(directory, f))
 
def getContent(limit):
    imageList = []

    deleteFiles("./images")
    deleteFiles("./audio")
    deleteFiles("./output")

    run = 1
    totalDuration = 0

    for post in subreddit.hot(limit=limit):
        totalDuration += tts(post.title, "question")
        print("Created Title audio file")

        imageList.append({"url": post.url, "title": "question"})

        submission = reddit.submission(post.id)
        submission.comments.replace_more(limit = 0)
        index = 0
  
        for comment in submission.comments:
            # limit character count
            if (len(comment.body) > 600):
                continue
            totalDuration += tts(comment.body, f"comment-{index}")
            # limit video to 60 s
            if (totalDuration > 60):
                # delete last tts
                os.remove(f"./audio/comment-{index}.mp3")
                break
            imageList.append({"url": f"https://www.reddit.com{comment.permalink}", "title": f"comment-{index}", "commentId": comment.id})
            print(f"Created audio file for comment {index + 1}")
            index += 1

        createImages(imageList)

        createVideo(run)
        run += 1
