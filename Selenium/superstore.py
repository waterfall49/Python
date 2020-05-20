from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.atlanticsuperstore.ca/search?search-bar='
plusUrl = input('What do you want to search? : ')
url = baseUrl + plusUrl
print(url)