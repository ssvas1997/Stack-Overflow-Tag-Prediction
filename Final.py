import time, re, json, numpy as np, sys, csv
from sklearn.svm import LinearSVC
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from nltk.stem.snowball import SnowballStemmer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd

#fh=open('Tags.txt','rt',encoding="utf-8")
#fh2=open('cleaned.txt','rt',encoding="utf-8")
#_i=[]
#_t=[]
#_T=[]
#_b=[]

s=set(stopwords.words('english'))
stemmer = SnowballStemmer('english', ignore_stopwords=True)
count=0
#tagrows=fh.read().split('\n')[:248000]
#checktags=[]
#X=fh2.read().split('\n')[:248000]
classifier = joblib.load('clf.txt')
multibin = joblib.load('multibin.txt')
vectorizer_2=CountVectorizer()

def predictTags():
    T=[]
    #words = str(self.lineEdit.text())+' '+str(self.plainTextEdit.toPlainText())
    words=input("Enter question:")
    words = re.sub('\n',' ',words)
    words = re.sub('[!@%^&*()$:"?<>=~,;`{}|]',' ',words)
    words = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?]))''',' ',words)
    words = re.sub('_','-',words)
    words = words.replace('[',' ')
    words = words.replace(']',' ')
    words = words.replace('/',' ')
    words = words.replace('\\',' ')
    words = re.sub(r'(\s)\-+(\s)',r'\1', words)
    words = re.sub(r'\.+(\s)',r'\1', words)
    words = re.sub(r'\.+\.(\w)',r'\1', words)
    words = re.sub(r'(\s)\.+(\s)',r'\1', words)
    words = re.sub("'",'', words)
    words = re.sub(r'\s\d+[\.\-\+]+\d+|\s[\.\-\+]+\d+|\s+\d+\s+|\s\d+[\+\-]+',' ',words)
    words = re.sub("^\d+\s|\s\d+\s|\s\d+$"," ", words)
    words = re.sub(r'\s\#+\s|\s\++\s',' ',words)
    stemmed_words = [stemmer.stem(word) for word in words.split()]
    clean_text = filter(lambda w: not w in s,stemmed_words)
    words=''
    for word in clean_text:
            words+=word+' '
    T.append(words)
    print("T",T)
    results=classifier.predict(T)
    results=multibin.inverse_transform(results)
    #print '\n',results,'\n'
    buff=''
    tagarr=[]
    for result in results[0]:
            #buff=buff+QString(result)+' ; '
            tagarr.append(result)
    #self.lineEdit_2.setText(buff[:len(buff)-3])
    #recommend()
    print(tagarr)

predictTags()
