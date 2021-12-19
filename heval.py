from os import listdir

ms = sorted(listdir('./dec/MatchSum/'))
pn = sorted(listdir('./dec/PNBERT/'))
inputs = sorted(listdir('./in/'))

msscore = [0,0]
pnscore = [0,0]

for i in range(len(ms)):
	msdata = []
	pndata = []
	indata = []
	with open('./dec/MatchSum/' + ms[i], "r") as _file:
		msdata = _file.readlines()
	with open('./dec/PNBERT/' + ms[i], "r") as _file:
		pndata = _file.readlines()
	with open('./in/' + inputs[i], "r") as _file:
		indata = _file.readlines()

	y = input("Press any key to view original article.")

	for line in indata:
		print(line, end="")

	print()

	y = input("Press any key to view first summary.")

	print()

	for line in msdata:
		print(line, end="")

	print()

	y = input("Press any key to view second summary.")

	print()

	for line in pndata:
		print(line, end="")

	print()

	r = input("Enter which was more relevant (0 or 1):")
	c = input("Enter which was more coherent (0 or 1):")

	if (r == "0"):
		msscore[0] += 1
	else:
		pnscore[0] += 1

	if (c == "0"):
		msscore[1] += 1
	else:
		pnscore[1] += 1
