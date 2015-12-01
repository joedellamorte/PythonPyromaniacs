## -*- coding: utf-8 -*-
#"""
#Created on Sun Nov 22 11:50:31 2015
#
#@author: Rahmeh
#"""
#
##import tkinter as tk
##class App:
##    def __init__(self, root):
##        frame = tk.Frame(root)
##        frame.pack()
##
##        self.button = tk.Button(frame, text="Don't do anything", font='courier', foreground = 'Red', command=self.donothing)
##        self.button.pack(side=tk.LEFT)
##
##        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
##        self.hi_there.pack(side=tk.LEFT)
##
##    def say_hi(self):
##        print("hi there, everyone!")
##    def donothing(self):
##        pass
##
##base = tk.Tk()
##
##app = App(base)
##
##base.mainloop()
#
#
#from tkinter import *
#
#def sched_outline():
#    print ('hi')
##    root=Tk()
##    outline = Canvas(root, width=900, height=700)
##    outline.pack()
##    
##    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
##    count = 0
##    for i in range(100, 800, 100):
##        outline.create_text(50+i,30,text=week[count])
##        for j in range(40, 680, 40):
##            outline.create_rectangle(i, j, 100+i, j+40, fill="")   
##        count+=1
##    
##    time = ['7:00 am', '8:00 am', '9:00 am', '10:00 am', '11:00 am', '12:00 am', '1:00 pm', '2:00 pm', '3:00 pm', '4:00 pm', '5:00 pm', '6:00 pm', '7:00 pm', '8:00 pm', '9:00 pm', '10:00 pm'] 
##    count = 0
##    for x in range(40, 680, 40):
##        outline.create_text(75,x,text=time[count])
##        count += 1
##    
##    root.mainloop()
#        
#def all_options():
#    base=Tk()
#    opts = Canvas(base)
#    opts.pack()
#    
#    #for i in range(3):
#    Button(base, text=("Option"))
##    for i in range(4):
##        button = opts.Checkbutton(frame, text="Don't do anything", font='courier', foreground = 'Red', command=self.donothing)
##    
#    base.mainloop()
#    
#    
#all_options()
#
# 
##for i in range(len(dct))
#        
#    
#    
#
##w.create_rectangle(65, 35, 135, 65, fill="yellow")
##w.create_line(0, 0, 50, 20, fill="green", width=3)
##w.create_line(0, 100, 50, 80, fill="green", width=3)
##w.create_line(150,20, 200, 0, fill="green", width=3)
##w.create_line(150, 80, 200, 100, fill="green", width=3)
##
##xy = 200, 20, 400, 220
##w.create_arc(xy, start=0, extent=270, fill="red")
##w.create_arc(xy, start=270, extent=60, fill="blue")
##w.create_arc(xy, start=330, extent=30, fill="green")
##
##w.create_oval(20,250, 80, 310, fill = 'purple')
##w.create_polygon(20,350,70,350,50,390,fill='black')  # needs at least 3 points...
##w.create_rectangle(100,350,200,400,fill='cyan')
#


import tkinter as tk
class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()

        self.button = tk.Button(frame, text="Don't do anything", font='courier', foreground = 'Red', command=self.donothing)
        self.button.pack(side=tk.LEFT)

        self.hi_there = tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("hi there, everyone!")
    def donothing(self):
        pass

base = tk.Tk()

app = App(base)

base.mainloop()