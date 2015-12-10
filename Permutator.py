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
    scheduleobjects=[scheduleclass.Schedule()]
    for i in range(length):
        try:
            scheduleobjects[-1].add_course(sched[maikeys[0]][indexing[0]])
            #print('pass')
        except:
            pass
            #scheduleobjects[-1].add_course(sched[maikeys[i]][indexing[i]])
            #print('fail')    
    
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
                #print('now we see most, we did it dadadadadadadada')
            except:
                #scheduleobjects[-1].add_course(sched[maikeys[i]][indexing[i]])
                #print('we DDDDDDIIIIIIIEEEEEDDDDDD')
                pass
                #scheduleobjects[-1].add_course(sched[maikeys[i]][indexing[i]])
                #print('fail')
    return scheduleobjects
def permutator(crs1,crs2,crs3,crs4):
    
    sched = {}
    for i in crs1:
        name = i.typ+'1'
        if name not in sched:
            sched[name] = [i]
        else:
            if i in sched[name]:
                sched[name].append(i)
    try:
        for i in crs2:
            name = i.typ+'2'
            if name not in sched:
                sched[name] = [i]
            else:
                if i in sched[name]:
                    sched[name].append(i)
    except:
        print('skipped2')
        pass
    try:
        for i in crs3:
            name = i.typ+'3'
            if name not in sched:
                sched[name] = [i]
            else:
                if i in sched[name]:
                    sched[name].append(i)
    except:
        print('skipped3')
        pass
    try:
        for i in crs4:
            name = i.typ+'4'
            if name not in sched:
                sched[name] = [i]
            else:
                if i in sched[name]:
                    sched[name].append(i)
    except:
        print('skipped4')
        pass
    return indexer(sched)
        

            
    def scheduleMaker(num):
        scheduleobjects.append(scheduleclass.Schedule)
        scheduleMaker()
    