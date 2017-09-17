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


user= api.user_timeline(id='526343521',count = 200)


for x in range(0, 200):
    print(user[x].text)
    TextBeforeEditing = user[x].text
    FilteredList = []
    ArabicStopwords = Preprocessing.ArabicStopwords()
    for w in word_tokenize(TextBeforeEditing):
        if w not in ArabicStopwords:
            FilteredList.append(w)
    print(FilteredList)
    print(Preprocessing.ArabicStemming(FilteredList))












"""
class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        print("#################################  1")
        tweet = all_data["text"]
        time = all_data['created_at']
        print(time)
        print(tweet)
        print("#################################  2")
        tweet_id = all_data['id']
      #  print(tweet_id)
        retweet = api.retweets(tweet_id)
       # print(retweet)
        TextBeforeEditing = tweet

        FilteredList = []
        ArabicStopwords = Preprocessing.ArabicStopwords()

        for w in word_tokenize(TextBeforeEditing):
            if w not in ArabicStopwords:
                FilteredList.append(w)
        print(FilteredList)
        print(Preprocessing.ArabicStemming(FilteredList))
        return True

    def on_error(self, status):
        print(status)


twitterStream = Stream(auth, listener())
twitterStream.filter(follow=['759251'])"""