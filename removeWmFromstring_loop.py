import json

wm = open("wm.json", 'r')
sl = open("string_loop.txt", "r")
sln = open("new_string_loop.txt", "w")

json_sl = json.loads(sl.read())
json_wm = json.loads(wm.read())
new_json = {}

for word in json_wm:
	new_json[str(word)] = 1

data = []

for word in json_sl.keys():
	dict = {}
	if word in new_json.keys():
		continue
	else:
		dict[str(word)] = 1
		data.append(dict)
sln.write(str(data))		