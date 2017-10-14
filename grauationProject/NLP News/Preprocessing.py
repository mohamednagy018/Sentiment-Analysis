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

