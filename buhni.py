import tweepy
from credentials import twitter_bot_keys

client = tweepy.Client(bearer_token=twitter_bot_keys['Bearer token'])

query = "Carrot"

tweets = client.search_recent_tweets(query=query, max_results=10)

if tweets.data:
    for tweet in tweets.data:
        print(f"Tweet: {tweet.text}")
else:
    print("No tweets found.")