from bs4 import BeautifulSoup
import re
import html5lib
import requests


URL = 'https://www.traveloka.com/en-id/promotion'
r = requests.get(URL)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
