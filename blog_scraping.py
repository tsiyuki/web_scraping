import requests
from bs4 import BeautifulSoup
from csv import writer
# http://www.rithmschool.com/blog
url = 'http://www.rithmschool.com/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
articles = soup.find_all('article')
with open('blog_data.csv','w') as file:
	csv_writer = writer(file)
	csv_writer.writerow(['Title', 'URL', 'Datetime'])
	for article in articles:
		tag = article.find('a')
		header = tag.get_text()
		URL = tag['href']
		time = article.find('time')['datetime']
		csv_writer.writerow([header,URL,time])


