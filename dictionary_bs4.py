import requests
from bs4 import BeautifulSoup

def find_meaning(word):
	url="http://www.collinsdictionary.com/dictionary/english/"+word
	r=requests.get(url)
	soup = BeautifulSoup(r.content)


	mean= soup.find_all("div",{"class":"sense"})

	for item in mean:
		try:
			print (item.contents[0].text) 
			print (item.contents[1].text)
			print (item.contents[2].text)
			print (item.contents[3].text)
		except:
			pass

word=input('Enter the word whose meaning you want to find : ')
find_meaning(word)
