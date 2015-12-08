# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 02:17:54 2015

@author: June
"""
import scheduleclass
def indexer(sched):
    maikeys=list(sched.keys())[:]
    length=len(maikeys)
    indexing=[0]*length
    scheduleobjects=[]
    while indexing[-1]!=len(sched[maikeys[-1]]):
        cary=1
        for i in range(length):
            if len(sched[maikeys[i]])==indexing[i]:
                indexing[i]=indexing[i]-len(sched[maikeys[i]])
                cary=1
            else:
                indexing[i]+=cary
                cary=0
        scheduleobjects.append(scheduleclass.Schedule())
        for i in range(len(indexing)):
            try:
                scheduleobjects[-1].add_course(sched[maikeys[i]][indexing[i]])
                print('pass')
            except:
                #scheduleobjects[-1].add_course(sched[maikeys[i]][indexing[i]])
                print('fail')
    return scheduleobjects
def permutator(crs1,crs2,crs3,crs4):
    
    sched = {}
    for i in crs1:
        name = i.typ+'1'
        if name not in sched:
            sched[name] = [i]
        else:
            sched[name].append(i)
    for i in crs2:
        name = i.typ+'2'
        if name not in sched:
            sched[name] = [i]
        else:
            sched[name].append(i)
    for i in crs3:
        name = i.typ+'3'
        if name not in sched:
            sched[name] = [i]
        else:
            sched[name].append(i)
    for i in crs4:
        name = i.typ+'4'
        if name not in sched:
            sched[name] = [i]
        else:
            sched[name].append(i)
    return indexer(sched)
        

            
    def scheduleMaker(num):
        scheduleobjects.append(scheduleclass.Schedule)
        scheduleMaker()
    