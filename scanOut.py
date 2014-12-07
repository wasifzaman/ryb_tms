from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

	d.loadData()

	w = AppWindow(t)

	w.bind("<Destroy>", lambda event: t2.destroy)

	w.lang = lang

#attendance table
	w.attinfo = Table(repr='attinfo', edit=True)
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

#payment widgets
	'''
	w.frames["Fourth Frame"].addWidget(tpd, (2, 0))
	w.frames["Fourth Frame"].addWidget(tpa, (3, 0))
	w.frames["Fourth Frame"].addWidget(tp, (4, 0))
	w.frames["Fourth Frame"].addWidget(tpo, (5, 0))
	'''

#class widget
	'''
	w.frames["Fourth Frame"].addWidget(sType, (6, 0))
	w.frames["Fourth Frame"].addWidget(cAwarded, (7, 0))
	w.frames["Fourth Frame"].addWidget(cRemaining, (8, 0))
	w.frames["Fourth Frame"].addWidget(ctime, (9, 0))
	'''

#notes widget
	w.frames["First Frame"].addWidget(ninfo, (8, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(notes, (9, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=2)
	notes.config(height=6, width=32)

#early checkin
	'''
	w.frames["Fourth Frame"].addWidget(checkin25, (0, 2))
	w.frames["Fourth Frame"].addWidget(checkin50, (0, 4))
	w.frames["Fourth Frame"].addWidget(checkin100, (0, 6))

	checkin25.label.config(width=4)
	checkin50.label.config(width=4)
	checkin100.label.config(width=4)

	checkin25.entry.config(width=3)
	checkin50.entry.config(width=3)
	checkin100.entry.config(width=3)
	'''
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

#renew classes button
	'''
	def renC():
		try:
			d.studentList[w.s]
		except:
			return

		r = renew(w.lang)
		if r == 0: return
		dp = d.studentList[w.s].datapoints
		dp['cRemaining'] = dp['cRemaining'] + r
		dp['cAwarded'] = dp['cAwarded'] + r
		dp['expire'] = d.calcExpir(datetime.now().date(), r)
		spec.setData("")
		#w2.spec2.setData("")
		cRemaining.setData(dp['cRemaining'])
		cAwarded.setData(dp['cAwarded'])
		tpa.setData(0)
		tpo.setData(0)
		tp.setData(0)

	w.ren = Buttonbox(text='Renew classes', lang=w.lang, repr='ren')
	w.frames["Fourth Frame"].addWidget(w.ren, (10, 1))
	w.ren.selfframe.grid(sticky=S)
	w.ren.button.config(width=20)
	w.ren.config(cmd=renC)
	'''

	w.attinfo.editwidget=False
	w.attinfo.canvas.config(width=695, height=300)

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

		#reset classes rem
		#spec.setData("")
		##w2.spec2.setData("")

		#temp workaround while table is fixed
		for child in w.frames["Eleventh Frame"].winfo_children():
			child.destroy()

		w.attinfo.build(headers=w.attinfoh, data=[[]])
		w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
		w.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

		w.attinfo.editwidget=False
		w.attinfo.canvas.config(width=695, height=300)


		#temp workaround while table is fixed
		#for child in #w2.frames["Third Frame"].winfo_children():
		#	child.destroy()

		#w2.attinfo.build(headers=#w2.attinfoh, data=[[]])
		#w2.frames["Third Frame"].addWidget(#w2.attinfo, (0, 0))
		#w2.frames["Third Frame"].grid(rowspan=100, sticky=W)

		#w2.attinfo.editwidget=False
		#w2.attinfo.canvas.config(width=695, height=500)
		#
		dp = d.studentList[w.s].datapoints

		w.populate(dp)
		#w2.populate(dp)

		w.tdp = dict(w.collect(d.studentList[w.s].datapoints))

		#if amount owed is larger than amount paid, color amount owed in red
		#if dp['tpa'] < dp['tpo']: tpo.entry.config(bg='red')
		#else: tpo.entry.config(bg='white')

		sby.entry.delete(0, END)

		'''
			##w2.spec2.show()
			##w2.spec2.setData(w.lang['Classes remaining for this student'] + ': ' + str(d.studentList[w.s].datapoints['cRemaining']))
			##w2.spec2.label.config(fg='#0000B8', font=('Verdana', 15))

			#try:
			#	if datetime.now().date() > d.studentList[w.s].datapoints['expire']:
			#		spec.show()
			#		spec.setData(w.lang['Membership Expired'])
			#		spec.label.config(fg='red', font=('Verdana', 15))
			#except:
			#	pass

			#if d.studentList[w.s].datapoints['cRemaining'] == 0:
			#	spec.show()
			#	spec.setData(w.lang['Classes remaining for this student'] + ': ' + str(d.studentList[w.s].datapoints['cRemaining']))
			#	spec.label.config(fg='red', font=('Verdana', 15))				
			#	noc(w.lang)
			#	sby.b.set(sby.rads[0][1])
			#	return
		'''

		conf_check_out_method = confirm_check_out_time(w.lang)
		if conf_check_out_method == True and conf_check_out_method != 'cancel':
			last_entry = d.studentList[w.s].datapoints['attinfo'][1][-1]
			last_entry_date = last_entry[0]
			last_entry_checkout = False if last_entry[-2] == '' else True
			print(last_entry_checkout)

			if datetime.strptime(last_entry_date, '%m/%d/%Y').date() != datetime.now().today().date():
				no_checkin_today(w.lang)
				return
			if last_entry_checkout and not confirm_overwrite_checkout('a', w.lang): return

			w.time_input_confirmed = datetime.now().strftime('%I:%M %p')
			d.scanOutTeacher(w.s, w.time_input_confirmed)

			w.frames['Eleventh Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])
			#w2.frames['Third Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])

			'''
			checkin25.setData(d.studentList[w.s].datapoints['25s'])
			checkin50.setData(d.studentList[w.s].datapoints['50s'])
			checkin100.setData(d.studentList[w.s].datapoints['100s'])
			'''

			#auto scroll to last position
			w.attinfo.canvas.yview_moveto(1.0)
			#w2.attinfo.canvas.yview_moveto(1.0)

			#reset Scan By to Barcode
			sby.b.set(sby.rads[0][1])

			d.saveData()

			return
		elif conf_check_out_method == 'cancel': return
		else:
			ss()

		#if csout(d.studentList[w.s].datapoints['firstName'], w.lang): ss()
		#except:
		#	nos(w.lang)
		#	pass


#scan student
	def ss(mode=False):
		#print report prompt
		last_entry = d.studentList[w.s].datapoints['attinfo'][1][-1]
		last_entry_date = last_entry[0]
		last_entry_checkout = False if last_entry[-2] == '' else True
		print(last_entry_checkout)

		if datetime.strptime(last_entry_date, '%m/%d/%Y').date() != datetime.now().today().date():
			no_checkin_today(w.lang)
			return
		if last_entry_checkout and not confirm_overwrite_checkout('a', w.lang): return




		def out():
			time_input = str(hour_input.getData()) + ':' + str(minute_input.getData()) + ' ' + am_pm_input.getData()
			w.time_input_confirmed = time_input
			confirm_time.destroy()

		confirm_time = Window(top=True)
		confirm_time.attributes('-fullscreen', False)
		confirm_time.resizable(0, 0)
		confirm_time.geometry('400x200+200+200')
		confirm_time.grab_set()
		confirm_time.focus_set()

		confirm_window = AppWindow(confirm_time.mainFrame)

		hour_input = IntTextbox(text='Hour', lang=w.lang, repr='h_input')
		minute_input = IntTextbox(text='Minute', lang=w.lang, repr='m_input')
		am_pm_input = Textbox(text='AM/PM', lang=w.lang, repr='am_pm')
		rbutton = Buttonbox(text='Confirm', lang=w.lang, repr='rbutton')

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


		d.scanOutTeacher(w.s, w.time_input_confirmed)#, xtra=w.lang['Scan'] if sby.getData()[0] == 'bCode' and not mode else w.lang['Manual'])
		print('out', w.time_input_confirmed)
		d.saveData()
		
		#show alert if classes remaining is less than 2
		#cRem = d.studentList[w.s].datapoints['cRemaining']
		#expir = d.studentList[w.s].datapoints['expire']
		#if cRem <= 2:
		#	spec.show()
		#	spec.setData(w.lang['Classes remaining for this student'] + ': ' + str(cRem))
		#	spec.label.config(fg='red', font=('Verdana', 15))
		#else:
		#	spec.setData("")
		#	#hide, show will work better once window size is set
		#	pass

		#print(expir > datetime.now().date())
		#try:
		#	if datetime.now().date() > expir:
		#		spec.show()
		#		spec.setData(w.lang['Membership Expired'])
		#		spec.label.config(fg='red', font=('Verdana', 15))
		#except:
		#	pass

		#spec.setData(w.lang['Classes remaining for this student'] + ': ' + str(cRem))

		##w2.spec2.show()
		##w2.spec2.setData(w.lang['Classes remaining for this student'] + ': ' + str(cRem))
		##w2.spec2.label.config(fg='#0000B8', font=('Verdana', 15))

		#update cRemaining
		#cRemaining.setData(str(cRem))

		w.frames['Eleventh Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])
		#w2.frames['Third Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])

		'''
		checkin25.setData(d.studentList[w.s].datapoints['25s'])
		checkin50.setData(d.studentList[w.s].datapoints['50s'])
		checkin100.setData(d.studentList[w.s].datapoints['100s'])
		'''

		#auto scroll to last position
		w.attinfo.canvas.yview_moveto(1.0)
		#w2.attinfo.canvas.yview_moveto(1.0)

		#reset Scan By to Barcode
		sby.b.set(sby.rads[0][1])


	def z(mode=False):
		try:
			conf_check_out_method = confirm_check_out_time(w.lang)
			if conf_check_out_method == True and conf_check_out_method != 'cancel':

				last_entry = d.studentList[w.s].datapoints['attinfo'][1][-1]
				last_entry_date = last_entry[0]
				last_entry_checkout = False if last_entry[-2] == '' else True
				print(last_entry_checkout)

				if datetime.strptime(last_entry_date, '%m/%d/%Y').date() != datetime.now().today().date():
					no_checkin_today(w.lang)
					return
				if last_entry_checkout and not confirm_overwrite_checkout('a', w.lang): return
				
				w.time_input_confirmed = datetime.now().strftime('%I:%M %p')
				d.scanOutTeacher(w.s, w.time_input_confirmed)

				w.frames['Eleventh Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])
				#w2.frames['Third Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])

				'''
				checkin25.setData(d.studentList[w.s].datapoints['25s'])
				checkin50.setData(d.studentList[w.s].datapoints['50s'])
				checkin100.setData(d.studentList[w.s].datapoints['100s'])
				'''

				#auto scroll to last position
				w.attinfo.canvas.yview_moveto(1.0)
				#w2.attinfo.canvas.yview_moveto(1.0)

				#reset Scan By to Barcode
				sby.b.set(sby.rads[0][1])

				d.saveData()

				return
			elif conf_check_out_method == 'cancel': return
			else:
				ss()
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

	#bcheck = Buttonbox(text='Scan Out Teacher', lang=language, repr='bcheck')
	#w.frames["Fifth Frame"].addWidget(bcheck, (0, 1))
	#bcheck.config(cmd=lambda: z(True))






#t2 window
	t2 = Window(top=True)
	t2.attributes('-fullscreen', False)
	t2.attributes('-alpha', 0.0)
	t2.geometry('1200x800')

#remove close button function
	t2.protocol('WM_DELETE_WINDOW', lambda: False)

#set minimum height
	t2.update_idletasks()
	t2.after_idle(lambda: t2.minsize(t2.winfo_width(), t2.winfo_height()))

	#w2 = AppWindow(t2.mainFrame)

	#w2.lang = lang

#attendance table
	#w2.attinfo = Table(repr='attinfo', edit=True)
	#w2.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time'], language['Check-Out Time']]
	#w2.attinfo.build(headers=#w2.attinfoh, data=[[]])
	#w2.attinfo.clast = '#FF99FF'

#frame initialization
	#w2.newFrame("First Frame", (0, 0))
	#w2.newFrame("Second Frame", (1, 0))
	#w2.newFrame("Third Frame", (0, 1))

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
	w.attinfo.canvas.config(width=695, height=300)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

#	for frame in #w2.frames.values():
#		for widget in frame.widgets.values():
#			widget.config(lang=w.lang)

	return t2