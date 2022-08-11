import urllib.request
from os.path import exists

book_url = "https://www.gutenberg.org/cache/epub/54430/pg54430.txt"
book_file = "libro.txt"

if not exists(book_file):
    urllib.request.urlretrieve(book_url, book_file)

with open(book_file, encoding = 'utf-8') as f:
    book = f.read()

stop_words = ".,:-¿?¡!;/$"

words = []
current = ''

for char in book:
    if char >= 'a' and char <= 'z':
        current = current + char
    else:
        if len(current) > 0:
            words.append(current)
        current = ''
   

print(words)
