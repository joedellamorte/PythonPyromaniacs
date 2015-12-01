# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:29:29 2015

@author: mohammadalirijjal
"""

def filter_by_nomonday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'M' in course.days:
            final_result.remove(course)
    return final_result

def filter_by_nofriday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'F' in course.days:
            final_result.remove (course)
    return final_result