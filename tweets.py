import st_class
import tweepy, json
from tweet_auth import auth

l = st_class.MyStreamListener()
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
track = ['clinton', 'trump', 'sanders', 'cruz']
stream.filter(track=track)