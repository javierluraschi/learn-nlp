# Based of https://towardsdatascience.com/sentiment-analysis-comparing-3-common-approaches-naive-bayes-lstm-and-vader-ab561f834f89

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import nltk

import pandas as pd

df=pd.read_csv('010_books_authors.csv', delimiter='|')

nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Create a and run a data processing Pipeline
def data_cleaning(text_list): 
    stopwords_rem=False
    stopwords_en=stopwords.words('english')
    lemmatizer=WordNetLemmatizer()
    tokenizer=TweetTokenizer()
    reconstructed_list=[]
    for each_text in text_list: 
        lemmatized_tokens=[]
        tokens=tokenizer.tokenize(each_text.lower())
        pos_tags=pos_tag(tokens)
        for each_token, tag in pos_tags: 
            if tag.startswith('NN'): 
                pos='n'
            elif tag.startswith('VB'): 
                pos='v'
            else: 
                pos='a'
            lemmatized_token=lemmatizer.lemmatize(each_token, pos)
            if stopwords_rem: # False 
                if lemmatized_token not in stopwords_en: 
                    lemmatized_tokens.append(lemmatized_token)
            else: 
                lemmatized_tokens.append(lemmatized_token)
        reconstructed_list.append(' '.join(lemmatized_tokens))
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
