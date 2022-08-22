import nltk

my_list = ["cat", "cats", "lie", "lying", "run", "running", "city", "cities", 
           "month", "monthly", "woman", "women", "scarf", "scarves"]
mi_lista = ["gato", "gatos", "mentira", "mentir", "mintiendo", "ciudad", 
            "ciudades", "comer", "comida"]

#Stemming - Derivacion?

porter =  nltk.PorterStemmer()  #1979

snowball = nltk.SnowballStemmer('english')
snowball_sp = nltk.SnowballStemmer('spanish')

lancaster = nltk.LancasterStemmer()

for word in my_list:
    print(word)
    print("Porter Stemmer: " + porter.stem(word))
    print("Snowball: " + snowball.stem(word))
    print("Lancaster Stemmer: " + lancaster.stem(word))    
    
for word in mi_lista:
    print(word)
    print("Porter Stemmer: " + porter.stem(word))
    print("Snowball: " + snowball_sp.stem(word))
    print("Lancaster Stemmer: " + lancaster.stem(word))    
    
   
#Lemmatizing - Lematizacion?

lemmatizer = nltk.WordNetLemmatizer()


#Lematizar la lista e imrpimir resultados
for word in my_list:
    print(word)
    print("Lemmatize: " + lemmatizer.lemmatize(word))

    
final_list = []
for word in my_list:
    w = snowball.stem(lemmatizer.lemmatize(word))
    final_list.append(w)
final_list

#Tarea - Ver ejemplos de Chunking and Chinking (??? que nombre mas rarito). 
