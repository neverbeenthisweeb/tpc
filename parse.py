from bs4 import BeautifulSoup
import re
import html5lib
import requests



# def apply_filter(keywords):

def get_url(URL):
	request = requests.get(URL)
	return request

def get_soup(request, parser):
	soup = BeautifulSoup(request.content, parser)
	return soup

def get_keywords():
	keywords = input('Keywords: ')
	return keywords

def welcome_screen():
	text = """
 /$$$$$$$$ /$$$$$$$  /$$    /$$ /$$       /$$   /$$
|__  $$__/| $$__  $$| $$   | $$| $$      | $$  /$$/
   | $$   | $$  \ $$| $$   | $$| $$      | $$ /$$/ 
   | $$   | $$$$$$$/|  $$ / $$/| $$      | $$$$$/  
   | $$   | $$__  $$ \  $$ $$/ | $$      | $$  $$  
   | $$   | $$  \ $$  \  $$$/  | $$      | $$\  $$ 
   | $$   | $$  | $$   \  $/   | $$$$$$$$| $$ \  $$
   |__/   |__/  |__/    \_/    |________/|__/  \__/
                                                       
	"""
	return text


print(welcome_screen())
promo_count = 0
URL = get_url(URL="https://www.traveloka.com/en-id/promotion")
soup = get_soup(request=URL, parser="html5lib")
filter_ = get_keywords()

for info in soup.find_all("div", class_="promo-thumb-info"):
	description = info.find(class_="promo-thumb-desc").get_text() 
	m = re.search("(?i){}".format(filter_), description)
	if m:
		promo_count += 1
		print(description)
		print(info.find(class_="promo-thumb-duration").findChild().get_text())
		print("================")

print(promo_count, 'promo found!')
