import tweepy
import random
import time
from config import botkeys

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
    client.create_tweet(text=chooseTweet())
    time.sleep(7200)