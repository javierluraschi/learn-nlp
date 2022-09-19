
import gensim
from gensim.models import Word2Vec

# train simple model

model1 = gensim.models.Word2Vec([ 'a', 'mi', 'me', 'gusta', 'esta', 'clase' ], min_count = 1, vector_size = 2, window = 2)

# download word2vec

import gensim.downloader as api

# beware this is a 1.5GB download
wv = api.load('word2vec-google-news-300')

wv.similarity('alice', 'wonderland')

# fos spanish consider using
# https://github.com/aitoralmeida/spanish_word2vec

wv.similarity('alice', 'wonderland')
#0.3020006

wv.similarity('france', 'berlin')
# 0.45780045

wv.similarity('france', 'apple')
# 0.124436855

# do some vector operations on word space

v.similar_by_vector(wv.get_vector('france', norm=True) - wv.get_vector('paris', norm=True) + wv.get_vector('berlin', norm=True))
#[('berlin', 0.7039149403572083), ('france', 0.6814685463905334), ('germany', 0.5094344019889832), ('european', 0.4865044951438904), ('german', 0.4714890122413635), ('austria', 0.46964019536972046), ('swedish', 0.464518278837204), ('Wissenschaft', 0.4532880485057831), ('denmark', 0.4477354884147644), ('München', 0.4438532590866089)]

wv.similar_by_vector(wv.get_vector('hamburger', norm=True) - wv.get_vector('usa', norm=True) + wv.get_vector('mexico', norm=True))
# [('hamburger', 0.7995819449424744), ('burger', 0.6117082238197327), ('hamburgers', 0.5973707437515259), ('taco', 0.5853015780448914), ('burgers', 0.5690708160400391), ('cheeseburger', 0.5570955872535706), ('burrito', 0.5422651171684265), ('bologna_sandwich', 0.523348331451416), ('steak', 0.509742021560669), ('sandwich', 0.5096349120140076)]