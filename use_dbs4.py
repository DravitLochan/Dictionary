from dictionary_bs4 import find_meaning
import json

f = open("string_loop.txt")
with open("wm.json", "a") as mf:
	mf.write("[")
	words_json = json.loads(f.read())
	words = words_json.keys()
	data = []
	for word in words:
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
	mf.write("]")	