import course
import matplotlib as plt

class Search:
    def __init__(self,course_list):
        self.course_list = course_list
        self.queue = course_list
        
    def distance(self,crse,inpt):
        distance = 0
        beta = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+'
        
        for i in range(len(beta)):
            distance += (inpt.count(beta[i])-crse.count(beta[i]))**2
    
        return float(distance**(1/2))

#    def filter_by_title(self, title):
#        title = str(title)
#        title = title.lower()
#        minimumdist=50
#        lowestcourse=[]
#        for section in self.course_list:
#            if self.distance(title,section.title)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(title,section.title)
#            elif self.distance(title,section.title)==minimumdist:
#                lowestcourse.append(section)
                
    def sortof(self,col='',dep='',crseNum='',section='',instructor='',title=''):
        self.sorted_queue=[]
        self.queue=self.queue.sort(key=lambda i:self.distance(i.courseNum,crseNum)+self.distance(i.department,dep)+self.distance(i.title,title)+self.distance(i.college,col)+self.distance(i.section,section)+self.distance(i.instructor,instructor))
        for i in self.queue:
            self.sorted_queue.append(self.distance(i.courseNum,crseNum)+self.distance(i.department,dep)+self.distance(i.title,title)+self.distance(i.college,col)+self.distance(i.section,section)+self.distance(i.instructor,instructor))
        plt.scatter(self.sorted_queue)
            
#            if title in section.title:
#                self.queue.append(section)

#    def filter_by_code(self, code, section=None):
#        for section in self.course_list:
#            if section is not None:
#                if code in section.code and section in section.section:
#                    self.queue.append(section)
#            elif code in section.code:
#                self.queue.append(section)

#    def filter_by_instructor(self, instructor):
#        minimumdist=50
#        lowestcourse = []
#        instructor = str(instructor)
#        instructor = instructor.lower()
#        for section in self.course_list:
#            if self.distance(instructor,section.instructor)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(instructor,section.instructor)
#            elif self.distance(instructor,section.instructor)==minimumdist:
#                lowestcourse.append(section)
#                
##            if section.instructor.lower() == instructor:
##                self.queue.append(section)
#    def filter_by_college(self, college):
#        minimumdist=50
#        lowestcourse = []
#        college = str(college)
#        college = college.lower()
#        for section in self.course_list:
#            if self.distance(college,section.college)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(college,section.college)
#            elif self.distance(college,section.college)==minimumdist:
#                lowestcourse.append(section)
#                
#    def filter_by_courseNum(self, courseNum):
#        minimumdist=50
#        lowestcourse = []
#        courseNum = str(courseNum)
#        courseNum = courseNum.lower()
#        for section in self.course_list:
#            if self.distance(courseNum,section.courseNum)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(courseNum,section.courseNum)
#            elif self.distance(courseNum,section.courseNum)==minimumdist:
#                lowestcourse.append(section)
#                
#    def filter_by_department(self, dept):
#        minimumdist=50
#        lowestcourse = []
#        dept = str(dept)
#        dept = dept.lower()
#        for section in self.course_list:
#            if self.distance(dept,section.dept)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(dept,section.dept)
#            elif self.distance(dept,section.dept)==minimumdist:
#                lowestcourse.append(section)
#                
#    def no_monday(self):
#        for section in self.queue:
#            if 'Mon' in section.days:
#                self.queue.remove(section)
#
#    def no_friday(self):
#        for section in self.queue:
#            if 'Fri' in section.days:
#                self.queue.remove(section)
#
#    def clear_q(self):
#        self.queue = []


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

