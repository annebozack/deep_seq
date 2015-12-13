import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
import itertools

path = sys.argv[1]

path1 = ''+path+'spacer_count0.csv'
filename1 = 'relspacer_hist0.png'
path2 = ''+path+'spacer_count2.csv'
filename2 = 'relspacer_hist2.png'
path3 = ''+path+'spacer_count7.csv'
filename3 = 'relspacer_hist7.png'
path4 = ''+path+'spacer_count60.csv'
filename4 = 'relspacer_hist60.png'

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

def makeLists(path1, path4, filename):
	dict0 = makeDict(path1)
	dict60 = makeDict(path4)
	listkeys = list(dict0.keys())
	list0 = []
	list60 = []
	listspacers = []
	i = 0
	while i < len(listkeys):
		if listkeys[i] in dict60:
			list0.append(dict0[listkeys[i]])
			list60.append(dict60[listkeys[i]])
			listspacers.append(listkeys[i])
		i+=1
	k = 0
	abundance = []
	while k < len(listspacers):
		abundance.append([list0[k], list60[k]])
		k+=1
	order = [i[0] for i in sorted(enumerate(list0), key=lambda x:x[1])]
	l = 0
	abundancesort = []
	while l < len(abundance):
		abundancesort.append(abundance[order[l]])
		l+=1
	print abundancesort
	print type(abundancesort)
	listtimes = [0, 1, 2]
	listspacersnum = list(range(0, len(listspacers)))
	x, y = np.meshgrid(listtimes, listspacersnum)
	abundancesort = np.array(abundancesort)
	plt.pcolormesh(x, y, abundancesort)
	plt.colorbar()
	plt.show()
	plt.close()

makeLists(path1, path4, 'spacer_count_time0_2_7_60.png')


