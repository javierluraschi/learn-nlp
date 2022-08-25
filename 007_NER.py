import nltk

text = 'My name is Carolina Perez. I live in Alaska'
#text = 'The dog Firulais barked at the cat.'

#Ngrams
tokens = nltk.word_tokenize(text)
print(tokens)

#Name Entity Recognition
tags = nltk.pos_tag(tokens)
text_ch = nltk.ne_chunk(tags, binary=True)

print(text_ch)