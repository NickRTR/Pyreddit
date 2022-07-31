from TTS import tts
import praw

# TODO: env variable for secrets
 
reddit = praw.Reddit(client_id="sGiZv9kRIP8pqpJG1PQYmg",         # your client id
                               client_secret="Gx-jdV5vhbjvIOi_ehR-Vf85aoHREQ",      # your client secret
                               user_agent="Scraper")        # your user agent

subreddit = reddit.subreddit("askreddit")
 
def createAudioFiles():
    for post in subreddit.hot(limit=1):
        tts(post.title, "question")
        # TODO: sort comments (hot)
        submission = reddit.submission(post.id)
        for index, comment in enumerate(submission.comments):
            if (index > 1):
                break
            try:
                tts(comment.body, f"comment-{index}")
            except:
                continue