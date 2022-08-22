import nltk

alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
    
alice = [w.lower() for w in alice]
   
alice[:100]

#Distribucion de frecuencia
alice_fd = nltk.FreqDist(alice)

#100 mas comunes
alice_100 = alice_fd.most_common(100)
alice_100

#Solo seleccionar caracteres alfanumericos con palabra.isalpha()
alice_mod = [x[0] for x in alice_100 if x[0].isalpha()]
alice_mod

#alice_norm = [word.lower() for word in alice if word.isalpha()]


#Palabras de ingles comunes 'stop_words'
stop_words = nltk.corpus.stopwords.words("english")

info_words_alice = set(alice_mod) - set(stop_words)

#moby = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
#moby_norm = [word.lower() for word in moby if word.isalpha()]
#moby_norm_fd = nltk.FreqDist(moby_norm)
#moby_norm_100 = moby_norm_fd.most_common(100)
#moby_common = [word[0] for word in moby_norm_100]

#info_words_moby = set(moby_common) - set(stop_words) 

#info = set(info_words_alice) - set(info_words_moby)


