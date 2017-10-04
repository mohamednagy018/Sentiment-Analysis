import feedparser as fd


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


print(summaries[0])
print(links[0])
print(titles[0])
 
