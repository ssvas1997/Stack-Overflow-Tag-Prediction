from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import MultiLabelBinarizer
tags={}
freq=[]
count=0
fh=open('Tags.txt','rt',encoding="utf-8")
fh2=open('cleaned.txt','rt',encoding="utf-8")
tagrows=fh.read().split('\n')[:248000]
# X-> cleaned data without stopwords i.e question
X=fh2.read().split('\n')[:248000]
# Y-> most repeated tag for that question
Y = [[] for i in range(len(X))]
classifier = Pipeline([
		     ('vectorizer', CountVectorizer()),
		     ('tfidf', TfidfTransformer()),
		     ('clf', OneVsRestClassifier(LinearSVC(), n_jobs = -2))])

#One tag has repeated how many times stored in dictionary
for line in tagrows:
	for tag in line.split():
		if tag in tags:
			tags[tag]+=1
		else:
			tags[tag]=1
	count=0
#sorted the dictionary in reverse order of value
#most repeated tags will come first
for tag in sorted(tags,key=lambda tag:tags[tag], reverse=True):
	if tags[tag] > 4000:
		count += 1
		freq.append(tag)
	else:
		break
	
print("Training...")

#after getting the freq we will map question from X to that of freq as tagrows contains multiple tags for the same question
#we will map the highest freq tag to the question 
#X-> check upload file imag without mime type bis way check upload file imag apart check file extens use php
#Y-> php
for x,tag in enumerate(freq):
	i=0
	for row in tagrows:
		if tag in row.split():
			Y[i].append(tag)
		i=i+1

print("Tagrows:",tagrows[:50])
#print("Tags Dict:",tags[:50])
print("Frequency:",freq[:50])
print("X:",X[:50])
print("Y",Y[:50])
multibin=MultiLabelBinarizer()
Y=multibin.fit_transform(Y)
classifier.fit(X,Y)
job = joblib.dump(classifier, 'clf.txt', compress=9)
job = joblib.dump(multibin, 'multibin.txt', compress=9)
