from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(lang, database, top=False, i=0):
	database.loadData()

	top_window_ = Window(top=top)
	top_window_.attributes('-fullscreen', False)
	top_window_.geometry('1280x740+1+1')
	top_window_.resizable(0, 0)
	top_window_.grab_set()
	top_window_.focus_set()
	top_window_.titleFrame.config(height=1)
	top_window_.wintitle.place_forget()

	window_main = AppWindow(top_window_.mainFrame)
	window_1 = AppWindow(top_window_.mainFrame)
	window_2 = AppWindow(top_window_.mainFrame)

	window_main.pack(anchor=N)
	window_2.pack_forget()

	window_1.lang = lang
	window_1.s = i

	window_main.newFrame("Seventh Frame", (1, 0))
	window_1.newFrame("First Frame", (1, 1))
	window_1.newFrame("Second Frame", (1, 2))
	window_1.newFrame("Third Frame", (2, 1))
	window_1.newFrame("Fourth Frame", (2, 1))
	window_1.newFrame("Fifth Frame", (5, 0))
	window_1.newFrame("Sixth Frame", (4, 2))
	window_1.newFrame("Eigth Frame", (3, 2))
	window_1.newFrame("Ninth Frame", (3, 1))
	window_1.newFrame("Tenth Frame", (0, 1))
	window_1.newFrame("Twelfth Frame", (3, 0))
	window_2.newFrame("table_frame", (0, 0))

	sstudent = Buttonbox(text='savestudent', lang=window_1.lang, repr='sstudent')
	bclose = Buttonbox(text='close', lang=window_1.lang, repr='bclose')
	window_1.attinfo = attinfo
	#switch_frame_button = Buttonbox(text='Attendance Table', lang=window_1.lang, repr='showstudentinfo')
	
	window_main.frames["Seventh Frame"].addWidget(portr, (0, 0))
	window_main.frames["Seventh Frame"].addWidget(brwp, (1, 0))
	window_1.frames["First Frame"].addWidget(sinfo, (0, 0))
	window_1.frames["First Frame"].addWidget(firstName, (1, 0))
	window_1.frames["First Frame"].addWidget(lastName, (2, 0))
	window_1.frames["First Frame"].addWidget(chineseName, (3, 0))
	window_1.frames["First Frame"].addWidget(dob, (4, 0))
	window_1.frames["First Frame"].addWidget(cp, (5, 0))
	window_1.frames["First Frame"].addWidget(notes, (8, 0))
	window_1.frames["First Frame"].addWidget(ninfo, (7, 0))
	window_1.frames["Fourth Frame"].addWidget(early_checkin, (0, 0))
	window_1.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	window_1.frames["Eigth Frame"].rowconfigure(0, weight=5, minsize=20)
	window_1.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	window_1.frames["Tenth Frame"].grid(columnspan=5)
	window_1.frames["Eigth Frame"].grid(sticky=S, rowspan=2)
	window_1.frames["Second Frame"].addWidget(ainfo, (0, 3))
	window_1.frames["Second Frame"].addWidget(city, (1, 3))
	window_1.frames["Second Frame"].addWidget(state, (2, 3))
	window_1.frames["Second Frame"].addWidget(zip, (3, 3))
	window_1.frames["Second Frame"].addWidget(email, (4, 3))
	window_1.frames["Second Frame"].addWidget(cPhone, (5, 3))
	window_1.frames["Second Frame"].addWidget(cPhone2, (6, 3))
	window_1.frames["Second Frame"].addWidget(pinfo, (7, 3))
	window_1.frames["Second Frame"].addWidget(bCode, (8, 3))
	window_1.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	window_1.frames["Fifth Frame"].addWidget(bclose, (0, 1))	
	window_2.frames["table_frame"].addWidget(window_1.attinfo, (0, 0))
	window_2.frames["table_frame"].grid(rowspan=3, sticky=W)
	#window_main.frames["Seventh Frame"].addWidget(switch_frame_button, (2, 0))

	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	ainfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	pinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	bCode.label.grid(sticky=N)
	bCode.entry.grid(sticky=N)
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=2)
	notes.config(height=8, width=32)
	brwp.config(lang=window_1.lang)
	window_1.attinfo.config(lang=window_1.lang)
	window_1.attinfo.canvas.config(width=720)
	window_1.attinfo.editwidget = False
	window_1.attinfo.clast = False
	window_1.attinfo.canvas.config(width=700, height=520)
	portr.setData('monet_sm.jpg')
	#switch_frame_button.config(lang=window_1.lang)
	#switch_frame_button.selfframe.grid_forget()

	top_window_.current_shown = 'window_1'
	def switch_frame():
		if top_window_.current_shown == 'window_1':
			window_1.pack_forget()
			window_2.pack(side=LEFT)
			top_window_.current_shown = 'window_2'
			switch_frame_button.button.config(text=window_1.lang['Student Information'])
		elif top_window_.current_shown == 'window_2':
			window_2.pack_forget()
			window_1.pack(side=LEFT)
			top_window_.current_shown = 'window_1'
			switch_frame_button.button.config(text=window_1.lang['Attendance Table'])
		return

	s = database.studentList[i]
	window_1.populate(s.datapoints)
	window_2.populate(s.datapoints)

	tdp = dict(window_1.collect(s.datapoints))

	def collect():
		if not changed():
			top_window_.destroy()
			return
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], window_1.lang): return

		cbcode = bCode.getData()
		if s.datapoints['bCode'] != cbcode:
			if not ase(database.studentList[cbcode].datapoints['firstName'], window_1.lang):
				return
			else:
				dbcode = s.datapoints['bCode']
				database.studentList[cbcode] = s
				del database.studentList[dbcode]

		s.datapoints = dict(list(s.datapoints.items()) + list(window_1.collect(s.datapoints).items()))
		database.saveData()
		top_window_.destroy()

	def changed():
		ctdp = dict(window_1.collect(s.datapoints))
		for key in tdp.keys():
			if ctdp[key] != tdp[key]:
				return True
		return False

	def quit():
		if not changed():
			top_window_.destroy()
		elif ret(window_1.lang):
			top_window_.destroy()
	
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)
	bclose.config(cmd=quit)
	brwp.config(cmd=ppicker)
	#switch_frame_button.config(cmd=switch_frame)

	for frame in window_1.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=window_1.lang)

	top_window_.mainloop()