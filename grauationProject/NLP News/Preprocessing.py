from nltk.tokenize import word_tokenize
from nltk.stem.isri import ISRIStemmer
from html.parser import HTMLParser
from difflib import SequenceMatcher
import requests
import re

text_nolink = ""


def ArabicStopwords():
    StopwordsFile = open('stopwords-ar.txt', encoding='utf-8')
    ArabicStopwords = StopwordsFile.read().split('\n')
    return ArabicStopwords


def ArabicStemming(text):
    st=ISRIStemmer()
    stemmedwords=[]
    word=text
    for w in word:
        stemmedwords.append(st.stem(w))
    return stemmedwords


def normalize(text_withlink):
    global text_nolink
    link = re.search(r'http\S+',text_withlink, flags=0)
    if link != None:
        text_nolink = re.sub(r"http\S+", "", text_withlink)
        print(link.group(0) + text_nolink)
        array_text = []
        for x in text_nolink.split("\n"):
            array_text.append(x)
        text_nolink = array_text[len(array_text) - 1]
        #text_nolink = "ستيفن بادوك، المشتبه بإطلاق النار في لاس فيغاس، كان مقامرا"
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
                search_obj = re.search(r'<div(.)*><p(.)*>(.)*</p></div>'  , x, flags=0)
                if search_obj:
                    Paragraph_array.append(search_obj.group())
            return Paragraph_array

        #print(str(similar(link.group(0), "http://www.bbc.com/arabic")) + "HHHHHHHHHHHHHHHHHHHHHHHHHHH")

        active_link = link.group(0)
        script = Get_HTML_Script(active_link)
        if script == "":
            return ""
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
            if similar(x,text_nolink)>=0.3:
                index=all_news.index(x)
                break
        while index!=len(all_news):
            print(all_news[index])
            news+=all_news[index]
            index=index+1
        print("-------------------------------------------------------------")
        print(news)
        return news
    else:
        return ""



