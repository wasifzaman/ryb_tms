from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(lang, d, top=False, i=0):

	d.loadData()

	t = Window(top=top)
	t.attributes('-fullscreen', False)
	t.geometry('1280x740+1+1')
	t.resizable(0, 0)
	t.grab_set()
	t.focus_set()
	t.titleFrame.config(height=1)
	t.wintitle.place_forget()

	w = AppWindow(t.mainFrame)
	w2 = AppWindow(t.mainFrame)
	w3 = AppWindow(t.mainFrame)

	w.pack(anchor=N)
	w3.pack_forget()

	w2.lang = lang
	w2.s = i

#frame initialization
	w2.newFrame("First Frame", (1, 1))
	w2.newFrame("Second Frame", (1, 2))
	w2.newFrame("Third Frame", (2, 1))
	w2.newFrame("Fourth Frame", (2, 1))
	w2.newFrame("Fifth Frame", (5, 0))
	w2.newFrame("Sixth Frame", (4, 2))
	w.newFrame("Seventh Frame", (1, 0))
	w2.newFrame("Eigth Frame", (3, 2))
	w2.newFrame("Ninth Frame", (3, 1))
	w2.newFrame("Tenth Frame", (0, 1))
	w2.newFrame("Twelfth Frame", (3, 0))
	#w3.newFrame("Eleventh Frame", (1, 3))

	w3.newFrame("table_frame", (0, 0))

	w2.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w2.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	w2.frames["Tenth Frame"].grid(columnspan=5)
	w2.frames["Eigth Frame"].grid(sticky=S, rowspan=2)
	w2.frames["Eigth Frame"].rowconfigure(0, weight=5, minsize=20)
	#w2.frames["Seventh Frame"].grid(rowspan=2)
	#w2.frames["Eleventh Frame"].grid(sticky=N)
	#w2.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=520)

#student info widgets
	w2.frames["First Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["First Frame"].addWidget(firstName, (1, 0))
	w2.frames["First Frame"].addWidget(lastName, (2, 0))
	w2.frames["First Frame"].addWidget(chineseName, (3, 0))
	w2.frames["First Frame"].addWidget(dob, (4, 0))
	#w2.frames["First Frame"].addWidget(age, (5, 0))
	#w2.frames["First Frame"].addWidget(parentName, (6, 0))
	w2.frames["First Frame"].addWidget(cp, (5, 0))

#address widgets
	w2.frames["Second Frame"].addWidget(ainfo, (0, 3))
	ainfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Second Frame"].addWidget(city, (1, 3))
	w2.frames["Second Frame"].addWidget(state, (2, 3))
	w2.frames["Second Frame"].addWidget(zip, (3, 3))
	w2.frames["Second Frame"].addWidget(email, (4, 3))
	w2.frames["Second Frame"].addWidget(cPhone, (5, 3))
	w2.frames["Second Frame"].addWidget(cPhone2, (6, 3))

#database info widgets
	w2.frames["Second Frame"].addWidget(pinfo, (7, 3))
	pinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Second Frame"].addWidget(bCode, (8, 3))
	bCode.label.grid(sticky=N)
	bCode.entry.grid(sticky=N)
	#w2.frames["Fourth Frame"].addWidget(sid, (2, 0))

#notes widget
	w2.frames["First Frame"].addWidget(ninfo, (7, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["First Frame"].addWidget(notes, (8, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=2)
	notes.config(height=8, width=32)

	w2.frames["Fourth Frame"].addWidget(early_checkin, (0, 0))

	switch_frame_button = Buttonbox(text='Attendance Table', lang=w2.lang, repr='showstudentinfo')
	#show_table = Buttonbox(text='Attendance Table', lang=w2.lang, repr='showtable')

	w.frames["Seventh Frame"].addWidget(switch_frame_button, (2, 0))
	switch_frame_button.selfframe.grid_forget()
	#w2.frames["Seventh Frame"].addWidget(show_table, (3, 0))

	t.current_shown = 'w2'
	def switch_frame():
		if t.current_shown == 'w2':
			w2.pack_forget()
			w3.pack(side=LEFT)
			t.current_shown = 'w3'
			switch_frame_button.button.config(text=w2.lang['Student Information'])
		elif t.current_shown == 'w3':
			w3.pack_forget()
			w2.pack(side=LEFT)
			t.current_shown = 'w2'
			switch_frame_button.button.config(text=w2.lang['Attendance Table'])
		return

	switch_frame_button.config(cmd=switch_frame)


	w.frames["Seventh Frame"].addWidget(portr, (0, 0))

	def save_attendance_():
		#print()
		d.studentList[i].datapoints['attinfo'] = list(w2.attinfo.getData())
		d.saveData()
		return

	w2.attinfo = attinfo
	w3.frames["table_frame"].addWidget(w2.attinfo, (0, 0))
	w3.frames["table_frame"].grid(rowspan=3, sticky=W)
	#w3.frames["table_frame"].addWidget(save_attendance, (1, 0))
	#save_attendance = Buttonbox(text='Save Attendance', lang=w2.lang, repr='saveattendance')
	#save_attendance.config(cmd=save_attendance_)
	w2.attinfo.canvas.config(width=720)
	w2.attinfo.editwidget = False
	w2.attinfo.clast = False
	w2.attinfo.canvas.config(width=700, height=520)

	#reset portrait
	portr.setData('monet_sm.jpg')

	s = d.studentList[i]
	#print(s.datapoints['attinfo'])
	print(s.datapoints['notes'])
	w2.populate(s.datapoints)
	w3.populate(s.datapoints)

	for cell_id, cell_val in w2.attinfo.cells.items():
		if cell_id[0] == 0:
			cur_text = cell_val.label.cget('text')
			cell_val.label.config(text=lang[cur_text])


	tdp = dict(w2.collect(s.datapoints))

	#if amount owed is larger than amount paid, color amount owed in red
	if s.datapoints['tpa'] < s.datapoints['tpo']: tpo.entry.config(bg='red')

	def collect():
		if not changed():
			t.destroy()
			return
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w2.lang): return

		#if the barcode changes
		cbcode = bCode.getData()
		if s.datapoints['bCode'] != cbcode:
			if not ase(d.studentList[cbcode].datapoints['firstName'], w2.lang):
				return
			else:
				dbcode = s.datapoints['bCode']
				d.studentList[cbcode] = s
				del d.studentList[dbcode]

		s.datapoints = dict(list(s.datapoints.items()) + list(w2.collect(s.datapoints).items()))
		d.saveData()

		t.destroy()


	def changed():
		ctdp = dict(w2.collect(s.datapoints))
		#print(ctdp)
		for key in tdp.keys():
			if ctdp[key] != tdp[key]:
				return True
		return False


	def quit():
		if not changed():
			t.destroy()
		elif ret('a', w2.lang):
			t.destroy()


	sstudent = Buttonbox(text='savestudent', lang=w2.lang, repr='sstudent')
	w2.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)

	bclose = Buttonbox(text='close', lang=w2.lang, repr='bclose')
	w2.frames["Fifth Frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=quit)

	w.frames["Seventh Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

	#set starting lang
	for frame in w2.frames.values():
		for widget in frame.widgets.values():
			if hasattr(widget, 'config'):
				widget.config(lang=w2.lang)

	brwp.config(lang=w2.lang)
	switch_frame_button.config(lang=w2.lang)
	w2.attinfo.config(lang=w2.lang)
	
	t.mainloop()