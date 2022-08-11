import urllib.request
from os.path import exists
import re

book_url = "https://www.gutenberg.org/cache/epub/54430/pg54430.txt"
book_file = "book.txt"

if not exists(book_file):
    urllib.request.urlretrieve(book_url, book_file)

with open(book_file, encoding = 'utf-8') as f:
    book = f.read()
    
book = re.sub('.*START OF THIS PROJECT.*[*]+', '', book, re.DOTALL)

print(book[0:200])
