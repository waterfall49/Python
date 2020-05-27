from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

baseUrl = 'https://www.atlanticsuperstore.ca/search?search-bar='
plusUrl = input('What do you want to search? : ')
url = baseUrl + plusUrl
webpage_res = requests.get(url)
webpage = webpage_res.content

# driver = webdriver.Chrome()
# driver.get(url)

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(webpage, 'html.parser')
print(soup)

# r = soup.select('.product-tile.product-tile--add-to-list-button.product-tile--marketplace')
r = soup.select('product-name__item')
print(r)
# for i in r:
#     print(i.select_one('product-name__item.product-name__item--name').text)

