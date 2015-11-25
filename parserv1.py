# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:19:25 2015

@author: joseph
"""

import csv
import course
import course_filters
newdata=[]
with open('niceek128DATA.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in spamreader:
        newdata.append(row)
        #print(', '.join(row))
        

dictionarydata=[]
courselist=[]
goodCnt = 0
badCount = 0

for i in newdata:
    try:
	k={'course':i[0],'title':i[1],'professor':i[2],'credit':i[3],'type':i[4],'students':i[5],'seatingcapacity':i[6],'building':i[7],'room':i[8],'requestedbuilding':i[9],'requested room':i[10],'days':i[11], 'time':(i[12], i[13]) ,'notes':i[14],'unitdept':i[15],'startdate':i[16],'enddate':i[17]}
        dictionarydata.append(k)
  	c = course.Course(k['title'], k['course'],k['course'],k['type'], k['credit'],(k['building'], k['room']), k['days'], k['time'], k['professor'], k['notes'])
    	courselist.append(c)
	goodCnt+=1

    except Exception as inst:
	print (inst)
	print ("i has this many elements : " +str(len(i)))
	print (i)
	badCount+=1
	print("ERROR BUILDING LIST OF COURSES Good Count "+ str(goodCnt)+ " Bad Count " + str(badCount))
	
        pass
f = course_filters.filter_by_title("Art History 2", courselist)

for i in f:
    print(str(i))	
