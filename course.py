__author__ = 'NicholasArnold'



class Course:
    def __init__(self, title, code, section, typ, cred, location, days, time,
                 instructor, notes=None):
        """
        :param title: Title of course: 'Eng Compt ++'
        :param course: Code for course in 'ENG EK 128'
        :param section: Section of course: 'A1'
        :param typ: 'Lecture/'Lab'/'Discussion'/'Independent'
        :param cred: Amount of course credits: 4
        :param location: ('Building', 'Room')
        :param days: Days of Week that Class Meets: 'Tue,Thu'
        :param time: Start and Stop time in 12hr format: ('12:00pm','1:30pm')
        :param instructor: Last Name of Professor: 'Carruthers'
        :param notes: Optional notes for course
        :return:
        """
        self.college = code.split()[0]
        self.department = code.split()[1][:2]
        self.courseNum =code.split()[1][2:]
        self.title = title
        #self.code = code.split(' ')
        self.section = section.split()[2]
        self.typ = typ
        self.cred_hrs = cred
        self.location = location
        self.days = days.split(',')
        self.time = time
        self.dayTime = {}
        for day in self.days:
            self.dayTime[day] = (self.to_twenty_four(self.time[0]), self.to_twenty_four(self.time[1]))
        self.instructor = instructor

        self.notes = notes
    def to_twelve(self,time):
        "Converts an integer time value between 0 and 2400 to HR:MIN am/pm format"
        tod = 'am'
        if time >= 1200:
            time -= 1200
            tod = 'pm'
        if time == 0:
            time += 1200
        hour = str(time)[0:-2]
        minute = str(time)[-2:]
        return "{}:{} {}".format(hour, minute, tod)


    def to_twenty_four(self,time):
        """Converts a time given as a string in format 'HR:MINam/pm'
        to an integer between 0 and 2400"""
        hours = 0
        hour_min = time[0:-2].split(':')
        afternoon = time[-2:] == 'pm'
        hours += int(hour_min[0]) * 100 + int(hour_min[1])
        if afternoon:
            hours += 1200
        return hours
    
    def Timeconflict24(self,time1=None,time2=None):
        if time1==None or time2==None:
            return True
        if time1[0] >= time2[0] and time1[0] < time2[1]:
            return False
        elif time1[1] > time2[0] and time1[1] <= time2[1]:
            return False
        return True    
    
    def can_schedule(self, other):
        """
        :param other: other Course to compare
        :return: True if course times don't overlap, False if schedule conflict
        """
        
        for day in self.dayTime.keys():
            if day in self.dayTime.keys() and day in other.dayTime.keys():
                if self.Timeconflict24(self.dayTime[day],other.dayTime[day]):
                    pass
                else:
                    return False
            else:
                pass
        return True

#        isTimeConflict = False
#        sched = [] 
#    
#        if time[0] >= sched[count] and time[0] < sched[count+1]:
#            for days in schedule[count][2]:
#                for check in time[2]:
#                    if days == check:
#                        isTimeConflict = True
#        elif time[1] > sched[count] and time[1] <= sched[count+1]:
#            for days in schedule[count][2]:
#                for check in time[2]:
#                    if days == check:
#                        isTimeConflict = True
#            count += 2
#        return isTimeConflict

    def __str__(self):
        return '~~~' + str(self.dayTime) + ' ' + str(self.typ) + ' '  + str(self.college) + ' ' + str(self.department) + ' ' + str(self.courseNum) + " " + str(self.title) + " " + str(self.instructor)+' '+ str(self.section)+'~~~'

    def __repr__(self):
        return str(self)
