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
        self.title = title
        self.code = code.split(' ')
        self.section = section
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
    
    def can_schedule(self, other):
        """
        :param other: other Course to compare
        :return: True if course times don't overlap, False if schedule conflict
        """
        other_times = other.dayTime
        for day in self.dayTime:
            if day in other_times:
                if self.dayTime[day][0] in range(other_times[day][0], other_times[day][1]) or \
                                self.dayTime[day][1] in range(other_times[day][0], other_times[day][1]):
                    return False

                elif other_times[day][0] in range(self.dayTime[day][0], self.dayTime[day][1]) or \
                                other_times[day][1] in range(self.dayTime[day][0], self.dayTime[day][1]):
                    return False

                elif self.dayTime[day][0] == other_times[day][0] or self.dayTime[day][1] == other_times[day][1]:
                    return False

                else:
                    return True

    def __str__(self):
        return(str(self.code) + " " + str(self.title) + " " + str(self.days)+ str(self.time))
