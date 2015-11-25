__author__ = 'NicholasArnold'

import course

class schedule():
    def __init__(self,course_list):
        self.course_list=course_list
        self.queue = []
    def filter_by_title(self,title):
        for section in self.course_list:
            if section.title == title:
                self.queue.append(section)
    
    
    def filter_by_code(self,code, section=None):
        for section in self.course_list:
            if section is not None:
                if section.code == code and section.section == section:
                    self.queue.append(section)
            elif section.code == code:
                self.queue.append(section)

    def filter_by_professor(self,instructor):
        for section in self.course_list:
            if section.instructor == instructor:
                self.queue.append(section)
        
    def clear_q(self):
        self.queue=[]
        
