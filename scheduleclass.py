import course


class Search:
    def __init__(self,course_list):
        self.course_list = course_list
        self.queue = []

    def filter_by_title(self, title):
        title = str(title)
        title = title.lower()
        for section in self.course_list:
            if title in section.title:
                self.queue.append(section)

    def filter_by_code(self, code, section=None):
        for section in self.course_list:
            if section is not None:
                if code in section.code and section in section.section:
                    self.queue.append(section)
            elif code in section.code:
                self.queue.append(section)

    def filter_by_professor(self, instructor):
        instructor = str(instructor)
        instructor = instructor.lower()
        for section in self.course_list:
            if section.instructor.lower() == instructor:
                self.queue.append(section)

    def no_monday(self):
        for section in self.queue:
            if 'Mon' in section.days:
                self.queue.remove(section)

    def no_friday(self):
        for section in self.queue:
            if 'Fri' in section.days:
                self.queue.remove(section)

    def clear_q(self):
        self.queue = []


class Schedule:
    def __init__(self, course_list):
        self.course_list = course_list
        self.taking=[]
#        self.timeday=[]
#        self.title=[]
#        self.code=[]
#        self.section=[]
#        self.typ=[]
#        self.cred=[]
#        self.location=[]
#        self.days=[]
#        self.time=[]
#        self.instructor=[]
#        self.notes=[]
#    def add_course(self,new):
#        self.timeday=self.timeday+[(new.time,new.days)]
#        self.title=self.title+new.title
#        self.code=self.code+new.code
#        self.section=self.section+new.section
#        self.typ=self.typ+new.typ
#        self.cred=self.cred+new.cred
#        self.location=self.location+new.location
#        self.days=self.days+new.days
#        self.time=self.time+new.time
#        self.instructor=self.instructor+new.instructor
#        self.notes=self.notes+new.notes

    def add_course(self, new):
        for i in self.taking:
            if new.can_schedule(i):
                pass
            else:
                raise ValueError('could not add course time conflict')
        self.taking += new

    def remove_course(self, old):
        while old in self.taking:
            self.taking.remove(old)

