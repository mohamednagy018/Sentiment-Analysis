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
#ids=['526343521','1000989876',' 52032722']
ids=['52032722']

text_withlink=""
for x in range(0, 1):
    user= api.user_timeline(id = ids[x],count = 5)
    for x in range(0, 5):
        print(user[x].text)
        text_withlink=user[x].text
        TextBeforeEditing = user[x].text
        FilteredList = []
        ArabicStopwords = Preprocessing.ArabicStopwords()
        for w in word_tokenize(TextBeforeEditing):
            if w not in ArabicStopwords:
                FilteredList.append(w)
        print(FilteredList)
        print(Preprocessing.ArabicStemming(FilteredList))






import requests
import re
from html.parser import HTMLParser
from difflib import SequenceMatcher

text_nolink =  re.sub(r"http\S+", "", text_withlink)
array_text = []
for x in text_nolink.split("\n"):
    array_text.append(x)
text_nolink=array_text[len(array_text)-1]
text_nolink="مطاعم أمريكية توقف بث مباريات كرة القدم رفضا لحركة نحن"
text_nolink= re.sub(r'[:!@#$%^&*;,`''""(){}]',"", text_nolink)
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def Get_HTML_Script(link):
   HTML_script =requests.get(link)
   Script=HTML_script.text
   return Script

def Get_Paragraph(HTML_script):
    Paragraph_array = []
    for x in HTML_script.split('\n'):
        search_obj = re.search(r'<p(.)*>(.)*</p>'  , x, flags=0)
        if search_obj:
            Paragraph_array.append(search_obj.group())
    return Paragraph_array
script=Get_HTML_Script("https://t.co/ycAYd4TpmE")
Paragraph_array=Get_Paragraph(script)
check_type=""
all_news=[]
class MyHTMLParser(HTMLParser):
    check_type = ""
    def handle_starttag(self, tag, attrs):
        self.check_type=tag

    def handle_data(self, data):
       if len(Paragraph_array)>0:
           if self.check_type=="p":
             all_news.append(data)
       else:
            if self.check_type!="a":
                all_news.append(data)
       self.check_type=""
parser = MyHTMLParser()
if len(Paragraph_array)>0:
 for x in Paragraph_array:
  parser.feed(x)
else:
    parser.feed(script)
news=""
index=0
for x in all_news:
    print(similar(x,text_nolink))
    if similar(x,text_nolink)>=.3:
        index=all_news.index(x)
        break
while index!=len(all_news):
    print(all_news[index])
    news=all_news[index]+news
    index=index+1
#print("-------------------------------------------------------------")
#print(news)

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