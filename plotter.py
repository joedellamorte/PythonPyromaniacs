# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:31:35 2015

@author: Rahmeh
"""

from tkinter import *
def course_block_maker(all_poss = [(('chemistry',{'Mon':('8:30','9:00'),'Wed':('16:00','19:00')}),('physics',{'Tues':('8:00','9:00')})),(('Archeology',{'Sat':('17:30','18:30'),'Fri':('7:00','10:00')}),('Lit of Reptilian',{'Mon':('8:00','8:30'),'Wed':('7:00','8:30')}))]):
    root=Tk()
    
    option = StringVar()
    
    
    Label(root,text='You Have '+(str(len(all_poss)))+' Options').grid(row=0)
    Label(root,text='Which option would you like to view? Please type in a number.').grid(row=1)
    Entry(root,textvariable=option).grid(row=3)
    
    def call_grid():
        graph=Tk()
       
        for r in range(17):
            for c in range(1,8,1): #what is (1,8,1) make a column?
                Label(graph,text='', relief=GROOVE,width=15, height=2).grid(row=r,column=c)
        
        Label(graph,text='', width=120, height=2).grid(row=0, columnspan=9)
        
        
        # Add each day to grid     
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
        for x in range(len(week)):
            Label(graph,text=week[x]).grid(row=0,column=x+1,sticky=S)
        
        # Add each hourly time to grid 
        time = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 am', '1:00 pm', '2:00 pm', '3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm', '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm'] 
        for x in range(len(time)):
            Label(graph,text=time[x]).grid(rowspan=2, row=x,column=0)        
 ################################################################################       
        
        colors=['red','blue','green','purple','yellow']
        week=['Sun','Mon','Tues','Wed','Thurs','Fri','Sat']
        selection = option.get()
        c=0
        for course in all_poss[int(selection)-1]:
            print(course)
            title = course[0]
            days_times = course[1]
            for day in days_times:
                for i in range(len(week)):
                    if day == week[i]:
                        col = i+1
                timestart=days_times.get(day)[0]
                timeend=days_times.get(day)[1]
                start=timestart.split(':')
                start=int(start[0])+int(start[1])*5/300
                end=timeend.split(':')
                end=int(end[0])+int(end[1])*5/300
                duration=(end-start)*2
                print(start)
                if start%2!=0 and end%2==0:
                    Label(graph,text=title, background=colors[c], height=int(duration), width=15).grid(column=col,row=abs(int(start)-6),rowspan=abs(int(duration)),sticky=S)
                elif start%2!=0 and end%2!=0:
                    Label(graph,text=title, background=colors[c], height=int(duration), width=15).grid(column=col,row=abs(int(start)-6),rowspan=abs(int(duration)),sticky=S)
                elif start%2==0 and end%2!=0:
                    Label(graph,text=title, background=colors[c], height=int(duration), width=15).grid(column=col,row=abs(int(start)-6),rowspan=abs(int(duration)),sticky=N)
                else:
                    Label(graph,text=title, background=colors[c], height=int(duration), width=15).grid(column=col,row=abs(int(start)-6),rowspan=abs(int(duration)),sticky=N)
                    
            c+=1
        graph.mainloop()
    
    Button(root,text='Enter',width=15, height=2, command=call_grid).grid(column=6, sticky=SE)
    root.mainloop()   

            
course_block_maker()