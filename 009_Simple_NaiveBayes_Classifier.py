import nltk
import random
import matplotlib 
matplotlib.style.use("ggplot")
#nltk.download("name")

from nltk.corpus import names

#names?
names.fileids()

#Crear listas de nombres
lista_masculinos = [(name, "male") for name in names.words("male.txt")] 
lista_femeninos = [(name, "female") for name in names.words("female.txt")]
lista = lista_masculinos + lista_femeninos

#Ver nombres
lista[:10]
lista[-10:]

#Distribucion de Frecuencia condicional de las combinaciones de las 2 ultimas 
#letras en los nombres
nombres_dfc = nltk.ConditionalFreqDist((fileid, nombre[-2:]) 
                                       for fileid in names.fileids() 
                                       for nombre in names.words(fileid))

nombres_dfc.plot()

#Funcion para obtener las 2 ultimas letras de los nombres
def nombre_final(nombre):
    return {"par final": nombre[-2:]}

nombre_final("Katy")

#'Desorganizar' aleatoriamente la lista
random.shuffle(lista)

lista[:10]

#Obtener combinaciones del final del nombre con el genero al que corresponde
finales = [ (nombre_final(name), gender) for (name, gender) in lista]
finales[:10]

len(finales)

#Conjuntos para el modelo
training_set = finales[:2500]
testing_set = finales[2500:]

#Entrenar el clasificador
clasificador = nltk.NaiveBayesClassifier.train(training_set)

#Precision
nltk.classify.accuracy(clasificador, testing_set)

#Ejemplos
"Julieta" in lista_femeninos
"Juliette" in lista_femeninos
clasificador.classify(nombre_final("Julieta"))
clasificador.classify(nombre_final("Juliette"))

"Romeo" in lista_masculinos
clasificador.classify(nombre_final("Romeo"))


"Zoey" in lista_femeninos
clasificador.classify(nombre_final("Zoey"))

"Joey" in lista_masculinos
clasificador.classify(nombre_final("Joey"))

clasificador.classify(nombre_final("Yusnavy"))

