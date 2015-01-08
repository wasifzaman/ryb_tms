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
	window_.frames["Fourth Frame"].addWidget(early_checkin, (0, 0))

	window_.portr = portr = Photo(repr='portr', path='monet_sm.jpg')
	window_.frames["Third Frame"].addWidget(window_.portr, (0, 0))
	window_.portr.hide()

	window_.frames["Eleventh Frame"].addWidget(window_.attinfo, (0, 0))
	window_.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

	window_.attinfo.editwidget=False
	window_.attinfo.canvas.config(width=695, height=300)

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

			sl = []

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
					sl.append([data_points['bCode'], data_points['firstName'], data_points['lastName'], data_points['chineseName']])


			if len(sl) == 0:
				nos(window_.lang)
				return

			window_.student_id = sl[0][0]
			if len(sl) > 1:
				sl.sort()
				window_.student_id = spicker(sl)
				if not window_.student_id: return

		#reset portrait
		window_.portr.setData('monet_sm.jpg')
		portr2.setData('monet_sm.jpg')

		#temp workaround while table is fixed
		for child in window_.frames["Eleventh Frame"].winfo_children():
			child.destroy()

		window_.attinfo.build(headers=window_.attinfoh, data=[[]])
		window_.frames["Eleventh Frame"].addWidget(window_.attinfo, (0, 0))
		window_.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

		window_.attinfo.editwidget=False
		window_.attinfo.canvas.config(width=695, height=300)

		data_points = database.studentList[window_.student_id].datapoints

		window_.populate(data_points)
		#w2.populate(data_points)

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
		data = False
		for row in data_points['attinfo'][1]:
			if row[0] == date:
				data = row
				#break

		if not data: return
		if len(data[4]) != 0:
			if confirm_overwrite_checkout(window_.lang):
				overwrite = True
			else:
				sby.b.set(sby.rads[0][1]) #reset search bar
				return

		confirm_status = confirm_check_out_time(window_.lang, database)
		if confirm_status == 'manual':
			time_ = time_entry(window_.lang)
			if not time_: return
			data[3] = ''
			data[4] = time_
		elif confirm_status:
			data[3] = time
			data[4] = timeslot
		else:
			sby.b.set(sby.rads[0][1]) #reset search bar
			return

		if datetime.strptime(date + ' ' + data[4], '%m/%d/%Y %I:%M %p') < datetime.strptime(date + ' ' + data[2], '%m/%d/%Y %I:%M %p'):
			checkout_earlier_checkin(window_.lang)
			return

		database.saveData()
		window_.attinfo.setData(
		[data_points['attinfo'][0], [data]]) #display entry being scanned out
		sby.b.set(sby.rads[0][1]) #reset search bar
		window_.attinfo.canvas.yview_moveto(1.0)

	''' 
	** obsolete? **
	def scan_student():
		last_entry = database.studentList[window_.student_id].datapoints['attinfo'][1][-1]
		last_entry_date = last_entry[0]
		last_entry_checkout = False if last_entry[-2] == '' else True
		print(last_entry_checkout)

		if datetime.strptime(last_entry_date, '%m/%d/%Y').date() != datetime.now().today().date():
			no_checkin_today(window_.lang)
			return
		if last_entry_checkout and not confirm_overwrite_checkout(window_.lang): return

		def out():
			time_input = str(hour_input.getData()) + ':' + str(minute_input.getData()) + ' ' + am_pm_input.getData()
			dt = datetime.strptime(datetime.strftime(time_input, '%I:%H %p'), '%I:%H %p')
			window_.time_input_confirmed = dt
			confirm_time.destroy()

		confirm_time = Window(top=True)
		confirm_time.attributes('-fullscreen', False)
		confirm_time.resizable(0, 0)
		confirm_time.geometry('400x200+200+200')
		confirm_time.grab_set()
		confirm_time.focus_set()

		confirm_window = AppWindow(confirm_time.mainFrame)

		hour_input = IntTextbox(text='Hour', lang=window_.lang, repr='h_input')
		minute_input = IntTextbox(text='Minute', lang=window_.lang, repr='m_input')
		am_pm_input = Textbox(text='AM/PM', lang=window_.lang, repr='am_pm')
		rbutton = Buttonbox(text='Confirm', lang=window_.lang, repr='rbutton')

		confirm_window.newFrame("First Frame", (0, 0))

		confirm_window.frames["First Frame"].addWidget(hour_input, (0, 0))
		confirm_window.frames["First Frame"].addWidget(minute_input, (0, 2))
		confirm_window.frames["First Frame"].addWidget(am_pm_input, (0, 4))
		confirm_window.frames["First Frame"].addWidget(rbutton, (1, 0))

		hour_input.label.config(width=4)
		minute_input.label.config(width=6)
		am_pm_input.label.config(width=6)
		hour_input.entry.config(width=3)
		minute_input.entry.config(width=3)
		am_pm_input.entry.config(width=3)
		rbutton.selfframe.grid(columnspan=6, pady=20)

		rbutton.config(cmd=out)

		confirm_time.wait_window()

		try:
			database.scanOutTeacher(window_.student_id, window_.time_input_confirmed)
		except AttributeError:
			return
		print('out', window_.time_input_confirmed)
		database.saveData()
		
		data_points = database.studentList[window_.student_id].datapoints
		window_.attinfo.setData([data_points['attinfo'][0], [data_points['attinfo'][1][-1]]])
		window_.attinfo.canvas.yview_moveto(1.0)

		#reset Scan By to Barcode
		sby.b.set(sby.rads[0][1])
	'''

	def manual_scan():

		print(bCodeNE.getData())
		if (len(bCodeNE.getData())) == 0: return

		dt = date_time_entry(window_.lang)
		if not dt[0]: return
		date = dt[0]
		time = dt[1]

		print(date, time)

		data_points = database.studentList[bCodeNE.getData()].datapoints

		for row in data_points['attinfo'][1]:
			if row[0] == date:
				if len(row[4]) == 0 or confirm_overwrite_checkout(window_.lang):
					if datetime.strptime(date + ' ' + time, '%m/%d/%Y %I:%M %p') < datetime.strptime(date + ' ' + row[2], '%m/%d/%Y %I:%M %p'):
						checkout_earlier_checkin(window_.lang)
						return
					row[3] = ''
					row[4] = time
					database.saveData()
					window_.attinfo.setData(
					[data_points['attinfo'][0], [[date, row[1], row[2], row[3], row[4], row[5]]]])
				return

		entry_not_found(window_.lang, date)

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

#special
	'''
	#w2.spec2 = Labelbox(text='spec', lang=window_.lang, repr='spec')
	#w2.frames["Second Frame"].addWidget(#w2.spec2, (4, 0))
	#w2.spec2.label.config(font=('Verdana', 15), wraplength=200, justify=LEFT)
	#w2.spec2.label.grid(columnspan=2, sticky=N)
	'''

#basic info widgets
	#w2.frames["Second Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)

	window_.attinfo.canvas.config(width=695, height=300)

#set starting lang
	for frame in window_.frames.values():
		for widget in frame.widgets.values():
			if hasattr(widget, 'config'):
				widget.config(lang=window_.lang)