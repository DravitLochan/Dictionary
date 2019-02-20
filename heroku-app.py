import requests
import json

url = "https://dictionaryapi.herokuapp.com/"
f = open("string_loop.txt")
w = open("wm.json", "w")
words_json = json.loads(f.read())
words = words_json.keys()
meaning = []
print(len(words))
for word in words:
	word = word.encode('ascii', 'ignore')
	if len(word) < 3:
		continue
	p = {'define':word}
	print word
	try:
		response = requests.get(url = url, params = p)
		json_response = response.json()
		meaning[0] = json_response[0]['meaning']['noun'][0]['definition']
		memaing[1] = json_response[0]['meaning']['verb'][0]['definition']
		meaing[2] = json_response[0]['meaning']['adjective'][0]['definition']
		meaning[3] = json_response[0]['meaning']['adverb'][0]['definition']
		# print(json_response_noun)
		# print(json_response_verb)
		# print(json_response_adverb)
		# print(json_response_adj)
		print (meaning)	
	except:
		a = 1