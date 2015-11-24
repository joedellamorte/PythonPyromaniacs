__author__ = 'NicholasArnold'

import course


def filter_by_title(title,course_list):
    result = []
    for course in course_list:
        if course.title == title:
            result.append(course)
    return result


def filter_by_code(code, course_list, section=None):
    result = []
    for course in course_list:
        if section is not None:
            if course.code == code and course.section == section:
                result = course
        elif course.code == code:
            result.append(course)
    return result


def filter_by_professor(instructor, course_list):
    result = []
    for course in course_list:
        if course.instructor == instructor:
            result.append(course)
    return result


