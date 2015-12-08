# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:02:57 2015

@author: Rahmeh
"""


from tkinter import *

def cal_outline():      #creates a blank calander that we can eventually plot possible schedules on
    root=Tk()
    for r in range(17):
        for c in range(1,8,1):
            Label(root,text='', relief=GROOVE,width=15, height=2).grid(row=r,column=c)
    
    Label(root,text='', width=120, height=2).grid(row=0, columnspan=9)
    
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for x in range(len(week)):
        Label(root,text=week[x]).grid(row=0,column=x+1,sticky=S)
    
    time = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 am', '1:00 pm', '2:00 pm', '3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm', '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm'] 
    for x in range(len(time)):
        Label(root,text=time[x]).grid(rowspan=2, row=x,column=0)
    Label(root,text='', height=3,  width=15, background='red').grid(rowspan=2,row=4, column=5, sticky=N)    
    root.mainloop()
#cal_outline() 
 
def all_options():          #creates window with a bunch of buttons that are eventually supposed to each open
    base=Tk()               #another window with a schedule possibiliy on it, but it doesn't work right now
    for i in range(10):
        Button(base,text=('Option', str(i)), relief=GROOVE,width=15, height=2, command = print('hi')).grid()
    
    
#    Label(root,text='', width=120, height=2).grid(row=0, columnspan=9)
#    
#    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
#    for x in range(len(week)):
#        Label(root,text=week[x]).grid(row=0,column=x+1,sticky=S)
#    
#    time = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 am', '1:00 pm', '2:00 pm', '3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm', '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm'] 
#    for x in range(len(time)):
#        Label(root,text=time[x]).grid(rowspan=2, row=x,column=0)
#        
    base.mainloop()
  
cal_outline()
