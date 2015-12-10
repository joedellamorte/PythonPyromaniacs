import course
import matplotlib.pyplot as plt

class search:
    def __init__(self,course_list):
        self.course_list = course_list
        self.queue = self.course_list
        self.coldictionary=['CAS', 'CFA', 'CGS', 'COM', 'ENG', 'EOP', 'GMS', 'GRS', 'GSM', 'KHC', 'LAW', 'MET', 'OTP', 'PDP', 'SAR', 'SED', 'SHA', 'SMG', 'SPH', 'SSW', 'STH']
        self.departments=['AA', 'AH', 'AI', 'AM', 'AN', 'AR', 'AS', 'BB', 'BI', 'CC', 'CG', 'CH', 'CI', 'CL', 'CS', 'EC', 'EI', 'EN', 'ES', 'FY', 'GE', 'HI', 'ID', 'IR', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LJ', 'LK', 'LN', 'LP', 'LR', 'LS', 'LT', 'LX', 'LY', 'LZ', 'MA', 'ME', 'NE', 'NS', 'PH', 'PO', 'PS', 'PY', 'RN', 'SO', 'SY', 'WR', 'WS', 'XL', 'FA', 'MH', 'MP', 'MT', 'MU', 'TH', 'HU', 'RH', 'SS', 'CM', 'CO', 'EM', 'FT', 'JO', 'BE', 'BF', 'EK', 'MS', 'SE', 'CN', 'LL', 'MB', 'AC', 'DS', 'FE', 'HM', 'IS', 'MF', 'MG', 'MK', 'OB', 'OM', 'PL', 'QM', 'SI', 'HC', 'HS', 'RS', 'ST', 'BK', 'JD', 'TX', 'AD', 'AT', 'CJ', 'ML', 'UA', 'AQ', 'DA', 'ER', 'GS', 'HE', 'NT', 'OE', 'PE', 'SK', 'WF', 'HP', 'OT', 'PT', 'SH', 'AP', 'CE', 'CT', 'DE', 'ED', 'LW', 'SC', 'TL', 'HF', 'IM', 'LA', 'SM', 'PM', 'CP', 'ET', 'HB', 'SR', 'SW', 'WP', 'TA', 'TC', 'TF', 'TJ', 'TM', 'TN', 'TO', 'TR', 'TS', 'TT', 'TY', 'TZ']
        self.courseNumbers=['207', '215', '305', '310', '382', '385', '408', '502', '504', '580', '590', '112', '201', '233', '240', '242', '295', '313', '314', '326', '361', '377', '379', '392', '428', '521', '527', '546', '563', '585', '587', '591', '598', '101', '200', '202', '250', '554', '102', '210', '260', '263', '307', '316', '317', '319', '331', '336', '337', '360', '363', '384', '438', '462', '510', '524', '555', '568', '573', '594', '100', '150', '308', '330', '347', '390', '450', '500', '105', '203', '312', '414', '441', '522', '106', '108', '114', '116', '119', '206', '216', '282', '302', '303', '306', '315', '325', '410', '411', '416', '422', '423', '445', '448', '486', '525', '528', '542', '553', '576', '582', '584', '204', '212', '350', '110', '172', '174', '182', '214', '220', '232', '273', '352', '354', '455', '269', '340', '365', '369', '420', '460', '537', '545', '548', '549', '550', '565', '579', '581', '583', '589', '115', '162', '213', '222', '229', '262', '328', '332', '351', '391', '406', '451', '461', '520', '561', '103', '111', '131', '132', '235', '237', '320', '440', '512', '552', '304', '323', '333', '341', '342', '355', '356', '371', '387', '403', '404', '436', '501', '505', '507', '508', '513', '515', '517', '531', '536', '541', '544', '551', '595', '509', '120', '121', '125', '127', '130', '141', '142', '143', '164', '175', '177', '180', '221', '322', '327', '364', '370', '373', '375', '389', '405', '475', '484', '493', '496', '503', '506', '511', '514', '516', '518', '519', '588', '593', '301', '424', '533', '309', '394', '425', '560', '597', '599', '152', '176', '191', '218', '226', '230', '244', '271', '278', '280', '286', '294', '299', '321', '334', '346', '349', '358', '393', '397', '402', '426', '453', '538', '275', '290', '292', '300', '318', '343', '348', '372', '374', '383', '395', '452', '526', '532', '556', '557', '570', '577', '592', '211', '251', '287', '311', '412', '457', '571', '586', '463', '139', '473', '386', '470', '225', '123', '285', '454', '456', '575', '540', '471', '381', '113', '118', '122', '124', '193', '293', '442', '562', '564', '234', '499', '530', '159', '160', '247', '248', '255', '256', '259', '266', '443', '458', '171', '344', '357', '376', '378', '380', '396', '497', '535', '539', '569', '578', '231', '241', '261', '324', '339', '434', '472', '107', '252', '421', '543', '681', '104', '345', '368', '435', '439', '468', '205', '253', '400', '437', '444', '097', '098', '223', '281', '238', '239', '338', '362', '388', '415', '418', '430', '432', '469', '523', '566', '567', '621', '638', '639', '747', '770', '842', '844', '846', '848', '861', '865', '866', '882', '884', '173', '601', '604', '605', '610', '645', '702', '799', '874', '427', '433', '611', '620', '629', '631', '711', '715', '723', '726', '727', '761', '771', '823', '826', '827', '851', '852', '854', '860', '871', '236', '446', '449', '600', '602', '603', '606', '607', '608', '614', '616', '622', '636', '640', '642', '644', '646', '649', '650', '660', '670', '671', '682', '690', '692', '694', '722', '730', '731', '735', '782', '792', '894', '632', '672', '701', '091', '092', '094', '095', '096', '099', '192', '194', '195', '196', '197', '199', '128', '138', '140', '148', '154', '168', '170', '178', '186', '190', '224', '228', '264', '270', '272', '276', '284', '288', '366', '464', '476', '480', '494', '574', '652', '654', '656', '662', '664', '666', '676', '678', '680', '684', '686', '688', '696', '756', '764', '766', '780', '784', '796', '856', '876', '878', '880', '409', '417', '419', '481', '529', '709', '710', '712', '713', '716', '721', '724', '729', '732', '741', '742', '743', '750', '752', '753', '772', '773', '809', '401', '704', '757', '777', '808', '855', '888', '889', '353', '703', '705', '707', '810', '813', '815', '817', '431', '719', '733', '734', '736', '209', '466', '492', '695', '700', '745', '755', '765', '751', '768', '821', '413', '763', '774', '156', '335', '691', '359', '714', '740', '762', '778', '020', '031', '050', '060', '071', '072', '081', '082', '811', '630', '677', '885', '802', '887', '895', '717', '760', '790', '805', '725', '781', '623', '648', '697', '625', '634', '643', '791', '651', '708', '718', '794', '903', '904', '912', '916', '952', '675', '693', '706', '746', '749', '801', '850', '859', '786', '788', '789', '685', '783', '822', '624', '633', '659', '803', '883', '994', '843', '737', '754', '824', '828', '831', '840', '845', '881', '910', '951', '896', '626', '628', '641', '687', '739', '795', '834', '837', '838', '698', '814', '841', '847', '869', '879', '919', '911', '820', '825', '829', '920', '833', '728', '921', '853', '862', '875', '830', '928', '836', '839', '934', '935', '943', '950', '957', '958', '960', '971', '972', '987', '988', '995', '720', '748', '769', '776', '779', '793', '812', '816', '819', '835', '857', '858', '870', '873', '890', '897', '898', '899', '906', '908', '909', '917', '925', '926', '931', '936', '938', '939', '941', '944', '945', '946', '963', '964', '965', '974', '981', '982', '984', '985', '986', '990', '992', '998', '653', '655', '657', '902', '907', '914', '918', '924', '930', '932', '933', '937', '940', '953', '977', '978', '979', '647', '667', '758', '804', '208', '744', '635', '669', '673', '674', '699', '109', '129', '151', '161', '179', '329', '572', '785', '547', '738', '849', '609', '658', '559', '534', '613', '615', '612', '429', '465', '245', '447', '467', '487', '482', '080', '818', '787', '798', '806', '800', '775', '905', '807', '832', '976', '877', '923', '929', '949', '961', '868']
    def distance(self,crse,inpt):
        distance = 0
        beta = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+'
        crse=crse.lower()
        inpt=inpt.lower()
        
        for i in range(len(beta)):
            distance += (inpt.count(beta[i])-crse.count(beta[i]))**2
    
        return float(distance**(1/2))
################################################# *^*  *-*  ^-^ *^*  *-*  ^-^
       #   """June's test code"""
################################################## *^*  *-*  ^-^ *^*  *-*  ^-^
#    def filter_by_title(self, title, courselist):
#        title = str(title)
#        title = title.lower()
#        minimumdist=50
#        lowestcourse=[]
#        for section in courselist:
#            if self.distance(title,section.title)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(title,section.title)
#            elif self.distance(title,section.title)==minimumdist:
#                lowestcourse.append(section)
#        for element in lowestcourse:
#            if element.title == title:
#                return [element]
#        return lowestcourse
    def filter_by_instructor(self, instructor, courselist):
        for x in courselist:
            if instructor.lower() in x.instructor.lower():
                return True
        return False
    def InstructorSched(self,instructor):
        ofTheDead = []
        for joes in self.course_list:
            if not(self.filter_by_instructor(instructor,joes.taking)):
                ofTheDead.append(joes)
        self.course_list = ofTheDead

    def __str__ (self):
        toprint=''
        for i in self.course_list:
            toprint+=str(i)
        return toprint
    def __repr__(self):
        return str(self)
    def __len__(self):
        return len(self.course_list)
#        minimumdist=50
#        lowestcourse = []
#        instructor = str(instructor)
#        instructor = instructor.lower()
#        for section in courselist:
#            if self.distance(instructor,section.instructor)<minimumdist:
#                lowestcourse=[section]
#                minimumdist=self.distance(instructor,section.instructor)
#            elif self.distance(instructor,section.instructor)==minimumdist:
#                lowestcourse.append(section)
#        return lowestcourse
#    def returnCourse(title=None,instr=None): 
#        count = 0
#        if title != None and instr!= None:
#            for ttl in title:
#                if instr.count(ttl) >= count:
#                    count = instr.count(ttl)
#                    course1 = ttl
#            return course1
#        elif title == None and instr != None:
#            return instr[0]
#        elif instr == None and title != None:
#            return title[0]
################################################# *^*  *-*  ^-^ *^*  *-*  ^-^
                      #        """June's test code"""
################################################## *^*  *-*  ^-^ *^*  *-*  ^-^
                
    def finder(self,col='',dep='',crseNum='',section='',instructor='',title=''):
        courselist1=[]
        courselist2=[]
        col=col.lower()
        dep=dep.lower()
        section=section.lower()
        instructor=instructor.lower()
        title=title.lower()
        if not(col.upper() in self.coldictionary):
            return 'error'
            #####################################
            """Call input_window function that tells user 'ERROR' """
            #####################################
        else:
            for i in self.queue:
                if i.college.lower() == col:
                    courselist1.append(i)
        if not(dep.upper() in self.departments):
            return 'error'
        else:
            for i in courselist1:
                if dep == i.department.lower():
                    courselist2.append(i)
        if not(crseNum.upper() in self.courseNumbers):
            return 'error'
        else:
            courselist1=[]
            for i in courselist2:
                if crseNum == i.courseNum:
                    courselist1.append(i)
                    
                ###June's added Code###
#        if not(section.upper() in self.section()):
#            return 'error'
#        else:
#            courselist2=[]
#            for i in courselist1:
#                if section == i.section():
#                    courselist2.append(i)
#        courselist1 = []
#        instrList = filter_by_instructor(instructor,courselist2)
#        ttlList = filter_by_title(title,courselist2)
#        courselist1.append(returnCourse(ttlList,instrList))
#            
#           
        return courselist1
    
                    
    
        
    def sortof(self,col='',dep='',crseNum='',section='',instructor='',title=''):
        self.sorted_queue=[]
        self.queue.sort(key=lambda i:1*self.distance(i.courseNum,crseNum)+1*self.distance(i.department,dep)+self.distance(i.title,title)+1*self.distance(i.college,col)+self.distance(i.section,section)+self.distance(i.instructor,instructor))
        #print(len(self.queue))        
        for i in self.queue:
            self.sorted_queue.append(1*self.distance(i.courseNum,crseNum)+1*self.distance(i.department,dep)+self.distance(i.title,title)+1*self.distance(i.college,col)+self.distance(i.section,section)+self.distance(i.instructor,instructor))
        plt.plot(self.sorted_queue[:])
        print(self.queue[:20])
        plt.show()
            
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
    def __init__(self):
        self.taking=[]


    def add_course(self, new):
        for i in self.taking:
            if new.can_schedule(i):
                pass
            else:
                raise ValueError('could not add course time conflict')
        if new in self.taking:
            raise ValueError('already have that class')
        self.taking += [new]

    def remove_course(self, old):
        while old in self.taking:
            self.taking.remove(old)
    
    def __str__(self):
        strung='--------\n'
        for i in self.taking:
            strung+=str(i)+'\n'
        strung+='--------\n'
        
        return strung
    
    def __repr__(self):
        return str(self)
    def __len__(self):
        return len(self.taking)
        