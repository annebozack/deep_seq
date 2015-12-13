import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import itertools

path = sys.argv[1]

path1 = ''+path+'spacer_count0.csv'
path2 = ''+path+'spacer_count2.csv'
path3 = ''+path+'spacer_count7.csv'
path4 = ''+path+'spacer_count60.csv'

def getColumn(path, column):
	results = csv.reader(open(path), delimiter=',')
	return [result[column] for result in results]

def getInt(list):
	list1 = []
	i = 0
	while i < len(list):
		if list[i] != '':
			list1.append(list[i])
		i += 1
	list1 = map(int, list1)
	return list1

def getRel(list):
	list1 = []
	listsum = sum(list)
	i = 0
	while i < len(list):
		list1.append(float(list[i])/float(listsum))
		i+=1
	return list1

def makeDict(path):
	reads = getColumn(path, 2)
	reads1 = getInt(reads)
	relreads = getRel(reads1)
	seq = getColumn(path, 4)
	dictionary = dict(zip(seq, relreads))
	return dictionary

def makeLists(path1, path2, path3, path4, filename):
	dict0 = makeDict(path1)
	dict2 = makeDict(path2)
	dict7 = makeDict(path3)
	dict60 = makeDict(path4)
	listkeys = list(dict0.keys())
	list0 = []
	list2 = []
	list7 = []
	list60 = []
	i = 0
	while i < len(listkeys):
		if listkeys[i] in dict2:
			list2.append(listkeys[i])
		i+=1
	i = 0
	while i < len(listkeys):
		if listkeys[i] in dict7:
			list7.append(listkeys[i])
		i+=1
	i = 0
	while i < len(listkeys):
		if listkeys[i] in dict60:
			list60.append(listkeys[i])
		i+=1
	fract = [1, float(len(list2))/float(len(dict0)), float(len(list7))/float(len(dict0)), float(len(list60))/float(len(dict0))]
	listA = [0, 2, 7, 60]
	plt.figure('Relative abundance of spacers, time 0 and time 60')
	plt.ylabel('Proportion of time 0 spacers present')
	plt.xlabel('Time')
	plt.plot(listA, fract, color="#3CB7CC")
	plt.xlim(xmin=0, xmax=65)
	plt.xticks(listA)
#	plt.show()
	plt.savefig(filename, dpi=500)
	plt.close()


makeLists(path1, path2, path3, path4, 'spacer_proportion.png')



