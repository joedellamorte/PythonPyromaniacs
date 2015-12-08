# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:03:40 2015

@author: Rahmeh
"""


from tkinter import *
def prompt_user():
    MyInfo={}
    root=Tk()
    
    col_1 = StringVar(); dep_1 = StringVar(); crs_1 = StringVar();sect_1 = StringVar();instr_1 = StringVar(); ttl_1 = StringVar()
    col_2 = StringVar(); dep_2 = StringVar(); crs_2 = StringVar();sect_2 = StringVar();instr_2 = StringVar(); ttl_2 = StringVar()
    col_3 = StringVar(); dep_3 = StringVar(); crs_3 = StringVar();sect_3 = StringVar();instr_3 = StringVar(); ttl_3 = StringVar()
    col_4 = StringVar(); dep_4 = StringVar(); crs_4 = StringVar();sect_4 = StringVar();instr_4 = StringVar(); ttl_4 = StringVar()
    col_5 = StringVar(); dep_5 = StringVar(); crs_5 = StringVar();sect_5 = StringVar();instr_5 = StringVar(); ttl_5 = StringVar()
    col_6 = StringVar(); dep_6 = StringVar(); crs_6 = StringVar();sect_6 = StringVar();instr_6 = StringVar(); ttl_6 = StringVar()
    no_monday = IntVar() ; no_friday = IntVar()
    
    for i in range(6):
        Label(root, text=("Course", str(i+1))).grid(row=(i+1),column=0)
    
    Label(root, text="College").grid(row=0, column=1)
    Label(root, text="Dept").grid(row=0, column=2)
    Label(root, text="Course #").grid(row=0, column=3)
    Label(root, text="Section").grid(row=0, column=4)
    Label(root, text="Instructor").grid(row=0, column=5)
    Label(root, text="Title").grid(row=0, column=6)
       
    college_1 = Entry(root,textvariable=col_1).grid(column=1, row=1)
    department_1 = Entry(root,textvariable=dep_1).grid(column=2, row=1)
    course_1 = Entry(root,textvariable=crs_1).grid(column=3, row=1)
    section_1 = Entry(root,textvariable=sect_1).grid(column=4, row=1)
    instructor_1 = Entry(root,textvariable=instr_1).grid(column=5, row=1)
    title_1 = Entry(root,textvariable=ttl_1).grid(column=6, row=1)
    
    college_2 = Entry(root,textvariable=col_2).grid(column=1, row=2)
    department_2 = Entry(root,textvariable=dep_2).grid(column=2, row=2)
    course_2 = Entry(root,textvariable=crs_2).grid(column=3, row=2)
    section_2 = Entry(root,textvariable=sect_2).grid(column=4, row=2)
    instructor_2 = Entry(root,textvariable=instr_2).grid(column=5, row=2)
    title_2 = Entry(root,textvariable=ttl_2).grid(column=6, row=2)
    
    college_3 = Entry(root,textvariable=col_3).grid(column=1, row=3)
    department_3 = Entry(root,textvariable=dep_3).grid(column=2, row=3)
    course_3 = Entry(root,textvariable=crs_3).grid(column=3, row=3)
    section_3 = Entry(root,textvariable=sect_3).grid(column=4, row=3)
    instructor_3 = Entry(root,textvariable=instr_3).grid(column=5, row=3)
    title_3 = Entry(root,textvariable=ttl_3).grid(column=6, row=3)
    
    college_4 = Entry(root,textvariable=col_4).grid(column=1, row=4)
    department_4 = Entry(root,textvariable=dep_4).grid(column=2, row=4)
    course_4 = Entry(root,textvariable=crs_4).grid(column=3, row=4)
    section_4 = Entry(root,textvariable=sect_4).grid(column=4, row=4)
    instructor_4 = Entry(root,textvariable=instr_4).grid(column=5, row=4)
    title_4 = Entry(root,textvariable=ttl_4).grid(column=6, row=4)
    
    college_5 = Entry(root,textvariable=col_5).grid(column=1, row=5)
    department_5 = Entry(root,textvariable=dep_5).grid(column=2, row=5)
    course_5 = Entry(root,textvariable=crs_5).grid(column=3, row=5)
    section_5 = Entry(root,textvariable=sect_5).grid(column=4, row=5)
    instructor_5 = Entry(root,textvariable=instr_5).grid(column=5, row=5)
    title_5 = Entry(root,textvariable=ttl_5).grid(column=6, row=5)
    
    college_6 = Entry(root,textvariable=col_6).grid(column=1, row=6)
    department_6 = Entry(root,textvariable=dep_6).grid(column=2, row=6)
    course_6 = Entry(root,textvariable=crs_6).grid(column=3, row=6)
    section_6 = Entry(root,textvariable=sect_6).grid(column=4, row=6)
    instructor_6 = Entry(root,textvariable=instr_6).grid(column=5, row=6)
    title_6 = Entry(root,textvariable=ttl_6).grid(column=6, row=6)
    
    misc_label = Label(root, text="").grid(row=7, columnspan=6)
    more_options = Label(root, text="Other Preferences:").grid(column=2,row=8,sticky=W)    
    no_mon = Checkbutton(root,text="No Monday Classes", variable=no_monday).grid(column=3, row=8)
    no_fri = Checkbutton(root,text="No Friday Classes", variable=no_friday).grid(column=4, row=8)    

    
    def collect_data():
        class1 = {'college':[col_1.get(),col_2.get(),col_3.get(),col_4.get(),col_5.get(),col_6.get()],
        'department':[dep_1.get(),dep_2.get(),dep_3.get(),dep_4.get(),dep_5.get(),dep_6.get()],
        "course":[crs_1.get(),crs_2.get(),crs_3.get(),crs_4.get(),crs_5.get(),crs_6.get()],
        "instructor":[instr_1.get(),instr_2.get(),instr_3.get(),instr_4.get(),instr_5.get(),instr_6.get()],
        "Title":[ttl_1.get(),ttl_2.get(),ttl_3.get(),ttl_4.get(),ttl_5.get(),ttl_6.get()], 
        "section":[sect_1.get(),sect_2.get(),sect_3.get(),sect_4.get(),sect_5.get(),sect_6.get()],
        "other":[no_monday.get(), no_friday.get()]}

        MyInfo['classes']=class1
        root.destroy()
        
    
    Button(root,text='Enter', relief=GROOVE,width=15, height=2, command=collect_data).grid(column=6, sticky=SE)
    root.mainloop()   
    return MyInfo    


l=prompt_user()
print (l)

