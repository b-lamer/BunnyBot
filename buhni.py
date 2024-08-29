import tweepy
import random
import time
from credentials import botkeys

client = tweepy.Client(
    consumer_key = botkeys['API Key'],
    consumer_secret = botkeys['API Key Secret'],
    access_token = botkeys['Access Token'],
    access_token_secret = botkeys['Access Token Secret']
)

client.create_tweet(text="I do be testing")