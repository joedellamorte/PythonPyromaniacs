# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 14:19:25 2015

@author: joseph
"""
#######################################################################
#### we import the modules: 
#### csv to use to read the csvfile
#### courses to make the dictionary objects in to course objects
#### course_filters to start filtering later on
#######################################################################
import csv
import course
import scheduleclass
import input_window
import Permutator


#######################################################################
##### newdata is a list which holds lists,one for each class
#######################################################################
newdata=[]


#######################################################################
# we do some magic that reads the csvfile in to the list newdata as lists
#
# newdata[0][0] is the 0'th row, 0'th column
# newdata[1][0] is the 1'st row, 0'th column
# newdata[19][1] is the 19'th row, 1'st column
#######################################################################
with open('niceek128DATA.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in spamreader:
        newdata.append(row)
        #print(', '.join(row))
        
        
#############################################################################      
# we create an empty list to hold the dictionaries we are going to make from
# the lists in newdata
#############################################################################
dictionarydata=[]

#######################################################################
# we create an empty list courselist to hold the course objects created later on
#######################################################################
courselist=[]

#######################################################################
# we create a goodcounter and a bad counter to let us know how many of the 
# rows were successfully turned in to course objects
#######################################################################
goodCnt = 0
badCount = 0

#######################################################################
# we are reading the list of lists in to dictionaries, packing those
# dictionaries in to the list dictionarydata and in to a course object
# which is then packed in to a list of course objects known as courselist
#######################################################################
for i in newdata:
    try:
        k={'course':i[0],'title':i[1],'professor':i[2],'credit':i[3],'type':i[4],'students':i[5],'seatingcapacity':i[6],'building':i[7],'room':i[8],'requestedbuilding':i[9],'requested room':i[10],'days':i[11], 'time':(i[12], i[13]) ,'notes':i[14],'unitdept':i[15],'startdate':i[16],'enddate':i[17]}
#        print('****1')        
        dictionarydata.append(k)
#        print('****2')
        c = course.Course(k['title'], k['course'],k['course'],k['type'], k['credit'],(k['building'], k['room']), k['days'], k['time'], k['professor'], k['notes'])
#        print('****3')        
        courselist.append(c)
#        print('****4')
        goodCnt+=1
#        print ("i has this many elements : " +str(len(i)))
#        print (i)
        
#######################################################################
# if the number of columns was incorrect or something we run through this code
# and print some stuff out to see
#######################################################################
    except Exception as inst:
        #print (inst)
#        print ("i has this many elements : " +str(len(i)))
#        print (i)
#        #badCount+=1
#        print("****************************************************ERROR BUILDING LIST OF COURSES Good Count "+ str(goodCnt)+ " Bad Count " + str(badCount))
        pass
#f = course_filters.filter_by_title("Art History 2", courselist)
#
#for i in f:
#    print(str(i))	
        
        
        
###############################
#collegelist=[]
#for i in courselist:
#    if not(i.courseNum in collegelist):
#        collegelist.append(i.courseNum)
#print(collegelist)
#####################################




if __name__=='__main__':
    userinput=input_window.prompt_user()
    print(userinput)
    k=scheduleclass.search(courselist)
    #print('the queue is '+str(len(k.queue))+' items long')
    ourclassinput1=k.finder(userinput['college'][0],userinput['department'][0],userinput['course'][0],userinput['section'][0],userinput['instructor'][0],userinput['Title'][0])
    ourclassinput2=k.finder(userinput['college'][1],userinput['department'][1],userinput['course'][1],userinput['section'][1],userinput['instructor'][1],userinput['Title'][1])
    ourclassinput3=k.finder(userinput['college'][2],userinput['department'][2],userinput['course'][2],userinput['section'][2],userinput['instructor'][2],userinput['Title'][2])
    ourclassinput4=k.finder(userinput['college'][3],userinput['department'][3],userinput['course'][3],userinput['section'][3],userinput['instructor'][3],userinput['Title'][3])
    possibleschedules=Permutator.permutator(ourclassinput1,ourclassinput2,ourclassinput3,ourclassinput4)
    possibleschedules.sort(key=len)  
    for i in possibleschedules:
        pass
    #print(possibleschedules[1])
    WifeyNoodles = scheduleclass.search(possibleschedules)
#    print(WifeyNoodles)
    WifeyNoodles.InstructorSched(userinput['instructor'])
    print(WifeyNoodles)
    print(len(WifeyNoodles))
    
    #k.sortof('','','','','c')

