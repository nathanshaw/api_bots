import tweepy
# tokens should be shared in file
from access import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# search for tweets that mention CalArts
for tweet in tweepy.Cursor(api.search, q="CalArts").items(20):
    print(tweet.screen_name, tweet.text)

# search for tweets from CalArts
for tweet in tweepy.Cursor(api.search, q="*",
        geocode=cal_arts_lat+","+cal_arts_long+","+"10000m"):
    print(tweet.screen_name, tweet.text)

# 1 is the entire world
trending = api.trends_place(1)
