# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:00:05 2015

@author: June
"""


def timeConflict(schedule,time):
    isTimeConflict = False
    sched = []
    for count in range(len(schedule)):
        sched.append(int(schedule[count][0].replace(':','')))
        sched.append(int(schedule[count][1].replace(':','')))
    time[0] = int(time[0].replace(':',''))
    time[1] = int(time[1].replace(':',''))
    for count in range(len(sched)):
        if count != len(schedule)-1:
            if time[0] >= sched[count] and time[0] < sched[count+1]:
                for days in schedule[count][2]:
                    for check in time[2]:
                        if days == check:
                            isTimeConflict = True
            elif time[1] > sched[count] and time[1] <= sched[count+1]:
                for days in schedule[count][2]:
                    for check in time[2]:
                        if days == check:
                            isTimeConflict = True
        count += 2
    return isTimeConflict

arr = [('12:00','13:00',('M','W','F')),('13:00','14:00',('T','R'))]
print(timeConflict(arr,['12:00','2:00',('M','W')]))

    
