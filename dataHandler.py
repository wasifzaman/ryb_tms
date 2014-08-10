from datetime import datetime, time, timedelta
import keeper
import pickle
import xlrd
import xlsxwriter
import shutil

#sched feature to add: log all changes

class StudentInfo:

    def __init__(self):
        self.datapoints = {
            #datapoints to of each student
            "lastName": 'N/A',
            "firstName": 'N/A',
            "chineseName": 'N/A',
            "schoolLoc": 'N/A',
            "bCode": 'N/A',
            "sid": 0,
            "dob": '1/1/1900',
            "age": 0,
            "gender": 'N/A',
            "parentName": 'N/A',
            "hPhone": 0,
            "cPhone": 0,
            "cPhone2": 0,
            "pup": 'N/A',
            "addr": 'N/A',
            "state": 'N/A',
            "city": 'N/A',
            "zip": 0,
            "wkdwknd": 'N/A',
            "tpd": '1/1/1900',
            "tpa": 0,
            "tpo": 0,
            "tp": 0,
            "email": 'N/A',
            "sType": 'N/A',
            "cAwarded": 0,
            "cRemaining": 0,
            "findSchool": 'N/A',
            "notes": 'N/A',
            "attinfo": [['Date', 'Check-In Time', 'Class Time'], []],
            "portr": '',
            "ctime": 'N/A',
            "expire": 'N/A',
            "cp": "N"
            }

        self.dpalias = {
            #import aliases
            "Last Name": "lastName",
            "First Name": "firstName",
            "Chinese Name": "chineseName",
            "School Location": "schoolLoc",
            "Barcode": "bCode",
            "Student Number": "sid",
            "Date of Birth": "dob",
            "Age": "age",
            "Gender": "gender",
            "Parent Name": "parentName",
            "Home Phone": "hPhone",
            "Cell Phone": "cPhone",
            "Cell Phone 2": "cPhone2",
            "Pick Up Person": "pup",
            "Address": "addr",
            "State": "state",
            "City": "city",
            "Zip": "zip",
            "Weekday/Weekend": "wkdwknd",
            "Payment Date": "tpd",
            "Payment Method": "Payment Method: ",
            "Payment Amount": "tpa",
            "Payment Owed": "tpo",
            "Email": "email",
            "Service Type": "sType",
            "Classes Awarded": "cAwarded",
            "Classes Remaining": "cRemaining",
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


class StudentDB:

    def __init__(self, **kwargs):
        self.file = kwargs['file']
        
        try:
            #load data on call from self.file
            self.loadData()
        except:
            #create the file in the directory of self.file when not in databse
            self.studentList = {}
            self.saveData()
            print(self.file + " file not found, new file was created")
   
        #cell modifier code for import
        self.fcell = {1: lambda y: str(y), 2: lambda y: int(y), 3: lambda y: (datetime.strptime('1/1/1900', "%m/%d/%Y") + timedelta(days=y-2)).strftime("%m/%d/%Y")}
        
        #time table
        self.timeslot = {(time(9, 15, 0), time(10, 44, 0)): '09:30 AM',
            (time(10, 44, 1), time(12, 14, 0)): '11:00 AM',
            (time(12, 45, 0), time(14, 14, 0)): '01:00 PM',
            (time(14, 14, 1), time(15, 44, 0)): '02:30 PM',
            (time(15, 44, 1), time(17, 14, 0)): '04:00 PM',}
        
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
        #find the time slot for the student according to scan in time
        for timeslot in self.timeslot:
            if time.time() > timeslot[0] and time.time() < timeslot[1]:
                return self.timeslot[timeslot]

        h, m, p = '{:%I}'.format(time), '{:%M}'.format(time), '{:%p}'.format(time)
        m = int(m)

        if m > 40:
            m = '00'
            h = '{:%I}'.format(time + timedelta(hours=1))
        elif m > 10:
            m = '30'
        else:
            m = '00'

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


    def scanStudent(self, barcode, xtra=False):
        try:
            #scan the current student in
            cdt = datetime.now()

            timeslot = self.findTimeSlot(cdt)
            if not timeslot: return
            time = '{:%I:%M %p}'.format(cdt)
            date = '{:%m/%d/%Y}'.format(cdt)

            data = [date, time, timeslot]
            if xtra: data.append(xtra)

            s = self.studentList[barcode].datapoints
            s['attinfo'] = list(s['attinfo'])
            s['attinfo'][0] = ['Date', 'Check-In Time', 'Class Time']
            s['attinfo'][1].append(data)
            s['cRemaining'] -= 1
            if s['cRemaining'] < 0: s['cRemaining'] = 0
        except:
            return print("Student doesn't exist")


    def checkCode(self, barcode):
        #check if barcode exists
        ##bugfix 1
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
        pickle.dump(self.studentList, open(self.file, "wb"))


    def loadData(self):
        self.studentList = pickle.load(open(self.file, "rb"))
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
            dp['attinfo'].append(['Date', 'Check-In Time', 'Class Time'])
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

        workbook = xlsxwriter.Workbook(fpath + '.xlsx')# + 'report_' + sdate.replace('/', '.') + '.xlsx')
        worksheet = workbook.add_worksheet()

        totalondate = {v: [] for k, v in self.timeslot.items()}

        for student in self.studentList.values():
            for att in student.datapoints['attinfo'][1]:
                if att[0] in sdates:
                    for timeslot in totalondate:
                        if att[2][:5] in timeslot or att[2][:4] in timeslot:
                            cintime = att[2] if att[1] == '' else att[1]
                            totalondate[timeslot].append([str(cintime), str(student.datapoints['bCode']), str(student.datapoints['firstName']) + ' ' + str(student.datapoints['lastName']), str(student.datapoints['chineseName'])])

        totals = 0
        for v in totalondate.values():
            totals += len(v)

        worksheet.write(0, 0, 'Total check-ins: ' + str(totals))

        #cleanup
        for k, v in totalondate.items():
            l = []
            for s in v:
                if s not in l:
                    l.append(s)
            totalondate[k] = l

        #to list
        totalondate = [(k, v) for k, v in totalondate.items()]
        totalondate.sort()
        totalondate = totalondate[3:] + totalondate[:3]

        #format
        tformat = workbook.add_format({'bold': True})
        tformat.set_bg_color('#C2FFAD')

        #to excel
        r, c = 2, 0

        for l in totalondate:
            worksheet.write(r, c, l[0], tformat)
            worksheet.write(r, c + 1, str(len(l[1])), tformat)
            worksheet.write(r, c + 2, '', tformat)
            worksheet.write(r, c + 3, '', tformat)
            l[1].sort()
            r += 1
            for t in l[1]:
                worksheet.write(r, 0, t[0])
                worksheet.write(r, 1, t[1])
                worksheet.write(r, 2, t[2])
                worksheet.write(r, 3, t[3])
                r += 1

            worksheet.write(r, c, '')
            r += 1

        worksheet.set_column(0, 0, 5)
        worksheet.set_column(0, 1, 30)
        worksheet.set_column(0, 2, 30)
        worksheet.set_column(0, 3, 30)
        workbook.close()