# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:36:53 2015

@author: ScottHom
"""

# Open specific schedul with button 
"""
from tkinter import *
master = Tk()
lf = Frame(master)
lf.pack(side = LEFT)
rf = Frame(master)
rf.pack(side = RIGHT)
#schedule_op = Label(master, text = 'Schedule Options') 
#schedule_op.grid(row = 20)
def cal_outline():
    
    #Create text grid fields
    root=Tk()
    for r in range(17):
        for c in range(1,8,1): #what is (1,8,1) make a column?
            Label(root,text='', relief=GROOVE,width=15, height=2).grid(row=r,column=c)
    
    Label(root,text='', width=120, height=2).grid(row=0, columnspan=9)
    
    
    # Add each day to grid     
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
    for x in range(len(week)):
        Label(root,text=week[x]).grid(row=0,column=x+1,sticky=S)
    
    # Add each hourly time to grid 
    time = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 am', '1:00 pm', '2:00 pm', '3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm', '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm'] 
    for x in range(len(time)):
        Label(root,text=time[x]).grid(rowspan=2, row=x,column=0)
        
    root.mainloop()

v = IntVar()


    
import random

num_schedules = random.randint(1,10)

for schedules in range(num_schedules):
    name = 'Schedule'+ (str(schedules))
    filter_course = 'Option' + (str(schedules))
    Radiobutton(rf, text = filter_course , variable = v, value = schedules).pack()
    Button(lf, text = name, command = cal_outline).pack()
Radiobutton(rf, text = 'multi_check', variable = v, value = 11).pack()
mainloop()
"""

from tkinter import *
master = Tk()

#schedule_op = Label(master, text = 'Schedule Options') 
#schedule_op.grid(row = 20)
def cal_outline():
    
    #Create text grid fields
    root=Tk()
    for r in range(17):
        for c in range(1,8,1): #what is (1,8,1) make a column?
            Label(root,text='', relief=GROOVE,width=15, height=2).grid(row=r,column=c)
    
    Label(root,text='', width=120, height=2).grid(row=0, columnspan=9)
    
    
    # Add each day to grid     
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
    for x in range(len(week)):
        Label(root,text=week[x]).grid(row=0,column=x+1,sticky=S)
    
    # Add each hourly time to grid 
    time = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 am', '1:00 pm', '2:00 pm', '3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm', '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm'] 
    for x in range(len(time)):
        Label(root,text=time[x]).grid(rowspan=2, row=x,column=0)
        
    root.mainloop()

v = IntVar()


    
import random

num_schedules = random.randint(1,10)

for schedules in range(num_schedules):
    name = 'Schedule'+ (str(schedules))
    Button(master, text = name, command = cal_outline).grid(row = schedules+1, column = 1)
label_courses = Label (master, text = 'Course Choices').grid(row = 0, column = 1)
mainloop()


#picture on button https://www.youtube.com/watch?v=8HwHqa3tq70


# Task: def read_schedule() (from txt), create button to execute read_schedule() and generate_cours()

