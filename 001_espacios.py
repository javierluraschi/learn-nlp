# -*- coding: utf-8 -*-

import urllib.request
from os.path import exists

libro_url = "https://www.gutenberg.org/cache/epub/54430/pg54430.txt"
libro_archivo = "libro.txt"

# descargar libro
if not exists(libro_archivo):
    urllib.request.urlretrieve(libro_url, libro_archivo)

with open(libro_archivo, encoding = 'utf-8') as f:
    libro = f.read()
    
len(libro.split())
