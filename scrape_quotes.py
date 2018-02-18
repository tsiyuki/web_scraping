import requests
from bs4 import BeautifulSoup
from csv import DictWriter
from random import choice
from time import sleep

BASE_URL = "http://quotes.toscrape.com"
url = "/page/1"
all_quotes = []
while url:
	res = requests.get(f"{BASE_URL}{url}")
	print(f"Now Scraping {BASE_URL}{url}...")
	soup = BeautifulSoup(res.text,"html.parser")
	quotes = soup.find_all(class_="quote")
	for quote in quotes:
		all_quotes.append({
			"text":quote.find(class_="text").get_text(),
			"author":quote.find(class_="author").get_text(),
			"about":quote.find("a")['href']
			})
	next = soup.find(class_="next")
	url = next.find("a")['href'] if next else None

with open("write_data.cvs","w") as file:
	header = ["text","author","about"]
	cvs_writer = DictWriter(file, fieldnames=header )
	cvs_writer.writeheader()
	for quote in all_quotes:
		cvs_writer.writerow(quote)







