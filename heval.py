from os import listdir
from random import shuffle
from csv import writer

ms = sorted(listdir('./dec/MatchSum/'), key=lambda f : int(f.split(".")[0]))
pn = sorted(listdir('./dec/PNBERT/'), key=lambda f : int(f.split(".")[0]))
pg = sorted(listdir('./dec/PGen/'), key=lambda f : int(f.split(".")[0]))
ls = sorted(listdir('./dec/LoopSum/'), key=lambda f : int(f.split(".")[0]))
rf = sorted(listdir('./ref/'), key=lambda f : int(f.split(".")[0]))
inputs = sorted(listdir('./in/'), key=lambda f : int(f.split(".")[0]))

msscore = [[], []]
pnscore = [[], []]
pgscore = [[], []]
lsscore = [[], []]

scores = [msscore, pnscore, pgscore, lsscore]

for i in range(50):

	shufe = [j for j in range(2)]
	shufa = [j for j in range(2,4)]
	shuffle(shufe)
	shuffle(shufa)

	data = [[] for i in range(4)]

	indata = []
	rfdata = []


	with open('./dec/MatchSum/' + ms[i], "r") as _file:
		data[0] = _file.readlines()
	with open('./dec/PNBERT/' + pn[i], "r") as _file:
		data[1] = _file.readlines()
	with open('./dec/PGen/' + pg[i], "r") as _file:
		data[2] = _file.readlines()
	with open('./dec/LoopSum/' + ls[i], "r") as _file:
		data[3] = _file.readlines()
	with open('./ref/' + rf[i], "r") as _file:
		rfdata = _file.readlines()
	with open('./in/' + inputs[i], "r") as _file:
		indata = _file.readlines()

	print('\n')

	print("Original article:")

	for line in indata:
		print(line, end="")

	print('\n')

	print("Reference summary:")

	for line in rfdata:
		print(line, end="")

	print('\n')

	for name,shuf in [("Extractive", shufe), ("Abstractive", shufa)]:
		for num, j in enumerate(shuf):

			print(name + " summary " + str(num) + ":")

			for line in data[j]:
				print(line, end="")
			print('\n')

		for num, j in enumerate(shuf):
			r=-1
			while (type(r)!=float or r >5 or r <0):
				try:
					r = float(input("Rate the RELEVANCE for " + name.lower() + " summary " + str(num) +" on a scale from 1 and 5:"))
				except ValueError:
					continue
			scores[j][0].append(r)

			print('\n')

			c=-1
			while (type(c)!=float or c >5 or c <0):
				try:
					c = float(input("Rate the COHERENCE for " + name.lower() + " summary " + str(num) +" on a scale from 1 and 5:"))
				except ValueError:
					continue
			scores[j][1].append(c)

			print('\n')

	rrow = [scores[j][0][i] for j in range(4)]
	crow = [scores[j][1][i] for j in range(4)]

	with open('./rout.csv', 'a', newline='') as f:
		w = writer(f)
		w.writerow(rrow)

	with open('./cout.csv', 'a', newline='') as f:
		w = writer(f)
		w.writerow(crow)
