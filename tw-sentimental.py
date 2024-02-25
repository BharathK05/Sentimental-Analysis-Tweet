from transformers import AutoTokenizer,AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np
import subprocess

#python_output = subprocess.run(['python', 'tw-sentimental.py', user_input], capture_output=True).stdout.decode()

#Input of dataset
tweet = "@Bharath K Today is good day"

#Preprocessing Data
tweet_word=[]
for word in tweet.split(" "):
    if word.startswith('@') and len(word)>1:
        word="@user"
    elif word.startswith('http'):
        word="http"
    tweet_word.append(word)

tweet_proc=''.join(tweet_word) #The Cleaned Data is stored Here

#Loading the Model
roberta= "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative','Nuetral','Positive']

#Main-Sentimental Analysis
encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')


#Output after passing it to the Model
#output=model(encoded_tweet['input_ids'],encoded_tweet['attention_mask'])
output=model(**encoded_tweet)
prob=output[0][0].detach().numpy()
prob=softmax(prob)

#Printing the predicted result
a=[]
for i in range(len(prob)):
    s=prob[i]
    a.append(np.round(float(s), 4))

c=max(a)
d=a.index(c)
e=labels[d]
print("It is a",e,"Comment, With a Probabilty of",c,"%")
