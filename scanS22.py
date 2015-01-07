from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

	d.loadData()

	w = AppWindow(t)

	#w.bind("<Destroy>", lambda event: t2.destroy)

	w.lang = lang

#attendance table
	w.attinfo = Table(repr='attinfox', edit=True)
	w.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time'], language['Check-Out Time']]
	w.attinfo.build(headers=w.attinfoh, data=[[]])
	w.attinfo.clast = '#FF99FF'

#frame initialization
	w.newFrame("First Frame", (1, 1))
	w.newFrame("Second Frame", (1, 2))
	w.newFrame("Third Frame", (2, 2))
	w.newFrame("Fourth Frame", (2, 1))
	w.newFrame("Fifth Frame", (5, 0))
	w.newFrame("Sixth Frame", (4, 2))
	w.newFrame("Seventh Frame", (1, 0))
	w.newFrame("Eigth Frame", (3, 1))
	w.newFrame("Ninth Frame", (3, 2))
	w.newFrame("Tenth Frame", (0, 1))
	w.newFrame("Eleventh Frame", (1, 3))

	w.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w.frames["Seventh Frame"].grid(rowspan=2)
	w.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	w.frames["Tenth Frame"].grid(columnspan=5)
	w.frames["Eleventh Frame"].grid(sticky=N)
	w.frames["Eigth Frame"].grid(sticky=S, rowspan=2)
	w.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=420)
	w.frames["Eigth Frame"].rowconfigure(0, weight=5, minsize=20)
	#w.frames["First Frame"].grid(columnspan=5)
	#w.frames["Sixth Frame"].grid(rowspan=2, sticky=N)

#add widget to search for students
	w.frames["Tenth Frame"].addWidget(sby, (0, 0))

#student info widgets
	w.frames["First Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'), text=w.lang['Student information'])
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(firstName, (1, 0))
	w.frames["First Frame"].addWidget(lastName, (2, 0))
	w.frames["First Frame"].addWidget(chineseName, (3, 0))
	w.frames["First Frame"].addWidget(dob, (4, 0))
	#w.frames["First Frame"].addWidget(age, (5, 0))
	#w.frames["Second Frame"].addWidget(parentName, (8, 0))
	#w.frames["First Frame"].addWidget(cp, (5, 0))

#address widgets
	#w.frames["Second Frame"].addWidget(ainfo, (0, 0))
	#ainfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	#ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	#w.frames["Second Frame"].addWidget(addr, (3, 0))
	#w.frames["Second Frame"].addWidget(city, (4, 0))
	#w.frames["Second Frame"].addWidget(state, (5, 0))
	#w.frames["Second Frame"].addWidget(zip, (6, 0))
	#w.frames["First Frame"].addWidget(email, (6, 0))

#contact widgets
	'''
	w.frames["Third Frame"].addWidget(cinfo, (0, 0))
	cinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	cinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["Third Frame"].addWidget(pup, (1, 0))
	w.frames["Third Frame"].addWidget(hPhone, (2, 0))
	w.frames["Third Frame"].addWidget(cPhone, (3, 0))
	w.frames["Third Frame"].addWidget(cPhone2, (4, 0))
	'''

#database info widgets
	#w.frames["Fourth Frame"].addWidget(pinfo, (0, 0))
	#pinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	#pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(bCodeNE, (7, 0))

#notes widget
	w.frames["First Frame"].addWidget(ninfo, (8, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(notes, (9, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=2)
	notes.config(height=6, width=32)

#early checkin
	w.frames["Fourth Frame"].addWidget(early_checkin, (0, 0))

#special
	'''
	spec = Labelbox(text='spec', lang=w.lang, repr='spec')
	w.frames["Eigth Frame"].addWidget(spec, (0, 0))
	spec.label.config(font=('Verdana', 15), wraplength=200, justify=LEFT)
	spec.label.grid(columnspan=2, sticky=N)
	'''

	w.portr = portr = Photo(repr='portr', path='monet_sm.jpg')
	w.frames["Third Frame"].addWidget(w.portr, (0, 0))
	w.portr.hide()

	w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

	w.attinfo.editwidget=False
	w.attinfo.canvas.config(width=696, height=300)

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), \
		('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
		('Phone Number', 'phoneNumber')]

	w.tdp = dict()

#search
	def s():
		#try:
		w.s = sby.getData()[1]

		if len(w.s) == 0: return
		if sby.getData()[0] == 'bCode' and w.s not in d.studentList:
			nos(w.lang)
			return

		w.tdp = dict()

		print(sby.getData())


		if sby.getData()[0] != 'bCode':
			sty = sby.getData()[0]
			sdp = sby.getData()[1]

			sl = []

			for s in d.studentList:
				dp = False
				if sty == 'phoneNumber':
					if d.studentList[s].datapoints['hPhone'] == sdp or \
						d.studentList[s].datapoints['cPhone'] == sdp or \
						d.studentList[s].datapoints['cPhone2'] == sdp:
						dp = d.studentList[s].datapoints

				elif d.studentList[s].datapoints[sty] == sdp:
					dp = d.studentList[s].datapoints
				
				if dp:
					sl.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName']])


			if len(sl) == 0:
				nos(w.lang)
				return

			w.s = sl[0][0]
			if len(sl) > 1:
				sl.sort()
				w.s = spicker(sl)
				if not w.s: return

		#reset portrait
		w.portr.setData('monet_sm.jpg')
		portr2.setData('monet_sm.jpg')

		for child in w.frames["Eleventh Frame"].winfo_children():
			child.destroy()

		w.attinfo.build(headers=w.attinfoh, data=[[]])
		w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
		w.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

		w.attinfo.editwidget=False
		w.attinfo.canvas.config(width=696, height=300)

		dp = d.studentList[w.s].datapoints

		w.populate(dp)

		print('lastt attendance', dp['attinfo'][1][-1])
		w.attinfo.setData([dp['attinfo'][0], [dp['attinfo'][1][-1]]])

		for cell_id, cell_val in w.attinfo.cells.items():
			if cell_id[0] == 0:
				cur_text = cell_val.label.cget('text')
				cell_val.label.config(text=lang[cur_text])

		w.tdp = dict(w.collect(d.studentList[w.s].datapoints))
		sby.entry.delete(0, END)

		if confirm_check_in_time(w.lang, d): ss()
		#if cs(d.studentList[w.s].datapoints['firstName'], w.lang): ss()

#scan student
	def ss(mode=False):
		d.scanStudent(w.s, xtra=w.lang['Scan'] if sby.getData()[0] == 'bCode' and not mode else w.lang['Manual'])
		#cdt = datetime.now()
		#earlytime = datetime(cdt.year, cdt.month, cdt.day, 9, 15)
		#last_checkin = datetime(cdt.year, cdt.month, cdt.day, 9, 30)
		#if cdt > earlytime and cdt < last_checkin:
			#if confirm_check_in(w.s, w.lang):
				#d.studentList[w.s].datapoints['attinfo'][1][-1][2] = "09:15 AM"
		d.saveData()

		att_info = d.studentList[w.s].datapoints['attinfo']
		headers = att_info[0]
		last_check_in = [att_info[1][-1]]
		w.frames['Eleventh Frame'].widgets['attinfox'].setData([headers, last_check_in])
		

		sby.b.set(sby.rads[0][1]) #reset Scan By to Barcode
		w.attinfo.canvas.yview_moveto(1.0) #scroll to bottom

	def manual_scan():

		print(bCodeNE.getData())
		if (len(bCodeNE.getData())) == 0: return

		def out():
			time_input = str(hour_input.getData()) + ':' + str(minute_input.getData()) + ' ' + am_pm_input.getData()
			w.time_input_confirmed = time_input
			w.date_input = date_input.getData()
			confirm_time.destroy()

		confirm_time = Window(top=True)
		confirm_time.attributes('-fullscreen', False)
		confirm_time.resizable(0, 0)
		confirm_time.geometry('400x200+200+200')
		confirm_time.grab_set()
		confirm_time.focus_set()

		confirm_window = AppWindow(confirm_time.mainFrame)

		date_input = Datebox(text='Check-in date', lang=w.lang, repr='dateinput')
		hour_input = IntTextbox(text='Hour', lang=w.lang, repr='h_input')
		minute_input = IntTextbox(text='Minute', lang=w.lang, repr='m_input')
		am_pm_input = Textbox(text='AM/PM', lang=w.lang, repr='am_pm')
		rbutton = Buttonbox(text='Confirm', lang=w.lang, repr='rbutton')

		confirm_window.newFrame("First Frame", (0, 0))

		confirm_window.frames["First Frame"].addWidget(date_input, (0, 0))
		confirm_window.frames["First Frame"].addWidget(hour_input, (1, 0))
		confirm_window.frames["First Frame"].addWidget(minute_input, (1, 2))
		confirm_window.frames["First Frame"].addWidget(am_pm_input, (1, 4))
		confirm_window.frames["First Frame"].addWidget(rbutton, (2, 0))

		hour_input.label.config(width=4)
		minute_input.label.config(width=6)
		am_pm_input.label.config(width=6)
		hour_input.entry.config(width=3)
		minute_input.entry.config(width=3)
		am_pm_input.entry.config(width=3)
		hour_input.label.grid(sticky=E)
		rbutton.selfframe.grid(columnspan=6, pady=20)
		date_input.label.config(width=11)
		date_input.selfframe.grid(columnspan=7, pady=15)

		rbutton.config(cmd=out)

		confirm_time.titleFrame.pack_forget()

		confirm_time.wait_window()

		try:
			cdt = datetime.now()
			time = '{:%I:%M %p}'.format(cdt)
			date = w.date_input
			data = [date, time, w.time_input_confirmed, '', '', d.school]
			print(data)

			s = d.studentList[bCodeNE.getData()].datapoints
			s['attinfo'] = list(s['attinfo'])
			s['attinfo'][0] = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
			s['attinfo'][1].append(data)
		except AttributeError:
			return
		print('out', w.time_input_confirmed)
		d.saveData()

		att_info = d.studentList[w.s].datapoints['attinfo']
		headers = att_info[0]
		last_check_in = [att_info[1][-1]]
		print(last_check_in)
		w.frames['Eleventh Frame'].widgets['attinfox'].setData([headers, last_check_in])	

		sby.b.set(sby.rads[0][1]) #reset Scan By to Barcode
		w.attinfo.canvas.yview_moveto(1.0) #scroll to bottom

	def z(mode=False):
		try:
			ss(mode) if cs(d.studentList[w.s].datapoints['firstName'], w.lang) else False
		except:
			print("error-105")


		

		print(sby.getData())

	w.frames["Tenth Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())

	w.frames["Tenth Frame"].addWidget(bsearch, (1, 0))
	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

#collect and check in button
	def collect():
		try:
			if not changed(): return
			s = d.studentList[w.s]
			if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w.lang): return
			s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
			d.saveData()
		except:
			return

	def changed():
		s = d.studentList[w.s]
		ctdp = dict(w.collect(s.datapoints))
		for key in w.tdp.keys():
			if ctdp[key] != w.tdp[key]:
				return True
		return False

	sstudent = Buttonbox(text='savestudent', lang=w.lang, repr='sstudent')
	w.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)

	manual_entry_button = Buttonbox(text='Manual Entry', lang=language, repr='manualentrybutton')
	w.frames["Fifth Frame"].addWidget(manual_entry_button, (0, 1))
	manual_entry_button.config(cmd=lambda: manual_scan())

	firstName2 = Textbox(text="First Name", lang=language, repr='firstName')
	lastName2 = Textbox(text="Last Name", lang=language, repr='lastName')
	#chineseName2 = Textbox(text="Chinese Name", lang=language, repr='chineseName')
	bCode2 = Textbox(text="Barcode", lang=language, repr='bCode')
	#sid2 = IntTextbox(text="Old Student ID", lang=language, repr='sid')
	dob2 = Datebox(text="Date of Birth", lang=language, repr='dob')
	portr2 = Photo(repr='portr', path='monet_sm.jpg')

	#w2.frames["First Frame"].addWidget(portr2, (0, 0))

#special
	'''
	#w2.spec2 = Labelbox(text='spec', lang=w.lang, repr='spec')
	#w2.frames["Second Frame"].addWidget(#w2.spec2, (4, 0))
	#w2.spec2.label.config(font=('Verdana', 15), wraplength=200, justify=LEFT)
	#w2.spec2.label.grid(columnspan=2, sticky=N)
	'''

#basic info widgets
	#w2.frames["Second Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	#w2.frames["Second Frame"].addWidget(firstName2, (1, 0))
	#w2.frames["Second Frame"].addWidget(lastName2, (2, 0))
	#w2.frames["Second Frame"].addWidget(bCode2, (3, 0))
	##w2.frames["Second Frame"].addWidget(chineseName2, (3, 0))

#att table widget
	#w2.frames["Third Frame"].addWidget(w.attinfo, (0, 0))
	#w2.frames["Third Frame"].grid(rowspan=100, sticky=W)

	#w2.attinfo.editwidget=False
	w.attinfo.canvas.config(width=696, height=300)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

#	for frame in #w2.frames.values():
#		for widget in frame.widgets.values():
#			widget.config(lang=w.lang)

	#return t2