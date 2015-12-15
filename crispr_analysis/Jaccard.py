# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import sys
import os
import numpy
import matplotlib.pyplot as plt

# <codecell>

Threshold = .000
os.chdir('/Users/aress91/Desktop/CRASS Analysis/')
Time0 = open('DRsTime0')
Time2 = open('DRsTime2')
Time7 = open('DRsTime7')
Time60 = open('DRsTime60')
csv_0 = list(csv.reader(Time0))
csv_2 = list(csv.reader(Time2))
csv_7 = list(csv.reader(Time7))
csv_60 = list(csv.reader(Time60))
Jaccard = np.zeros(4)
Jaccard[0]=1
# Put all the relative abundances in column 1
print(len(csv_0))
    

# <codecell>

#Thresholding
i = 0
csv_0T = []
csv_2T = []
csv_7T = []
csv_60T = []
while i <= len(csv_0) - 1:
    if float(csv_0[i][2]) >= Threshold:
        csv_0T.append([csv_0[i][1],csv_0[i][2]])
        i = i + 1
    else:
        i = i + 1
i=0
while i <= len(csv_2) - 1:
    if float(csv_2[i][2]) >= Threshold:
        csv_2T.append([csv_2[i][1],csv_2[i][2]])
        i = i + 1
    else:
        i = i + 1
i=0
while i <= len(csv_7) - 1:
    if float(csv_7[i][2]) >= Threshold:
        csv_7T.append([csv_7[i][1],csv_7[i][2]])
        i = i + 1
    else:
        i = i + 1
i=0
while i <= len(csv_60) - 1:
    if float(csv_60[i][2]) >= Threshold:
        csv_60T.append([csv_60[i][1],csv_60[i][2]])
        i = i + 1
    else:
        i = i + 1

print(len(csv_0T))
print(len(csv_2T))
print(len(csv_7T))
print(len(csv_60T))

# <codecell>

col = 1
#Are you in time 2? Yay or Nay
i=0
j=0
while i < len(csv_0T)-1:
    if csv_0T[i][0] == csv_2T[j][0]:
        #print('hurray')
        Jaccard[col] = Jaccard[col]+1
        i=i+1
    elif i == len(csv_0T)-1:
        print('no luck')
    else:
        if j < len(csv_2T)-1:
            j=j+1
        else:
            #print('no bueno')
            i=i+1
            j=1
print(Jaccard[col])
Jaccard[col] = Jaccard[col]/(len(csv_0T)+len(csv_2T)-Jaccard[col])
#Are you in time 7? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0T)-1:
    if csv_0T[i][0] == csv_7T[j][0]:
        #print('hurray')
        Jaccard[col] = Jaccard[col]+1
        i=i+1
    elif i == len(csv_0T)-1:
        print('no luck')
    else:
        if j < len(csv_7T)-1:
            j=j+1
        else:
            #print('no bueno')
            i=i+1
            j=1
print(Jaccard[col])
Jaccard[col] = Jaccard[col]/(len(csv_0T)+len(csv_2T)-Jaccard[col])
#Are you in time 60? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0T)-1:
    if csv_0T[i][0] == csv_60T[j][0]:
        #print('hurray')
        Jaccard[col] = Jaccard[col]+1
        i=i+1
    elif i == len(csv_0T)-1:
        print('no luck')
    else:
        if j < len(csv_60T)-1:
            j=j+1
        else:
            #print('no bueno')
            i=i+1
            j=1
print(Jaccard[col])
Jaccard[col] = Jaccard[col]/(len(csv_0T)+len(csv_2T)-Jaccard[col])

print(Jaccard)

# <codecell>


# <codecell>

os.chdir('/Users/aress91/Desktop/CRASS Data 2/')
Time0 = open('DRsTime0')
Time2 = open('DRsTime2')
Time7 = open('DRsTime7')
Time60 = open('DRsTime60')
csv_0 = list(csv.reader(Time0))
csv_2 = list(csv.reader(Time2))
csv_7 = list(csv.reader(Time7))
csv_60 = list(csv.reader(Time60))
Jaccard2 = np.zeros(4)
Jaccard2[0]=1
i = 0
csv_0T = []
csv_2T = []
csv_7T = []
csv_60T = []
while i <= len(csv_0) - 1:
    if float(csv_0[i][2]) >= Threshold:
        csv_0T.append([csv_0[i][1],csv_0[i][2]])
        i = i + 1
    else:
        i = i + 1
i=0
while i <= len(csv_2) - 1:
    if float(csv_2[i][2]) >= Threshold:
        csv_2T.append([csv_2[i][1],csv_2[i][2]])
        i = i + 1
    else:
        i = i + 1
i=0
while i <= len(csv_7) - 1:
    if float(csv_7[i][2]) >= Threshold:
        csv_7T.append([csv_7[i][1],csv_7[i][2]])
        i = i + 1
    else:
        i = i + 1
i=0
while i <= len(csv_60) - 1:
    if float(csv_60[i][2]) >= Threshold:
        csv_60T.append([csv_60[i][1],csv_60[i][2]])
        i = i + 1
    else:
        i = i + 1
col = 1
#Are you in time 2? Yay or Nay
i=0
j=0
while i < len(csv_0T)-1:
    if csv_0T[i][0] == csv_2T[j][0]:
        #print('hurray')
        Jaccard2[col] = Jaccard2[col]+1
        i=i+1
    elif i == len(csv_0T)-1:
        print('no luck')
    else:
        if j < len(csv_2T)-1:
            j=j+1
        else:
            #print('no bueno')
            i=i+1
            j=1
Jaccard2[col] = Jaccard2[col]/(len(csv_0T)+len(csv_2T)-Jaccard2[col])
#Are you in time 7? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0T)-1:
    if csv_0T[i][0] == csv_7T[j][0]:
        #print('hurray')
        Jaccard2[col] = Jaccard2[col]+1
        i=i+1
    elif i == len(csv_0T)-1:
        print('no luck')
    else:
        if j < len(csv_7T)-1:
            j=j+1
        else:
            #print('no bueno')
            i=i+1
            j=1
Jaccard2[col] = Jaccard2[col]/(len(csv_0T)+len(csv_2T)-Jaccard2[col])
#Are you in time 60? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0T)-1:
    if csv_0T[i][0] == csv_60T[j][0]:
        #print('hurray')
        Jaccard2[col] = Jaccard2[col]+1
        i=i+1
    elif i == len(csv_0T)-1:
        print('no luck')
    else:
        if j < len(csv_60T)-1:
            j=j+1
        else:
            #print('no bueno')
            i=i+1
            j=1
Jaccard2[col] = Jaccard2[col]/(len(csv_0T)+len(csv_2T)-Jaccard2[col])

# <codecell>

#plt.yscale('log')
plt.ylabel('Jaccard Index (DRs)')
plt.xlabel('Time')
MyTitle = "Threshold = %s" % float(Threshold)
plt.suptitle(MyTitle)
Time = [0,2,7,60]
plt.xticks([0,2,7,60])
p1, = plt.plot(Time, Jaccard, color="#3CB7CC")
p2, = plt.plot(Time, Jaccard2, color='darkblue')
legend([p1,p2],['Alien','Bugkiller'])

# <codecell>


# <codecell>


