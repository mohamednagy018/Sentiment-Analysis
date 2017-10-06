import feedparser as fd
import requests
import re
from html.parser import HTMLParser
from difflib import SequenceMatcher


# url = "http://feeds.bbci.co.uk/arabic/world/rss.xml" #BBC
# url2 = "http://www.shorouknews.com/sports/local-sports/rss" #shorouknews
# url3 = "https://arabic.cnn.com/world/rss" #CNN
import time

URLS = ["http://www.shorouknews.com/sports/local-sports/rss","https://arabic.cnn.com/world/rss","http://feeds.bbci.co.uk/arabic/world/rss.xml"]
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


print(items[0])

def Get_HTML_Script(link):
   HTML_script =requests.get(link)
   Script=HTML_script.text
   return Script


for x in range(0,len(links)):
    script = Get_HTML_Script(links[x])
    print(links[x])
    final_news = []
    string = ""
    if("bbc" in links[x]):
        content2 = re.findall(r'<p class="story-body__introduction">(.*?)</p>',str(script))
        if(content2 != ""):
            final_news.append(content2)

        content = re.findall(r'<p>(.*?)</p>', str(script))
        final_news = content2 + content
    elif "cnn" in links[x]:
        content2 = re.findall(r'<p class="story-body__introduction">(.*?)</p>', str(script))
        if (content2 != ""):
            final_news.append(content2)

        content = re.findall(r'<p>(.*?)</p>', str(script))
        content = content[:len(content)-2]
        final_news = content2 + content

    elif "shorouknews" in links[x]:
        content = re.findall(r'<p>(.*?)</p>', str(script))
        content = content[:len(content)]
        final_news =  content

    for x in final_news:
        print(x)


