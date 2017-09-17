from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import Preprocessing
from nltk.tokenize import word_tokenize
import tweepy

# consumer key, consumer secret, access token, access secret.
ckey = "APvGgEdCuQNmKCV1xK0pR9Ytj"
csecret = "hYOXjK3wDXwfk0OYJ4zNKMCA0yl09JsoE28GQcvnIvTAlUrQBG"
atoken = "899290209413718018-HYZzw7fHjGOAXrNcrVekT2zWImObgQJ"
asecret = "gnM1W1pak2s9BqVEznmZmWleGXmXKPcwXHvwhuwO5rnhi"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

user= api.user_timeline(id='526343521',count = 100)


for x in range(1, 90):
    print(str(x)+"--------")
    print(user[x].text)
    print(user[x].created_at)


#twitterStream.filter(follow=['759251'])
