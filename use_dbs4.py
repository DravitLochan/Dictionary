from dictionary_bs4 import find_meaning
import json

f = open("string_loop.txt")
with open("wm.json", "a") as mf:
	mf.write("[")
	words_json = json.loads(f.read())
	words = words_json.keys()
	data = []
	i = 1
	for word in words:
		if i == 6:
			break
		dict = {}	
		a = word.encode('ascii', 'ignore')	
		dict['word'] = a
		b = find_meaning(a)
		if b == None:
			continue;
		else:
			dict['meaning'] = b.encode('ascii', 'ignore')	
		mf.write(json.dumps(dict))
		mf.write(", ")
		i = i+1
	mf.write("]")	