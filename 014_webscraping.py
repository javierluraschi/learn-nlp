# pip install lxml

import requests
from lxml import html
import pandas as pd

books = 'https://www.gutenberg.org/ebooks/results/?author=&title=&subject=&lang=es&category=&locc=&filetype=rdf&submit_search=Search&pageno=1'
contents = requests.get(books).text

tree = html.fromstring(contents)

authors = tree.xpath('//table[1]//td[3]//li[1]//text()')
titles = tree.xpath('//table[1]//td[4]//text()')
links = tree.xpath('//table[1]//td[4]//a[1]//@href')

pd.DataFrame().assign(authors = authors, titles = titles, links = links)