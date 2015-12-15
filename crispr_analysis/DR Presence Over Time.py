# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import csv
import sys
import os
import numpy
import matplotlib.pyplot as plt
os.chdir('/Users/aress91/Desktop/CRASS Analysis/')

# <codecell>

Time0 = open('DRsTime0')
Time2 = open('DRsTime2')
Time7 = open('DRsTime7')
Time60 = open('DRsTime60')
csv_0 = list(csv.reader(Time0))
csv_2 = list(csv.reader(Time2))
csv_7 = list(csv.reader(Time7))
csv_60 = list(csv.reader(Time60))
MyArray = np.zeros((len(csv_0),4))
# Put all the relative abundances in column 1
i=-1
while i < len(csv_0)-1:
    i = i + 1
    MyArray[i][0] = csv_0[i][2]
    

# <codecell>

col = 0
#Are you in time 2? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0)-1:
    if csv_0[i][1] == csv_2[j][1]:
        #print('hurray')
        MyArray[i][col] = csv_2[j][2]
        i=i+1
    elif i == len(csv_0)-1:
        print('no luck')
    else:
        if j < len(csv_2)-1:
            j=j+1
        else:
            #print('no bueno')
            MyArray[i][col]=0
            i=i+1
            j=1
#Are you in time 7? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0)-1:
    if csv_0[i][1] == csv_7[j][1]:
        #print('hurray')
        MyArray[i][col] = csv_7[j][2]
        i=i+1
    elif i == len(csv_0)-1:
        print('no luck')
    else:
        if j < len(csv_7)-1:
            j=j+1
        else:
            #print('no bueno')
            MyArray[i][col]=0
            i=i+1
            j=1
#Are you in time 60? Yay or Nay
i=0
j=0
col = col + 1
while i < len(csv_0)-1:
    if csv_0[i][1] == csv_60[j][1]:
        #print('hurray')
        MyArray[i][col] = csv_60[j][2]
        i=i+1
    elif i == len(csv_0)-1:
        print('no luck')
    else:
        if j < len(csv_60)-1:
            j=j+1
        else:
            #print('no bueno')
            MyArray[i][col]=0
            i=i+1
            j=1

# <codecell>

t = 1;
i=0;
plt.figure(dpi=500)
plt.xlim((-5,65))
colors=['#32A251', '#ACD98D', '#FF7F0F', '#FFB977', '#3CB7CC', '#98D9E4', '#B85A0D', '#E1D94A', '#39737C', '#86B4A9', '#82853B']
while t < len(csv_0):
    exclude7 = [float(MyArray[t-1,0]), float(MyArray[t-1,1]), float(MyArray[t-1,3])]
    if exclude7[0] > 0 and exclude7[1] > 0 and exclude7[2] > 0:
        print(exclude7)
        #plt.figure('Relative abundance of DRs')
        plt.xlabel('Time')
        plt.xticks([0,2,60])
        plt.ylabel('Relative abundance')
        plt.yscale('log')
        plt.plot([0,2,60], exclude7[:], color = colors[i])
        i = i+1
        t=t+1
    else:
        t = t+1




