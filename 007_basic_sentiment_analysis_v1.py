import csv

negative = []
with open("words_negative.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        negative.append(row[0])   
        
positive = []
with open("words_positive.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        positive.append(row[0])   

positive[:10]

negative[:10]

text = 'not like like'
texto = 'not bad, absolutely good'

def sentiment(text):
#    temp = []
#    text_sent = text.split('.')
#    print('ciclo')
    n_counts = 0
    p_counts = 0
    word = text.split()
    for words in word:
        print(words)
        if (words in negative):
            if word[word.index(words) + 1] in positive:
                n_counts += 2
            elif word[word.index(words) + 1] in negative:
                p_counts += 1
        elif words in positive:
            p_counts += 1
    return(n_counts, p_counts)

sentiment(text)
sentiment(texto)
