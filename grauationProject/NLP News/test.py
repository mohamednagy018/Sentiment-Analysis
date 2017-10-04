import feedparser
from nltk.stem.isri import ISRIStemmer
from html.parser import HTMLParser
from difflib import SequenceMatcher
import requests
import re

python_wiki_rss_url = "http://www.youm7.com/rss/SectionRss?SectionID=65"

feed = feedparser.parse( python_wiki_rss_url )


print(feed["items"])

for item in feed["items"]:
    url = item["link"]
    print(url)




text_nolink = "الخارجية تعلن الحركة التكميلية لتنقلات أعضاء السلك الدبلوماسى والقنصلى"
text_nolink = re.sub(r'[:!@#$%^&*;,`''""(){}]', "", text_nolink)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def Get_HTML_Script(link):
   HTML_script =requests.get(link)
   Script=HTML_script.text
   return Script

def Get_Paragraph(HTML_script):
    Paragraph_array = []
    for x in HTML_script.split('\n'):
        search_obj = re.search(r'<p(.)*>(.)*<span(.)*>(.)*</span>(.)*</p>'  , x, flags=0)
        if search_obj:
            Paragraph_array.append(search_obj.group())
    return Paragraph_array


active_link = url
script = Get_HTML_Script(active_link)
Paragraph_array = Get_Paragraph(script)

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
    print("Text -->" + x + " Score --> " + str(similar(x,text_nolink)))
    if similar(x,text_nolink)>=0.8:
        index=all_news.index(x)
        break
while index!=len(all_news):
    print(all_news[index])
    news+=all_news[index]
    index=index+1
print("-------------------------------------------------------------")
print(news)


