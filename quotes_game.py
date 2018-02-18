import requests
from bs4 import BeautifulSoup
from csv import DictReader
from random import choice
from time import sleep

all_quotes = []
BASE_URL = "http://quotes.toscrape.com"
url = "/page/1"
with open("write_data.cvs") as file:
	cvs_reader = DictReader(file)
	for quote in cvs_reader:
		all_quotes.append(quote)

def play_game(all_quotes):
	pick_quote = choice(all_quotes)
	remaining_guess = 4
	print(pick_quote["text"])
	print(pick_quote["author"])
	print(f"Guess who said that({remaining_guess} times remaining): ")
	guess = ''
	while guess.lower() != pick_quote['author'].lower() and remaining_guess != 0:
		guess = input()
		remaining_guess -= 1
		if guess.lower() == pick_quote["author"].lower():
			print("You are correct!")
			break
		print(f"Sorry you are wrong. Guess who said that({remaining_guess} times remaining):")
		if remaining_guess == 3:
			res = requests.get(f"{BASE_URL}{pick_quote['about']}")
			soup = BeautifulSoup(res.text,"html.parser")
			date = soup.find(class_="author-born-date").get_text()
			location = soup.find(class_="author-born-location").get_text()
			print(f"Here is a hint: the author born on {date} {location}")
		elif remaining_guess == 2:
			first_name = pick_quote["author"][0]
			print(f"The author's first name starts with {first_name}")
		elif remaining_guess == 1:
			last_name = pick_quote["author"].split(" ")[1][0]
			print(f"The author's last name starts with {last_name}")
		else:
			print(f"Sorry, you are lose. The answer is {pick_quote['author']}.")
	answer = ''
	while answer.lower() not in ['y','yes','no','n']:
		print("Want to play again?")
		answer = input()
		if answer.lower() in ['y', 'yes']:
			return play_game(all_quotes)
		elif answer.lower() in ['n', 'no']:
			print("Thank you for playing")

play_game(all_quotes)	

