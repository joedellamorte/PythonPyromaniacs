# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:19:25 2015

@author: joseph
"""

import csv
k=[]
with open('/Users/joseph/Desktop/EK128_Fall2015/Final Project/niceek128DATA.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in spamreader:
        k.append(row)
        #print(', '.join(row))
        
newdata=[]

for i in k:
    i=i[0]
    i=i.split('"')
    i=i.pop(0).split(',')+i
    l=i.pop(-1).split(',')
    i=i+l
    try:
        i=i[:11]+i[12:]
    except:
        pass
    #i=i[:11]+i[12:]
    newdata=newdata+[i]
    print(i)
dictionarydata=[]

for i in newdata:
    try:
        k={'course':i[0],'title':i[1],'professor':i[2],'credit':i[3],'type':i[4],'students':i[5],'seatingcapacity':i[6],'building':i[7],'room':i[8],'requestedbuilding':i[9],'requested room':i[10],'start/stop time':i[11],'notes':i[12],'uk':i[13],'uk2':i[14],'uk3':i[15],'startdate':i[16],'enddate':i[17]}
        dictionarydata.append(k)
    except:
        pass