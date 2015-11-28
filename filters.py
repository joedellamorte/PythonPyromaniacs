___author__ = 'NicholasArnold'

import course


def filter_by_title(title, course_list):
    """
    :param title: Title of Course wanted
    :param course_list: Database of courses to filter through
    :return: Course or list of courses that match title
    """
    result = []
    for item in course_list:
        if item.title == title:
            result.append(item)
    return result


def filter_by_code(code, course_list, section=None):
    """
    :param code: Code for a class, ex: EK EK 128
    :param course_list: Database of courses to filter through
    :param section: Optionally allows user to specify section of course
    :return:
    """
    result = []
    for item in course_list:
        if section is not None:
            if item.code == code and item.section == section:
                result = course
        elif item.code == code:
            result.append(item)
    return result


def filter_by_professor(instructor, course_list):
    """
    :param instructor: Name of professor
    :param course_list: Database of courses to filter through
    :return: All courses taught by professor
    """
    result = []
    for item in course_list:
        if item.instructor == instructor:
            result.append(item)
    return result