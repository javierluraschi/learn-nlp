// pip install lxml

import requests
from lxml import html

books = 'https://www.gutenberg.org/ebooks/results/?author=&title=&subject=&lang=es&category=&locc=&filetype=rdf&submit_search=Search&pageno=1'
contents = requests.get(books).text

