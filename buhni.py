import tweepy
import sys

from credentials import twitter_bot_keys
auth = tweepy.OAuthHandler(twitter_bot_keys['API Key'], twitter_bot_keys['API Key Secret'])
auth.set_access_token(twitter_bot_keys['Access Token'], twitter_bot_keys['Access Token Secret'])
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK\n")
except:
    print("Error during authentication\n")

print(api.search_tweets("carrot"))