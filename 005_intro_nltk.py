import nltk
import re

#Tokenizar(??)
texto = 'Hola!. Cual es tu nombre? Tu nombre es poco comun.'
palabras = nltk.word_tokenize(texto)
print(palabras)
print(len(palabras))

oraciones = nltk.sent_tokenize(texto)
print(oraciones)
print(len(oraciones))

#Distancias de Levenshtein para transformar s1 en s2
nltk.edit_distance('cangrejo', 'canguro')


#Textos del proyecto de gutenberg que trae nltk
nltk.corpus.gutenberg.fileids()

#Trabajaremos con el de Alicia en el Pais de las Maravillas.
carroll = nltk.corpus.gutenberg.words("carroll-alice.txt")
carroll_sent = nltk.corpus.gutenberg.sents("carroll-alice.txt")

print(carroll)
print(carroll[:100])

#Cuantas repeticiones hay de cada palabra
print(carroll.count('Alice'))
print(carroll.count('escuela'))

#Conjunto de palabras unicas 
carroll_set = set(carroll)

#Cantidad de repeticiones por palabras aprox
len(carroll)/len(carroll_set)

#Cantidad de palabras por oraciones
len(carroll)/len(carroll_sent)

#Buscar palabras que terminan en 'ing'
l = []
for word in carroll:
    if re.search("ing$", word):
        l.append(word)
print(l)

l1 = set(l)

set([word for word in carroll if re.search("ing$", word)])

 
#Buscar palabras que comienzan por 'fr'
set([word for word in carroll if re.search("^fr", word)])

#Buscar numeros
set([word for word in carroll if re.search("\d+", word)])

#Distribucion de frecuencias
carroll_fd = nltk.FreqDist(carroll)
print(carroll_fd['Cat'])
            
carroll_100 = carroll_fd.most_common(100)
print(carroll_100)

common_100 = [word[0] for word in carroll_100]
common_100

#Problemas por resolver
#1-
print(carroll_fd['Cat'])
#diferente a 
print(carroll_fd['cat'])
#y para nosotros significaria lo mismo

#2- 
#Las palabras mas comunes no son para nada informativas
common_100
