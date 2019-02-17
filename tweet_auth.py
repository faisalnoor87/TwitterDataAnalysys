import tweepy

access_tocken = ""
access_tocken_secret = ""

consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_tocken, access_tocken_secret)
