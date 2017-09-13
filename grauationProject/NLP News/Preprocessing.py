from nltk.tokenize import word_tokenize
from nltk.stem import ISRIStemmer

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


