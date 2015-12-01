# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:29:29 2015

@author: mohammadalirijjal
"""

def filter_by_noMonday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'M' in course.days:
            final_result.remove(course)
    return final_result

def filter_by_noTuesday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'T' in course.days:
            final_result.remove (course)
    return final_result

def filter_by_noWednesday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'W' in course.days:
            final_result.remove(course)
    return final_result

def filter_by_noThursday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'R' in course.days:
            final_result.remove (course)
    return final_result

def filter_by_noFriday(course_list):
    import copy
    final_result=copy.course_list
    for course in course_list:
        if 'F' in course.days:
            final_result.remove(course)
    return final_result

