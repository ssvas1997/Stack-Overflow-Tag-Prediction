[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/) 
## Stack Overflow Question Tag Prediction 
- Predict tags of StackOverflow posts using OneVsRestClassifier.
--------------------------------------------------------------------
<div align="center">
 &#10077; Want to make search even more faster ? Tags are the solution you are likely to look for. &#10078;
 </div>

 

### Technology Stack
- Backend Framework - [Flask](https://palletsprojects.com/p/flask/)
- Frontend Framework - [React Native](https://facebook.github.io/react-native/)

### Deployment Instructions
- Install all the packages as specified in the 
[Requirements File](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/requirements.txt "requirements.txt") 

- Download the [Dataset](https://www.kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data)

- Execute the [StackOverflow CSV Preprocessing.py](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/StackOverflow_CSV_Preprocessing.py "stackoverflow preprocess") to clean the posts i.e removing the stopwords

- This would generate 3 files:
  * [Tags](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/Tags.txt) which contains tags
  * [Cleaned](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/cleaned.txt) which contains questions after removing stopwords
  * [Errors](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/error_log.txt) which contains error logs if any

- Execute the [savejob.py](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/savejob.py) to train the model
- This would generate 2 files i.e Trained Model:
  * [Classifier](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/clf.txt)
  * [Multilabel Binarizer](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/multibin.txt)

- Execute the [server.py](https://github.com/ssvas1997/Stack-Overflow-Tag-Prediction/blob/master/server.py) to run the model on the flask server

- Open the [Link](http://127.0.0.1:5000/?q=%22connection%20failed%20between%20mysql%20and%20tkinter%22) in your web browser. This would return a json:
  - `{
  "tags": [
    "mysql", 
    "python"
  ]
}` 

### Reference Repositories
- [Frontend Repository](https://github.com/joshiadvait8/overCode)
- [Backend API Repository](https://github.com/ssvas1997/overcode-Tag-Prediction-Backend)


### Contributors
- [@ssvas1997](https://github.com/ssvas1997)
- [@joshiadvait8](https://github.com/joshiadvait8)
