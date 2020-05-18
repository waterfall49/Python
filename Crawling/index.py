#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.naver.com') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('span.keyword'):
        print(anchor)

