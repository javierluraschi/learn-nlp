# -*- coding: utf-8 -*-

import urllib.request

libro_url = "https://www.gutenberg.org/cache/epub/54430/pg54430.txt"

# descargar libro
urllib.request.urlretrieve(libro_url, "libro.txt")
