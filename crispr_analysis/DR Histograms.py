# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import xml.etree.ElementTree as ET
import csv
import sys
import os
import numpy
import matplotlib.pyplot as plt
os.chdir('/Users/aress91/Desktop/CRASS Analysis/')
#tree = ET.parse('/Users/aress91/Desktop/CRASS Analysis/Time 60/crass.crispr')
#root = tree.getroot()
#print((len(root[0][0][0])))
#print(root[1].attrib)

# <codecell>

TotAb = np.zeros(4)
#TotAb = [5924, 3012, 13433, 6835]
TotAb = [4543, 3341, 3882, 4249]
time = [0, 2, 7, 60]
k = -1;
#bop = np.zeros(4)
with open('DRsTimeAll', 'wb') as file:
    for i in time:
        reads = 0
        k = k + 1
        path = '/Users/aress91/Desktop/CRASS Analysis/Time %s/crass.crispr' % i
        tree = ET.parse(path)
        root = tree.getroot()
        print(len(root))
        #newfile = 'DRsTime'&i&'.csv'
        wr = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        j=0
        while j < len(root):
            # Abund = total abundance. relative abundance calculated later. 
            Abund = len(root[j][0][0]) / float(TotAb[k])
            group = [root[j].attrib["gid"], root[j].attrib["drseq"], Abund]
            wr.writerow(group)
            #bop[k] = bop[k] + Abund
            j+=1
file.close()


# <codecell>

results = csv.reader(open('DRsTimeAll'), delimiter=',')
relreads = [float(result[2]) for result in results]
print(max(relreads))
plt.figure('Relative abundance of DRs', dpi=1000)
plt.xlabel('Relative abundance (reads associated with DR/total reads)')
plt.ylabel('Frequency')
plt.hist(relreads, bins=125, log=True, color="#3CB7CC")
plt.xlim(xmax = .5)
plt.ylim(ymin = .75, ymax=100)
plt.savefig('FigTimeAll', dpi=1000)
plt.close()

# <codecell>


# <codecell>


