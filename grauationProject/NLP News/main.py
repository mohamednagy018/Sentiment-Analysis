from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import Preprocessing
from nltk.tokenize import word_tokenize

# consumer key, consumer secret, access token, access secret.
ckey = "APvGgEdCuQNmKCV1xK0pR9Ytj"
csecret = "hYOXjK3wDXwfk0OYJ4zNKMCA0yl09JsoE28GQcvnIvTAlUrQBG"
atoken = "899290209413718018-HYZzw7fHjGOAXrNcrVekT2zWImObgQJ"
asecret = "gnM1W1pak2s9BqVEznmZmWleGXmXKPcwXHvwhuwO5rnhi"


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        print(tweet)
        TextBeforeEditing = tweet  #############################################################################Tweets

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


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)



twitterStream = Stream(auth, listener())
twitterStream.filter(track=["egypt"],languages=["ar"])

