from bs4 import BeautifulSoup
import re
import html5lib
import requests


filter_ = input('Keywords? (if NO then just press ENTER): ')
# print(filter_)
promo_found = 0
URL = "https://www.traveloka.com/en-id/promotion"
r = requests.get(URL)

soup = BeautifulSoup(r.content, "html5lib")

for info in soup.find_all("div", class_="promo-thumb-info"):
	description = info.find(class_="promo-thumb-desc").get_text() 
	m = re.search("(?i){}".format(filter_), description)
	if m:
		promo_found += 1
		print(description)
		print(info.find(class_="promo-thumb-duration").findChild().get_text())
		print("================")

print(promo_found, 'promo found!')
