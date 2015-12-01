# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:03:40 2015

@author: Rahmeh
"""

from tkinter import *

root=Tk()

col_1 = StringVar(); dep_1 = StringVar(); crs_1 = StringVar()
col_2 = StringVar(); dep_2 = StringVar(); crs_2 = StringVar()
col_3 = StringVar(); dep_3 = StringVar(); crs_3 = StringVar()
col_4 = StringVar(); dep_4 = StringVar(); crs_4 = StringVar()
col_5 = StringVar(); dep_5 = StringVar(); crs_5 = StringVar()
col_6 = StringVar(); dep_6 = StringVar(); crs_6 = StringVar()

for i in range(6):
    Label(root, text=("Course", str(i+1))).grid(row=(i+1),column=0)

Label(root, text="College").grid(row=0, column=1)
Label(root, text="Dept").grid(row=0, column=2)
Label(root, text="Course #").grid(row=0, column=3)
   
college_1 = Entry(root,textvariable=col_1).grid(column=1, row=1)
department_1 = Entry(root,textvariable=dep_1).grid(column=2, row=1)
course_1 = Entry(root,textvariable=crs_1).grid(column=3, row=1)

college_2 = Entry(root,textvariable=col_2).grid(column=1, row=2)
department_2 = Entry(root,textvariable=dep_2).grid(column=2, row=2)
course_2 = Entry(root,textvariable=crs_2).grid(column=3, row=2)

college_3 = Entry(root,textvariable=col_3).grid(column=1, row=3)
department_3 = Entry(root,textvariable=dep_3).grid(column=2, row=3)
course_3 = Entry(root,textvariable=crs_3).grid(column=3, row=3)

college_4 = Entry(root,textvariable=col_4).grid(column=1, row=4)
department_4 = Entry(root,textvariable=dep_4).grid(column=2, row=4)
course_4 = Entry(root,textvariable=crs_4).grid(column=3, row=4)

college_5 = Entry(root,textvariable=col_5).grid(column=1, row=5)
department_5 = Entry(root,textvariable=dep_5).grid(column=2, row=5)
course_5 = Entry(root,textvariable=crs_5).grid(column=3, row=5)

college_6 = Entry(root,textvariable=col_6).grid(column=1, row=6)
department_6 = Entry(root,textvariable=dep_6).grid(column=2, row=6)
course_6 = Entry(root,textvariable=crs_6).grid(column=3, row=6)

def collect_data():
    class1 = col_1.get() + ' ' + dep_1.get() + ' ' + crs_1.get()
    print (class1)

Button(root,text='Enter', relief=GROOVE,width=15, height=2, command=collect_data).grid()

    
root.mainloop()

