import sys
import csv
import matplotlib.pyplot as plt
import numpy as np

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
		

def plot(path1, path2, path3, path4, filename):
	reads1 = getColumn(path1, 2)
	reads1 = getInt(reads1)
	relreads1 = getRel(reads1)
	reads2 = getColumn(path2, 2)
	reads2 = getInt(reads2)
	relreads2 = getRel(reads2)
	reads3 = getColumn(path3, 2)
	reads3 = getInt(reads3)
	relreads3 = getRel(reads3)
	reads4 = getColumn(path4, 2)
	reads4 = getInt(reads4)
	relreads4 = getRel(reads4)
	relreads = relreads1 + relreads2 + relreads3 + relreads4
#	print relreads
	print len(relreads)
	plt.figure('Relative abundance of spacers')
	plt.xlabel('Relative abundance (reads associated with spacer/total reads)')
	plt.ylabel('Frequency')
	plt.hist(relreads, bins=100, color="#3CB7CC", alpha=0.8, log=True)
	plt.savefig(filename, dpi=500)
	plt.show()
	plt.close()

plot(path1, path2, path3, path4, 'spacer_count_alltimes.png')

