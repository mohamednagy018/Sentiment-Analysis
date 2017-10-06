import feedparser as fd
import requests
from AWNDatabaseManagement import wn



import re
from html.parser import HTMLParser
from difflib import SequenceMatcher

# url = "http://feeds.bbci.co.uk/arabic/world/rss.xml" #BBC
# url2 = "https://aawsat.com/feed/news" #Awsaat
# url3 = "https://arabic.cnn.com/world/rss" #CNN

URLS = ["http://feeds.bbci.co.uk/arabic/world/rss.xml", "https://aawsat.com/feed/news",
        "https://arabic.cnn.com/world/rss"]
items = []
for url in URLS:
    feedparser = fd.parse(url)
    items.append(feedparser["items"])

# print(items[0]) #BBC summary , link = id , title --> Done
# print(items[1]) #Awsaat value ,  link = link , title --> Done
# print(items[2]) #CNN summary , link = link, title --> Done

# link , summary , title
summaries = []
links = []
titles = []

for item in items:
    for x in range(0, len(item)):
        if (item[x]["summary"]):
            summaries.append(item[x]["summary"])
        else:
            summaries.append(item[x]["value"])
        if (item[x]["link"]):
            links.append(item[x]["link"])
        else:
            links.append(item[x]["id"])
        titles.append(item[x]["title"])


def Get_HTML_Script(link):
   HTML_script =requests.get(link)
   Script=HTML_script.text
   return Script


from html.parser import HTMLParser

array = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    global array
    def handle_starttag(self, tag, attrs):
        #print ("Encountered a start tag:", tag)
        #array.append(tag)
        tag

    def handle_endtag(self, tag2):
        #print ("Encountered an end tag :", tag2)
        #array.append(tag2)
        tag2

    def handle_data(self, data):
        #print ("Encountered some data  :", data)
        array.append(data)


script = Get_HTML_Script(links[0])
# instantiate the parser and fed it some HTML
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(script)

print(array)
for x in array:
    if x == "\n" or x == "" or x == " ":
        array.remove(x)

print(array)


for x in array:
    print(x)
    print("_______________")