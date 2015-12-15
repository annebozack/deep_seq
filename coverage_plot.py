import sys
import csv
import matplotlib.pyplot as plt
from scipy import stats

path = sys.argv[1]

path1 = ''+path+'spacer_count1.csv'
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

def plot(path1, path2, path3, path4, filename):
	calculated1 = getInt(getColumn(path1, 2))
	cov1 = getInt(getColumn(path1, 3))
	calculated2 = getInt(getColumn(path2, 2))
	cov2 = getInt(getColumn(path2, 3))
	calculated3 = getInt(getColumn(path3, 2))
	cov3 = getInt(getColumn(path3, 3))
	calculated4 = getInt(getColumn(path4, 2))
	cov4 = getInt(getColumn(path4, 3))
	calculated = calculated1 + calculated2 + calculated3 + calculated4
	cov = cov1 + cov2 + cov3 + cov4
	slope, intercept, r_value, p_value, std_err = stats.linregress(calculated, cov)
	r2 = r_value**2
	plt.figure('Coverage calculated from Crass')
	plt.xlabel('Coverage calculated')
	plt.ylabel('Coverage provided from Crass')
	plt.plot([.9, 400], [.9, 400], color='black', linewidth=.25)
	plt.loglog(calculated, cov, 'ro', color="#3CB7CC", alpha=.3)
	plt.ylim(ymin=0, ymax=400)
	plt.xlim(xmin=0, xmax=400)
	plt.annotate('R2 = ' + str(r2), xy=(1.5, 250), xycoords='data')
	plt.savefig(filename, dpi=500)
	plt.close()

plot(path1, path2, path3, path4, 'cov_plot_alltime_2.png')





