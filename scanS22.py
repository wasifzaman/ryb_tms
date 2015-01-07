from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, database):

	database.loadData()

	window_ = AppWindow(t)
	window_.lang = lang

#attendance table
	window_.attinfo = Table(repr='attinfox', edit=True)
	window_.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time'], language['Check-Out Time']]
	window_.attinfo.build(headers=window_.attinfoh, data=[[]])
	window_.attinfo.clast = '#FF99FF'

#frame initialization
	window_.newFrame("First Frame", (1, 1))
	window_.newFrame("Second Frame", (1, 2))
	window_.newFrame("Third Frame", (2, 2))
	window_.newFrame("Fourth Frame", (2, 1))
	window_.newFrame("Fifth Frame", (5, 0))
	window_.newFrame("Sixth Frame", (4, 2))
	window_.newFrame("Seventh Frame", (1, 0))
	window_.newFrame("Eigth Frame", (3, 1))
	window_.newFrame("Ninth Frame", (3, 2))
	window_.newFrame("Tenth Frame", (0, 1))
	window_.newFrame("Eleventh Frame", (1, 3))

	window_.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	window_.frames["Seventh Frame"].grid(rowspan=2)
	window_.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	window_.frames["Tenth Frame"].grid(columnspan=5)
	window_.frames["Eleventh Frame"].grid(sticky=N)
	window_.frames["Eigth Frame"].grid(sticky=S, rowspan=2)
	window_.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=420)
	window_.frames["Eigth Frame"].rowconfigure(0, weight=5, minsize=20)

#add widget to search for students
	window_.frames["Tenth Frame"].addWidget(sby, (0, 0))

#student info widgets
	window_.frames["First Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'), text=window_.lang['Student information'])
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	window_.frames["First Frame"].addWidget(firstName, (1, 0))
	window_.frames["First Frame"].addWidget(lastName, (2, 0))
	window_.frames["First Frame"].addWidget(chineseName, (3, 0))
	window_.frames["First Frame"].addWidget(dob, (4, 0))
	window_.frames["First Frame"].addWidget(bCodeNE, (7, 0))

#notes widget
	window_.frames["First Frame"].addWidget(ninfo, (8, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	window_.frames["First Frame"].addWidget(notes, (9, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=2)
	notes.config(height=6, width=32)

#early checkin
	window_.frames["Fourth Frame"].addWidget(early_checkin, (0, 0))

	window_.portr = portr = Photo(repr='portr', path='monet_sm.jpg')
	window_.frames["Third Frame"].addWidget(window_.portr, (0, 0))
	window_.portr.hide()

	window_.frames["Eleventh Frame"].addWidget(window_.attinfo, (0, 0))
	window_.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

	window_.attinfo.editwidget=False
	window_.attinfo.canvas.config(width=696, height=300)

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), \
		('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
		('Phone Number', 'phoneNumber')]

	window_.tdp = dict()

#search
	def search_student():
		#try:
		window_.student_id = sby.getData()[1]

		if len(window_.student_id) == 0: return
		if sby.getData()[0] == 'bCode' and window_.student_id not in database.studentList:
			nos(window_.lang)
			return

		window_.tdp = dict()

		print(sby.getData())


		if sby.getData()[0] != 'bCode':
			scan_type = sby.getData()[0]
			scan_value = sby.getData()[1]

			student_list = []

			for s in database.studentList:
				data_points = False
				if scan_type == 'phoneNumber':
					if database.studentList[s].datapoints['hPhone'] == scan_value or \
						database.studentList[s].datapoints['cPhone'] == scan_value or \
						database.studentList[s].datapoints['cPhone2'] == scan_value:
						data_points = database.studentList[s].datapoints

				elif database.studentList[s].datapoints[scan_type] == scan_value:
					data_points = database.studentList[s].datapoints
				
				if data_points:
					student_list.append([data_points['bCode'], data_points['firstName'], data_points['lastName'], data_points['chineseName']])

			if len(student_list) == 0:
				nos(window_.lang)
				return

			window_.student_id = student_list[0][0]
			if len(student_list) > 1:
				student_list.sort()
				window_.student_id = spicker(student_list)
				if not window_.student_id: return

		#reset portrait
		window_.portr.setData('monet_sm.jpg')
		portr2.setData('monet_sm.jpg')

		for child in window_.frames["Eleventh Frame"].winfo_children():
			child.destroy()

		window_.attinfo.build(headers=window_.attinfoh, data=[[]])
		window_.frames["Eleventh Frame"].addWidget(window_.attinfo, (0, 0))
		window_.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

		window_.attinfo.editwidget=False
		window_.attinfo.canvas.config(width=696, height=300)

		data_points = database.studentList[window_.student_id].datapoints

		window_.populate(data_points)

		for cell_id, cell_val in window_.attinfo.cells.items():
			if cell_id[0] == 0:
				cur_text = cell_val.label.cget('text')
				cell_val.label.config(text=lang[cur_text])

		window_.tdp = dict(window_.collect(database.studentList[window_.student_id].datapoints))
		sby.entry.delete(0, END)

		dt = datetime.now()
		date = datetime.strftime(dt, '%m/%d/%Y')
		time = datetime.strftime(dt, '%I:%M %p')
		timeslot = database.findTimeSlot(dt)
		overwrite = False
		if date in [row[0] for row in data_points['attinfo'][1]]:
			if not confirm_overwrite_checkin(window_.lang):
				return
			else: overwrite = True

		confirm_status = confirm_check_in_time(window_.lang, database)
		data = [date, time, timeslot, '', '', database.school]
		if confirm_status == 'manual':
			time_ = time_entry(window_.lang)
			data[1] = ''
			data[2] = time_
			if overwrite:
				data_points['attinfo'][1][-1] = data
			else:
				data_points['attinfo'][1].append(data)
		elif confirm_status:
			if overwrite:
				data_points['attinfo'][1][-1] = data
			else:
				database.scanStudent(window_.student_id)
		else:
			return

		database.saveData()
		window_.attinfo.setData(
		[data_points['attinfo'][0], [data_points['attinfo'][1][-1]]]) #display last entry
		sby.b.set(sby.rads[0][1]) #reset search bar
		window_.attinfo.canvas.yview_moveto(1.0) #scroll to bottom of table

#scan student
	def scan_student():
		database.scanStudent(window_.student_id)
		
		'''
		** early checkin code block **
		cdt = datetime.now()
		earlytime = datetime(cdt.year, cdt.month, cdt.day, 9, 15)
		last_checkin = datetime(cdt.year, cdt.month, cdt.day, 9, 30)
		if cdt > earlytime and cdt < last_checkin:
			if confirm_check_in(window_.student_id, window_.lang):
				database.studentList[window_.student_id].datapoints['attinfo'][1][-1][2] = "09:15 AM"
		'''
		database.saveData()

		att_info = database.studentList[window_.student_id].datapoints['attinfo']
		headers = att_info[0]
		last_check_in = [att_info[1][-1]]
		window_.frames['Eleventh Frame'].widgets['attinfox'].setData([headers, last_check_in])
		
		sby.b.set(sby.rads[0][1]) #reset Scan By to Barcode
		window_.attinfo.canvas.yview_moveto(1.0) #scroll to bottom

	def manual_scan():

		print(bCodeNE.getData())
		if (len(bCodeNE.getData())) == 0: return

		def out():
			time_input = str(hour_input.getData()) + ':' + str(minute_input.getData()) + ' ' + am_pm_input.getData()
			window_.time_input_confirmed = time_input
			window_.date_input = date_input.getData()
			confirm_time.destroy()

		confirm_time = Window(top=True)
		confirm_time.attributes('-fullscreen', False)
		confirm_time.resizable(0, 0)
		confirm_time.geometry('400x200+200+200')
		confirm_time.grab_set()
		confirm_time.focus_set()

		confirm_window = AppWindow(confirm_time.mainFrame)

		date_input = Datebox(text='Check-in date', lang=window_.lang, repr='dateinput')
		hour_input = IntTextbox(text='Hour', lang=window_.lang, repr='h_input')
		minute_input = IntTextbox(text='Minute', lang=window_.lang, repr='m_input')
		am_pm_input = Textbox(text='AM/PM', lang=window_.lang, repr='am_pm')
		return_button = Buttonbox(text='Confirm', lang=window_.lang, repr='rbutton')

		confirm_window.newFrame("First Frame", (0, 0))

		confirm_window.frames["First Frame"].addWidget(date_input, (0, 0))
		confirm_window.frames["First Frame"].addWidget(hour_input, (1, 0))
		confirm_window.frames["First Frame"].addWidget(minute_input, (1, 2))
		confirm_window.frames["First Frame"].addWidget(am_pm_input, (1, 4))
		confirm_window.frames["First Frame"].addWidget(return_button, (2, 0))

		hour_input.label.config(width=4)
		minute_input.label.config(width=6)
		am_pm_input.label.config(width=6)
		hour_input.entry.config(width=3)
		minute_input.entry.config(width=3)
		am_pm_input.entry.config(width=3)
		hour_input.label.grid(sticky=E)
		return_button.selfframe.grid(columnspan=6, pady=20)
		date_input.label.config(width=11)
		date_input.selfframe.grid(columnspan=7, pady=15)

		return_button.config(cmd=out)

		confirm_time.titleFrame.pack_forget()

		confirm_time.wait_window()

		try:
			cdt = datetime.now()
			time = '{:%I:%M %p}'.format(cdt)
			date = window_.date_input
			data = [date, time, window_.time_input_confirmed, '', '', database.school]
			print(data)

			s = database.studentList[bCodeNE.getData()].datapoints
			s['attinfo'] = list(s['attinfo'])
			s['attinfo'][0] = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
			s['attinfo'][1].append(data)
		except AttributeError:
			return
		print('out', window_.time_input_confirmed)
		database.saveData()

		att_info = database.studentList[window_.student_id].datapoints['attinfo']
		headers = att_info[0]
		last_check_in = [att_info[1][-1]]
		print(last_check_in)
		window_.frames['Eleventh Frame'].widgets['attinfox'].setData([headers, last_check_in])	

		sby.b.set(sby.rads[0][1]) #reset Scan By to Barcode
		window_.attinfo.canvas.yview_moveto(1.0) #scroll to bottom

	'''
	** obsolete function? **
	def z(mode=False):
		try:
			scan_student(mode) if cs(database.studentList[window_.student_id].datapoints['firstName'], window_.lang) else False
		except:
			print("error-105")

		print(sby.getData())
	'''

	window_.frames["Tenth Frame"].widgets['sby'].entry.bind("<Return>", lambda x: search_student())

	window_.frames["Tenth Frame"].addWidget(bsearch, (1, 0))
	bsearch.button.config(width=20)
	bsearch.config(cmd=search_student)

#collect and check in button
	def collect():
		try:
			if not changed(): return
			s = database.studentList[window_.student_id]
			if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], window_.lang): return
			s.datapoints = dict(list(s.datapoints.items()) + list(window_.collect(s.datapoints).items()))
			database.saveData()
		except:
			return

	def changed():
		s = database.studentList[window_.student_id]
		ctdp = dict(window_.collect(s.datapoints))
		for key in window_.tdp.keys():
			if ctdp[key] != window_.tdp[key]:
				return True
		return False

	sstudent = Buttonbox(text='savestudent', lang=window_.lang, repr='sstudent')
	window_.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)

	manual_entry_button = Buttonbox(text='Manual Entry', lang=language, repr='manualentrybutton')
	window_.frames["Fifth Frame"].addWidget(manual_entry_button, (0, 1))
	manual_entry_button.config(cmd=lambda: manual_scan())

	firstName2 = Textbox(text="First Name", lang=language, repr='firstName')
	lastName2 = Textbox(text="Last Name", lang=language, repr='lastName')
	#chineseName2 = Textbox(text="Chinese Name", lang=language, repr='chineseName')
	bCode2 = Textbox(text="Barcode", lang=language, repr='bCode')
	#sid2 = IntTextbox(text="Old Student ID", lang=language, repr='sid')
	dob2 = Datebox(text="Date of Birth", lang=language, repr='dob')
	portr2 = Photo(repr='portr', path='monet_sm.jpg')

	#w2.frames["First Frame"].addWidget(portr2, (0, 0))

#basic info widgets
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	window_.attinfo.canvas.config(width=696, height=300)

#set starting lang
	for frame in window_.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=window_.lang)