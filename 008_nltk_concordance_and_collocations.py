from nltk.book import text8
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.text import Text

#######Concordancia
text8.concordance("love")
text8.concordance("man")
text8.concordance("women")
#text8.concordance("beach")
#text8.concordance("attractive")
#text8.concordance("sexy")
#text8.concordance("intelligent", width=150)

#Grafico de dispersion
text8.dispersion_plot(["woman", "lady", "girl", "female"])

#Distribucion de frecuencia
frequency_distribution = FreqDist(text8)
print(frequency_distribution)

#eliminar stop words y no alfanumericos
stop_words = set(stopwords.words("english"))
words = [word.casefold() for word in text8 if word.casefold() not in stop_words and word.isalpha() == True]

#Distribucion de frecuencia de nuevo
frequency_distribution = FreqDist(words)
frequency_distribution.most_common(20)

#Grafico
frequency_distribution.plot(20, cumulative=False)

######Collocations
col = text8.collocations()

#Lemmatize
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
new_text = Text(lemmatized_words)

new_text.collocations()