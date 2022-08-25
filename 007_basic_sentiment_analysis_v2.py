import nltk
import csv
import numpy as np

negative = []
with open("words_negative.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        negative.append(row)   

positive = []
with open("words_positive.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        positive.append(row)
        
positive[:10]

negative[:10]

text_p = 'The cake is fantastic. I love it.'
text_1 = 'I did not like the sandwish.'
text_2 = 'The frog is jumping'
text_n = 'I did not watch the movie. It was extreamly boring'
texto = 'not extremly bad'

def sentiment(text):
    temp = []
    text_sent = nltk.sent_tokenize(text)
    for sentence in text_sent:
        n_count = 0
        p_count = 0
        sent_words = nltk.word_tokenize(sentence)
        for word in sent_words:
            for item in positive:
                if(word == item[0]):
                    p_count += 1
            for item in negative:
                if(word == item[0]):
                    n_count += 1
        if(p_count>0 and n_count == 0):
            temp.append(1)
            print("+ : " + sentence)
        elif(n_count%2 > 0):
            temp.append(-1)
            print("- : " + sentence)
        elif(n_count%2 == 0 and n_count > 0):
            temp.append(1)
            print("+ : " + sentence)
        else:
            temp.append(0)
            print("? : " + sentence)
    return(temp)

sentiment(text_p)
sentiment(text_1)
sentiment(text_2)
sentiment(text_n)
sentiment(texto)

print(np.average(sentiment(str(text_n))))