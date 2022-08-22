import nltk
from nltk.util import ngrams

text = 'My name is Carolina Perez. I really want to eat chocolate now. I like to swim. I live in Alaska'

#Ngrams
tokens = nltk.word_tokenize(text) #Tokenizar el texto
print(tokens)

bigrams = nltk.bigrams(tokens)
for item in bigrams:
    print(item)

#trigrams
trigrams = nltk.trigrams(tokens)
for item in trigrams:
    print(item)
     

#ngrams, generales ngrams(tokens, 5)     
five_grams = ngrams(tokens, 5)
for item in five_grams:
    print(item)

    
#Tagging
tags = nltk.pos_tag(tokens, tagset = "universal")
tags

#Imprimir los sustantivos
for word in tags:
    if word[1]=='NOUN':
        print(word)

#Imprimir verbo + To + Verbo
#for x in nltk.bigrams([word[0] for word in tags if word[1] == 'VERB']):
#    print(x[0], 'To', x[1])
    
for ((word1, tag1), (word2, tag2), (word3, tag3)) in nltk.trigrams(tags):
    if tag1 == "VERB" and word2 == "to" and tag3 == "VERB":
        print(word1, word2, word3)
    


#Name Entity Recognition
tags = nltk.pos_tag(tokens)
text_ch = nltk.ne_chunk(tags, binary=True)

for chunk in text_ch:
    if hasattr(chunk, 'label'):
        #leaves (estructura)
        #print(chunk.label())
        #print(chunk.leaves())
        print(chunk.label(), " ".join(c[0] for c in chunk.leaves()))
