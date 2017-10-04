import feedparser as fd
import requests
import re
from html.parser import HTMLParser
from difflib import SequenceMatcher

url = "http://feeds.bbci.co.uk/arabic/world/rss.xml" #BBC
url2 = "https://aawsat.com/feed/news" #Awsaat
url3 = "https://arabic.cnn.com/world/rss" #CNN

URLS = ["http://feeds.bbci.co.uk/arabic/world/rss.xml","https://aawsat.com/feed/news","https://arabic.cnn.com/world/rss"]
items = []
for url in URLS:
    feedparser = fd.parse(url)
    items.append(feedparser["items"])


#print(items[0]) #BBC summary , link = id , title --> Done
#print(items[1]) #Awsaat value ,  link = link , title --> Done
#print(items[2]) #CNN summary , link = link, title --> Done

#link , summary , title
summaries = []
links = []
titles = []

for item in items:
    for x in range(0,len(item)):
        if(item[x]["summary"]):
            summaries.append(item[x]["summary"])
        else:
            summaries.append(item[x]["value"])
        if(item[x]["link"]):
            links.append(item[x]["link"])
        else:
            links.append(item[x]["id"])
        titles.append(item[x]["title"])


#print(summaries[1])
#print(links[1])
#print(titles[1])
#--------------------------------------------------------------------------------------------------


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
class MyHTMLParser(HTMLParser):
    check_type = ""
    def handle_starttag(self, tag, attrs):
        self.check_type=tag

    def handle_data(self, data):
       if len(Paragraph_array)>0:
           if self.check_type=="p" or self.check_type=="a":
             all_news.append(data)
       else:
            if self.check_type!="a":
                all_news.append(data)
       self.check_type=""


for item_news in range(0,len(links)):
    print(summaries[item_news])
    print(links[item_news])
    print(titles[item_news])
    print("####################################################################################")
    script=Get_HTML_Script(links[item_news])
    #print(script)
    Paragraph_array=Get_Paragraph(script)
    check_type=""
    all_news=[]
    parser = MyHTMLParser()
    if len(Paragraph_array)>0:
     for x in Paragraph_array:
      parser.feed(x)
    else:
        parser.feed(script)
    news=""
    index=0
    for x in all_news:
        #print(similar(x,summaries[item_news]))
        if similar(x,summaries[item_news])>=.6:
            index=all_news.index(x)
            break
    while index!=len(all_news):
        print(all_news[index])
        news+=all_news[index]
        index=index+1
    print("-------------------------------------------------------------")
   #print(news)

 
