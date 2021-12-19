from os import listdir
import json

pn = listdir('./test/')
msdata = {}

with open('./test.jsonl', "r") as _file:
	msdata = json.load(_file)

for i in range(len(msdata)):
	data = [j + '\n' for j in msdata[i]['text']]
	with open('./in/' + str(i) + '.in', "w") as _file:
		_file.writelines(data)

for i in range(len(msdata)):
	data = [j + '\n' for j in msdata[i]['summary']]
	with open('./ref/' + str(i) + '.ref', "w") as _file:
		_file.writelines(data)
