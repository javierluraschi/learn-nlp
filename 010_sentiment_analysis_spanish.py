# Based of https://towardsdatascience.com/sentiment-analysis-comparing-3-common-approaches-naive-bayes-lstm-and-vader-ab561f834f89
# Based of https://stackoverflow.com/questions/41337363/spanish-word-tokeniser

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize.toktok import ToktokTokenizer
import nltk

import pandas as pd

df=pd.read_csv('010_books_authors.csv', delimiter='|')

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Reconstruct text from "esto son unos libros" to "esto es in libro"
def data_cleaning(text_list): 
    stopwords_rem=False
    stopwords_sp=stopwords.words('spanish')
    tokenizer=ToktokTokenizer()
    reconstructed_list=[]
    for each_text in text_list:
        relevant_tokens=[]
        tokenized_tokens=tokenizer.tokenize(each_text)
        for each_token in tokenized_tokens:
            if each_token not in stopwords_sp: 
                relevant_tokens.append(each_token)
        reconstructed_list.append(' '.join(tokenized_tokens))
    return reconstructed_list
  
estimators=[('cleaner', FunctionTransformer(data_cleaning)), ('vectorizer', TfidfVectorizer(max_features=100000, ngram_range=(1, 2)))]
preprocessing_pipeline=Pipeline(estimators)

# Break data down into a training set and a testing set
X=df['text']
y=df['label']
X_train, X_test, y_train, y_test=train_test_split(X, y)

# Fit and transform the pipeline
X_train_transformed=preprocessing_pipeline.fit_transform(X_train)

# Create a Naive Bayes model and fit training data
nb=MultinomialNB()
nb.fit(X_train_transformed, y_train)
X_test_transformed=preprocessing_pipeline.transform(X_test)

# Evaluate model
print(f'Test Score: {nb.score(X_test_transformed, y_test)}')
print(f'Test Score: {nb.score(X_train_transformed, y_train)}')
