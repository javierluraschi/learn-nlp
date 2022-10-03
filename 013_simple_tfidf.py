
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = "a mi me gusta esta clase"
documentB = "a mi no me gusta esta clase"

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform([documentA, documentB])

feature_names = vectorizer.get_feature_names_out()

dense = vectors.todense()

denselist = dense.tolist()

df = pd.DataFrame(denselist, columns=feature_names)
