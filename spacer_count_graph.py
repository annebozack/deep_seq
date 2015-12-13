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
		

def plot(path, filename):
	reads = getColumn(path, 2)
	reads1 = getInt(reads)
	relreads = getRel(reads1)
	print relreads
	plt.figure('Relative abundance of spacers')
	plt.xlabel('Relative abundance (reads associated with spacer/total reads)')
	plt.ylabel('Frequency')
	plt.hist(relreads, bins=100, log=True, color='gray')
	plt.savefig(filename, dpi=500)
	plt.close()

plot(path1, filename1)
plot(path2, filename2)
plot(path3, filename3)
plot(path4, filename4)


