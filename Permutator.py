# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 02:17:54 2015

@author: June
"""
import scheduleclass

def permutator(crs1,crs2,crs3,crs4):
    
    sched = {}
    for i in crs1:
        name = i.typ+'1'
        if name not in sched1:
            sched[name] = [i]
        else:
            sched[name].append(i)
    for i in crs2:
        name = i.typ+'2'
        if name not in sched2:
            sched[name] = [i]
        else:
            sched[name].append(i)
    for i in crs3:
        name = i.typ+'3'
        if name not in sched3:
            sched[name] = [i]
        else:
            sched[name].append(i)
    for i in crs4:
        name = i.typ+'4'
        if name not in sched4:
            sched[name] = [i]
        else:
            sched[name].append(i)
                
    maikeys=sched.keys()[:]
    length=len(maikeys)
    indexing=[0]*length
    scheduleobjects=[]
    while 1:
        schedule
        
        
    