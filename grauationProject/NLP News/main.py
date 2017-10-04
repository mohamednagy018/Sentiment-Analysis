from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import Preprocessing as p
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
#ids=['526343521','1000989876',' 52032722']
ids=['52032722'] #bbc

text_withlink=""
for x in range(0, 1):
    user= api.user_timeline(id = ids[x],count = 5)
    for x in range(0, 3):
        print(user[x].text)
        text_withlink=user[x].text
        TextBeforeEditing = p.normalize(text_withlink)
        if TextBeforeEditing != "":
            FilteredList = []
            ArabicStopwords = p.ArabicStopwords()
            for w in word_tokenize(TextBeforeEditing):
                if w not in ArabicStopwords:
                    FilteredList.append(w)
            print(FilteredList)
            print(p.ArabicStemming(FilteredList))
        print("--------------")



