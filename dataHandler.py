from datetime import datetime, time, timedelta
from Crypto.Cipher import AES
from Crypto import Random
from timeclock import *
import keeper
import pickle
import xlrd
import xlsxwriter
import shutil
import math
import os

#sched feature to add: log all changes

class StudentInfo:

    def __init__(self):
        self.datapoints = {
            "lastName": 'N/A', "firstName": 'N/A', "chineseName": 'N/A',
            "schoolLoc": 'N/A', "bCode": 'N/A', "sid": 0,
            "dob": '1/1/1900', "age": 0, "parentName": 'N/A',
            "hPhone": 0, "cPhone": 0, "cPhone2": 0, "pup": 'N/A',
            "addr": 'N/A', "state": 'N/A', "city": 'N/A', "zip": 0,
            "wkdwknd": 'N/A',
            "tpd": '1/1/1900', "tpa": 0, "tpo": 0, "tp": 0,
            "email": 'N/A',
            "sType": 'N/A',
            "cAwarded": 0, "cRemaining": 0,
            "findSchool": 'N/A',
            "notes": 'N/A',
            "attinfo": [['Date', 'Check-In Time', 'Start Time', 'Check-Out Time'], []],
            "portr": '',
            "ctime": 'N/A', "expire": 'N/A', "cp": "N",
            "paid_entries": {},
            "last_payment": False
            #"25s": 0, "50s": 0, "100s": 0, "inrow": 0,
            }

        self.dpalias = {
            #import aliases
            "Last Name": "lastName", "First Name": "firstName", "Chinese Name": "chineseName",
            "School Location": "schoolLoc", "Barcode": "bCode",
            "Student Number": "sid",
            "Date of Birth": "dob", "Age": "age", "Gender": "gender",
            "Parent Name": "parentName", "Home Phone": "hPhone",
            "Cell Phone": "cPhone", "Cell Phone 2": "cPhone2",
            "Pick Up Person": "pup",
            "Address": "addr", "State": "state", "City": "city", "Zip": "zip",
            "Weekday/Weekend": "wkdwknd",
            "Payment Date": "tpd", "Payment Method": "Payment Method: ",
            "Payment Amount": "tpa", "Payment Owed": "tpo",
            "Email": "email",
            "Service Type": "sType",
            "Classes Awarded": "cAwarded", "Classes Remaining": "cRemaining",
            "How did you hear about the school?": "findSchool",
            "Notes": "notes",
            "Already Paid": "tp",
            "Card Printed": "cp",
            "Notes": 'notes'
            }

        self.ordereddp = ['bCode', 'sid', 'firstName', 'lastName', 'chineseName', 'parentName', 'pup', 'gender', 'dob', 'addr', 'state', 'city',\
            'zip', 'cPhone', 'cPhone2', 'hPhone', 'tpd', 'tpa', 'email', 'findSchool', 'cp', 'notes']

        self.revdpalias = {}
        for key, value in self.dpalias.items():
            self.revdpalias[value] = key

        self.ordereddpalias = [self.revdpalias[key] for key in self.ordereddp]

        self.timesheet = timesheet()
        self.timesheet.defineoutformat('%m/%d/%Y', '%I:%M %p')


class StudentDB:

    def __init__(self, **kwargs):
        self.file = kwargs['file']
        self.pwfile = kwargs['pwfile']

        self.iv = b't\xd4\xbc\xee~\xa2\xc2\xc1\x14T\x91\xcfd\x95/\xfc'

        self.studentList = {}
    
        if os.path.isfile(self.pwfile) and os.path.isfile(self.file):
            self.key = open(self.pwfile, 'rb').read()
            self.loadData()
        else:
            #create the file in the directory of self.file when not in databse
            print('creating file')
            self.studentList = {}
            self.saveData()
            print(self.file + " file not found, new file was created")
   
        #cell modifier code for import
        self.fcell = {1: lambda y: str(y), 2: lambda y: int(y), 3: lambda y: (datetime.strptime('1/1/1900', "%m/%d/%Y") + timedelta(days=y-2)).strftime("%m/%d/%Y")}
        
        #time table
        self.timeslot = {(time(6, 30, 0), time(9, 15, 0)): '09:15 AM'}

        self.school = ''
        
        #last barcode
        self.setLast()
        
    
    def setLast(self):
        #set the last barcode
        try:
            t = sorted(self.studentList.keys())[-1]
            self.pre = t[:3]
            self.last = int(t[4:7] + t[8:]) + 1
        except:
            #if barcode could not be parsed, use UNK (unknown)
            self.pre = 'UNK'
            self.last = 0
            pass  


    def formatCode(self):
        #format the new last code
        t = str(self.last)
        while len(t) < 6:
            t = '0' + t
        t = self.pre + '-' + t[:3] + '-' + t[3:]

        return t


    def checkDate(self, barcode):
        #check if student was checked in today
        #currently not in use
        checkedInToday = 0

        today = '{:%m/%d/%Y}'.format(datetime.now())
        attinfo = self.studentList[barcode].datapoints['attinfo'][1]

        for att in attinfo:
            if att[0] == today: checkedInToday += 1

        if checkedInToday > 0: return checkedInToday
        return True


    def findTimeSlot(self, time):
        h, m, p = '{:%I}'.format(time), '{:%M}'.format(time), '{:%p}'.format(time)

        x = int(m)
        if x <= 10:
            x = 0
        elif x > 10 and x <= 40:
            x = 30
        elif x > 40:
            x = 60
        #elif x > 40 and x <= 55:
        #    x = 45
        #elif x > 55:
        #    x = 60

        '''
        if x % 15 >= 7:
            x = 15 * (x // 15) + 15
        elif x % 15 < 7:
            x = (x - x % 15)
        '''

        if x >= 60:
            x = 0
            h = str(int(h) + 1)
        m = str(x) if x >= 10 else '0' + str(x)

        return h + ':' + m + ' ' + p


    def calcAge(self, dob):
        #calculate the age using the birthdate
        try:
            age = datetime.now() - datetime.strptime(dob, "%m/%d/%Y")
        except:
            age = datetime.now() - datetime.strptime(dob, "%m/%d/%y")
        return int(age.total_seconds() / 60 / 60 / 24 / 365)


    def calcExpir(self, start, rem):
        #calculate expiration of classes
        #currently, each class can be completed with 14 days
        return start + timedelta(days=rem*14)


    def calcInRow(self, barcode):
        cdt = datetime.now()

        todaysearly = datetime(cdt.year, cdt.month, cdt.day, 9, 15)

        s = self.studentList[barcode].datapoints

        s['inrow'] += 1
        
        '''
        if cdt < todaysearly:
            s['inrow'] += 1
            if s['inrow'] >= 100:
                s['100s'] += 1
            elif s['inrow'] >= 50:
                s['50s'] += 1
            elif s['inrow'] >= 25:
                s['25s'] += 1
        else:
            s['inrow'] = 0
        '''


    def reset_checkin(self, barcode, value):
        if value == True:
            s = self.studentList[barcode].datapoints
            s['25s'] = 0
            s['50s'] = 0
            s['100s'] = 0
            s['inrow'] = 0
            print('reset')
            return True

        return False


    def scanStudent(self, barcode, xtra=False):
        #try:
        #scan the current student in
        cdt = datetime.now()

        timeslot = self.findTimeSlot(cdt)
        if not timeslot: return
        time = '{:%I:%M %p}'.format(cdt)
        date = '{:%m/%d/%Y}'.format(cdt)

        data = [date, time, timeslot, '', '', self.school]
        print(data)

        s = self.studentList[barcode].datapoints
        s['attinfo'] = list(s['attinfo'])
        s['attinfo'][0] = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
        s['attinfo'][1].append(data)

        self.studentList[barcode].timesheet.clocktimein()
        self.calcInRow(barcode)


    def scanOutTeacher(self, barcode, confirmed_time, xtra=False):
        cdt = datetime.now()

        timeslot = self.findTimeSlot(datetime.strptime(confirmed_time, '%I:%M %p'))
        #if not timeslot: return
        time = '{:%I:%M %p}'.format(cdt)
        #date = '{:%m/%d/%Y}'.format(cdt)

        s = self.studentList[barcode].datapoints
        s['attinfo'] = list(s['attinfo'])
        s['attinfo'][0] = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
        s['attinfo'][1][-1][3] = time
        s['attinfo'][1][-1][4] = timeslot

        self.studentList[barcode].timesheet.clocktimeout()
        #print(self.studentList[barcode].timesheet.printtimesheet())


    def checkCode(self, barcode):
        return barcode in self.studentList


    def addStudent(self, barcode, student):
        #add a student to the database by the barcode
        self.studentList[barcode] = student
        dp = self.studentList[barcode].datapoints
        
        try:
            #calculate the age
            dp['age'] = self.calcAge(dp['dob'])
        except:
            dp['age'] = 0
        
        try:
            #calculate the expiration
            dp['expire'] = self.calcExpir(datetime.now().date(), dp['cAwarded'])
        except:
            pass

        #increment the last barcode
        self.last += 1


    def saveData(self):
        if not hasattr(self, 'key'):
            print('creating key')
            self.key = b'=5<(M8R_P8CJx);^'
            f = open(self.pwfile, 'wb')
            f.write(bytearray(self.key))
            f.close()
            print(self.key)
        cipher = AES.new(self.key, AES.MODE_CFB, self.iv)

        binary_string = pickle.dumps(self.studentList)
        encrypted = cipher.encrypt(binary_string)

        f = open(self.file, 'wb')
        f.write(bytearray(encrypted))
        f.close()

        #print('encrypted', encrypted)


    def loadData(self):
        #key = b'=5<(M8R_P8CJx);^'
        cipher = AES.new(self.key, AES.MODE_CFB, self.iv)

        try:
            f = open(self.file, 'rb')
            print('opened')
        except:
            self.saveData()
            f = open(self.file, 'rb')
            print('created')
        
        decrypted = cipher.decrypt(f.read())
        self.studentList = pickle.loads(decrypted)

        #print('student_list', self.studentList)

        #self.studentList = pickle.loads(cipher.decrypt(f.read()))

        #print(self.studentList)

        self.setLast()


    def format(self, ctype, value):
        #format cell for import
        try:
            return self.fcell[ctype](value)
        except:
            return
            if ctype == 0: print("cell is empty, not added to database")
            else: print("cell could not be formatted")


    def exportxlsx(self, filename):
        if len(self.studentList) == 0: return

        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()

        c = 0

        ss = StudentInfo()
        for dpalias in ss.ordereddpalias:
            worksheet.write(0, c, dpalias)
            c += 1

        r = 1
        for student in self.studentList.values():
            c = 0
            for dp in student.ordereddp:
                worksheet.write(r, c, student.datapoints[dp])
                c += 1
            r += 1

        workbook.close()


    def exporttxlsx(self, filename):
        if len(self.studentList) == 0: return

        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()

        ss = StudentInfo()
        dptd = ['bCode', 'firstName', 'lastName', 'cAwarded']

        c = 0
        for dp in dptd:
            worksheet.write(0, c, ss.revdpalias[dp])
            c += 1

        for i in range(1, 100):
            worksheet.write(0, c, i)
            c += 1

        r = 1
        for student in self.studentList.values():
            c = 0
            for dp in dptd:
                worksheet.write(r, c, student.datapoints[dp])
                c += 1

            if len(student.datapoints['attinfo']) == 2 and student.datapoints['attinfo'][1] == []:
                r += 1
                continue
            
            for att in student.datapoints['attinfo'][1]:
                if len(att) >= 4:
                    worksheet.write(r, c, att[0] + ' ' + att[1] + ' ' + att[2].replace(' ', '') + ' ' + att[3])
                else:
                    worksheet.write(r, c, att[0] + ' ' + att[2].replace(' ', ''))
                c += 1

            r += 1

        workbook.close()


    def importxlsx(self, filename):        
        #import database from xlsx or xls file
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)

        repr, headers = {}, [cell.value for cell in worksheet.row(0)]
        for h in headers:
            repr[headers.index(h)] = StudentInfo().dpalias[h]


        #raw cell data and formatted cell data
        sraw = [worksheet.row(rx) for rx in range(1, worksheet.nrows)]
        sinfo = [[self.format(cell.ctype, cell.value) for cell in row] for row in sraw]

        for info in sinfo:
            newS = StudentInfo()
            for dp in info:
                newS.datapoints[repr[info.index(dp)]] = dp
            newS.datapoints['attinfo'] = list([['Date', 'Time', 'Check-In Time'], []])
            
            try:
                newS.datapoints['age'] = self.calcAge(newS.datapoints['dob'])
            except:
                newS.datapoints['age'] = 0

            try:
                newS.datapoints['tp'] = newS.datapoints['tpa']
            except:
                newS.datapoints['tp'] = 0

            #error-zone: set for school code
            if newS.datapoints['bCode'][:3] != 'FLU' and newS.datapoints['bCode'][:3] != 'BRK': continue
            self.addStudent(newS.datapoints['bCode'], newS)

        self.saveData()


    def importtimexlsx(self, filename):
        #import time data from xlsx or xls
        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)

        repr, headers = {}, [cell.value for cell in worksheet.row(0)][:4]
        for h in headers:
            repr[headers.index(h)] = StudentInfo().dpalias[h]


        sraw = [worksheet.row(rx) for rx in range(1, worksheet.nrows)]
        sinfo = [[self.format(cell.ctype, cell.value) for cell in row] for row in sraw]

        ns, nt = 0, 0

        for info in sinfo:
    
            bCode = info[0]
            try:
                cAward = info[3]
            except:
                cAward = 0
            tdata = info[4:]

            if bCode not in self.studentList: continue

            ftdata = []
            for td in tdata:
                try:
                    dt = td.split(' ')
                    try:
                        date = datetime.strftime(datetime.strptime(dt[0], "%m/%d/%y"), "%m/%d/%Y")
                    except:
                        date = dt[0]
                    time = dt[1]
                except:
                    continue

                if len(dt) >= 4:
                    ftdata.append([date, dt[1] + ' ' + dt[2], dt[3], dt[4]])
                else:
                    ftdata.append([date, '', time])

            dp = self.studentList[bCode].datapoints
            
            dp['cAwarded'] = cAward
            try:
                dp['cRemaining'] = int(cAward) - len(ftdata) if int(cAward) > len(ftdata) else 0
            except:
                dp['cRemaining'] = 0
            dp['attinfo'] = []
            dp['attinfo'].append(['Date', 'Check-In Time', 'Start Time'])
            dp['attinfo'].append(ftdata)
            try:
                if len(ftdata) >= 0:
                    dp['expire'] = self.calcExpir(datetime.strptime(ftdata[0][0], "%m/%d/%y"), cAward)
                else:
                    dp['expire'] = self.calcExpir(datetime.strptime(dp['tpd'], "%m/%d/%Y"), cAward)
            except:
                dp['expire'] = '12/12/9999'
                pass

            ns += 1
            nt += len(ftdata)

        self.saveData()

        #return the amount of students and amount time data added
        return ns, nt


    def exportdb(self, dst):
        shutil.copyfile(self.file, dst)


    def exportreport(self, fpath, sdate):

        if len(self.studentList) == 0: return

        #format sdate
        sdates = [sdate]

        #iterations
        sdsplit = sdate.split('/')
        sdates.append(str(int(sdsplit[0])) + '/' + str(int(sdsplit[1])) + '/' + (sdsplit[2][2:] if len(sdsplit[2]) > 2 else sdsplit[2]))

        date = sdates[1].replace('/', '.')
        workbook = xlsxwriter.Workbook(fpath + '/Teacher Report - ' + self.school + ' ' + date + '.xlsx')
        worksheet = workbook.add_worksheet()

        #totalondate = {v: [] for k, v in self.timeslot.items()}
        #totalondate['other'] = []
        rows = []

        for student in self.studentList.values():
            for att in student.datapoints['attinfo'][1]:
                if att[0] in sdates:
                    first_name = student.datapoints['firstName']
                    last_name = student.datapoints['lastName']
                    barcode_ = student.datapoints['bCode']
                    rows.append([att[2], att[4], first_name, last_name, barcode_])

                    '''
                    cintime = att[2] if att[1] == '' else att[1]
                    if att[2][:5] in timeslot or att[2][:4] in timeslot:
                        totalondate[timeslot].append([str(cintime), str(att[-1]), str(student.datapoints['bCode']), str(student.datapoints['firstName']) + ' ' + str(student.datapoints['lastName']), str(student.datapoints['chineseName'])])
                    else:
                        totalondate['other'].append([str(cintime), str(att[-1]), str(student.datapoints['bCode']), str(student.datapoints['firstName']) + ' ' + str(student.datapoints['lastName']), str(student.datapoints['chineseName'])])
                    '''


        #sorted
        row_indexed = [(att[0], att) for att in rows]
        row_indexed.sort()
        row_sorted = [index_[1] for index_ in row_indexed]

        #format
        tformat = workbook.add_format({'bold': True})
        tformat.set_bg_color('#C2FFAD')

        title_format = workbook.add_format({'bold': True})

        #to excel
        worksheet.set_column(0, 4, 15)
        worksheet.write(0, 0, 'RYB Teacher Attendance Report', title_format)
        worksheet.write(1, 0, 'Total check-ins: ' + str(len(row_sorted)), title_format)
        worksheet.write(2, 0, '日期: ' + str(sdates[0]), title_format)
        worksheet.write(4, 0, '到达时间', tformat) #check-in
        worksheet.write(4, 1, '注销时间', tformat) #check-out
        worksheet.write(4, 2, '名字', tformat) #first_name
        worksheet.write(4, 3, '姓', tformat) #last_name
        worksheet.write(4, 4, '条码号', tformat) #barcode

        r, c = 5, 0

        for row in row_sorted:
            worksheet.write(r, 0, row[0])
            worksheet.write(r, 1, row[1])
            worksheet.write(r, 2, row[2])
            worksheet.write(r, 3, row[3])
            worksheet.write(r, 4, row[4])
            r += 1

        return

    def stringtime_to_decimal(self, string_time):
        (h, m, s) = string_time.split(':')
        return (int(h) * 3600 + int(m) * 60 + int(s)) / 3600


    def print_pay_entries(self, fpath, employee_id, pay_entries, pay_per_hour=1.00, max_hours=False):
        workbook = xlsxwriter.Workbook(fpath + '.xlsx')
        worksheet = workbook.add_worksheet()

        info_headerformat = workbook.add_format({'bold': True, 'bg_color': '#C2FFAD', 'border': 1})
        info_headerformat.set_border_color = '#E0E0E0'

        timesheet_headerformat = workbook.add_format({'bold': True, 'bg_color': '#66FFCC', 'border': 1})
        timesheet_headerformat.set_border_color = '#E0E0E0'

        footer_format = workbook.add_format({'bold': True, 'bg_color': '#EBF5FF', 'border': 1})
        footer_format.set_border_color = '#E0E0E0'

        hours_exceeded_format = workbook.add_format({'bold': True, 'bg_color': 'red', 'border': 1, 'font_color': 'yellow'})
        footer_format.set_border_color = '#E0E0E0'

        paid_alias = self.studentList[employee_id].datapoints['paid_entries']
        paid_alias = dict(list(paid_alias.items()) + list(pay_entries.items()))
        self.studentList[employee_id].datapoints['paid_entries'] = paid_alias
        self.studentList[employee_id].datapoints['last_payment'] = datetime.now().date()

        worksheet.write(0, 0, "发票号码:", info_headerformat)
        worksheet.write(0, 1, "", info_headerformat)
        worksheet.write(0, 2, "", info_headerformat)
        worksheet.write(0, 3, "今天日期", info_headerformat)
        worksheet.write(0, 4, datetime.strftime(datetime.now().date(), '%m/%d/%Y'), info_headerformat)
        
        worksheet.write(1, 0, "", info_headerformat)
        worksheet.write(1, 1, "", info_headerformat)
        worksheet.write(1, 2, "", info_headerformat)
        worksheet.write(1, 3, "", info_headerformat)
        worksheet.write(1, 4, "", info_headerformat)

        worksheet.write(2, 0, self.studentList[employee_id].datapoints['chineseName'], info_headerformat)
        worksheet.write(2, 1, self.studentList[employee_id].datapoints['firstName'], info_headerformat)
        worksheet.write(2, 2, self.studentList[employee_id].datapoints['lastName'], info_headerformat)
        worksheet.write(2, 3, "", info_headerformat)
        worksheet.write(2, 4, self.studentList[employee_id].datapoints['bCode'], info_headerformat)

        worksheet.write(3, 0, '日期', timesheet_headerformat)
        worksheet.write(3, 1, '工作开始时间', timesheet_headerformat)
        worksheet.write(3, 2, '工作结束时间', timesheet_headerformat)
        worksheet.write(3, 3, '支付小时', timesheet_headerformat)
        worksheet.write(3, 4, '工资', timesheet_headerformat)

        #column width
        worksheet.set_column(0, 0, 15)
        worksheet.set_column(1, 4, 20)

        #total hours
        total_time = 0

        r = 4
        for entry in pay_entries.values():

            date = entry[0]
            checkin = datetime.strptime(date + ' ' + entry[2], '%m/%d/%Y %I:%M %p')
            checkout = datetime.strptime(date + ' ' + entry[4], '%m/%d/%Y %I:%M %p')
            time_clocked = checkout - checkin
            decimal_time = self.stringtime_to_decimal(str(time_clocked))
            total_time += decimal_time
            #print()

            worksheet.write(r, 0, entry[0])
            worksheet.write(r, 1, entry[2])
            worksheet.write(r, 2, entry[4])
            worksheet.write(r, 3, str(time_clocked))
            worksheet.write(r, 4, str("%.2f" % float(decimal_time * pay_per_hour)))
            #worksheet.write(r, 4, )

            r += 1


        r += 1

        
        for row in range(r, r+8):
            for cell in range(0, 5):
                worksheet.write(row, cell, ' ', footer_format)

        school_translation = {'Flushing': '法拉盛学校',
                                'Chinatown': '唐人街学校',
                                'Brooklyn': '布鲁克林学校',
                                'Elmhurst': '艾姆赫斯特学校'}

        worksheet.write(r, 3, school_translation[self.school] + ':', footer_format)
        r += 2
        worksheet.write(r, 3, "现金工资:", footer_format)
        r += 1
        worksheet.write(r, 3, "支票工资:", footer_format)
        r += 1
        worksheet.write(r, 3, "支票号码:", footer_format)
        r += 2
        worksheet.write(r, 3, "合计薪水:", footer_format)
        
        if max_hours and max_hours < total_time:
            
            r += 1

            for column in range(0, 5):
                worksheet.write(r, column, ' ', hours_exceeded_format)

            worksheet.write(r, 0, "Hours Exceeded:", hours_exceeded_format)
            worksheet.write(r, 1, str(total_time - max_hours), hours_exceeded_format)

        self.saveData()

        return True