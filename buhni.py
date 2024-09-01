import tweepy
import random
import time
from config import botkeys

keyword = "carrot OR lettuce"

client = tweepy.Client(
    consumer_key = botkeys['API Key'],
    consumer_secret = botkeys['API Key Secret'],
    access_token = botkeys['Access Token'],
    access_token_secret = botkeys['Access Token Secret']
)

def chooseTweet():
    with open("tweets.txt", "r") as file:
        lines = file.readlines()
    return random.choice(lines).strip()

while True:
    timeline = client.search_recent_tweets(query = keyword, max_results = 10)
    for tweet in timeline:
        id = tweet.id
        client.like(id)
        client.create_tweet(in_reply_to_tweet_id = id, text = chooseTweet())
    time.sleep(7200)