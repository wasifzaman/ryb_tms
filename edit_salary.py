from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
import reset_check_in_row


def main(lang, d, top=False, i=0): #i is the id of the student passed in

	d.loadData()

	t = Window(top=top)
	t.attributes('-fullscreen', False)
	t.geometry('1280x720')
	t.resizable(0, 0)
	t.grab_set()
	t.focus_set()

	w = AppWindow(t.mainFrame)

	w.lang = lang
	w.s = i

#frame initialization
	w.newFrame("First Frame", (1, 1))
	w.newFrame("Fifth Frame", (5, 0))
	w.newFrame("Ninth Frame", (3, 1)) #notes
	w.newFrame("Eleventh Frame", (1, 2))


#frame configurations
	w.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	w.frames["Eleventh Frame"].grid(sticky=N)
	w.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=720)


#today's date
	today = TextboxNoEdit(text="today's date", lang=w.lang, repr='today_date')
	last_payment = TextboxNoEdit(text="last payment", lang=w.lang, repr='last_pay_date')
	dollar_per_hour = MoneyTextbox(text="dollar per hour", lang=w.lang, repr='dollar_p_hour')
	w.frames["First Frame"].addWidget(today, (0, 0))
	w.frames["First Frame"].addWidget(last_payment, (1, 0))
	w.frames["First Frame"].addWidget(dollar_per_hour, (2, 0))
	today.config(text=str(datetime.strftime(datetime.now().date(), '%m/%d/%Y')))
	if d.studentList[i].datapoints['last_payment']:
		last_payment.config(text=datetime.strftime(d.studentList[i].datapoints['last_payment'], '%m/%d/%Y'))


#student info widgets
	w.frames["First Frame"].addWidget(sinfo, (3, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	firstName_noedit = TextboxNoEdit(text="First Name", lang=language, repr='firstName')
	lastName_noedit = TextboxNoEdit(text="Last Name", lang=language, repr='lastName')
	chineseName_noedit = TextboxNoEdit(text="Chinese Name", lang=language, repr='chineseName')
	w.frames["First Frame"].addWidget(firstName_noedit, (4, 0))
	w.frames["First Frame"].addWidget(lastName_noedit, (5, 0))
	w.frames["First Frame"].addWidget(chineseName_noedit, (6, 0))

#reset check in row
	b_reset_checkin = Buttonbox(text='resetcheckin', lang=language, repr='bresetcheckin')
	w.frames["Ninth Frame"].addWidget(b_reset_checkin, (2, 1))


#notes widget
	w.frames["Ninth Frame"].addWidget(ninfo, (0, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["Ninth Frame"].addWidget(notes, (1, 0))
	notes.label.grid_forget()
	notes.config(height=8, width=32)


	#w.frames["Seventh Frame"].addWidget(portr, (0, 0))

	w.attinfo = attinfo
	w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Eleventh Frame"].grid(rowspan=3, sticky=W)
	w.attinfo.canvas.config(width=720)
	w.attinfo.editwidget = False
	w.attinfo.clast = False


	#reset portrait
	#portr.setData('monet_sm.jpg')

	s = d.studentList[i]
	#print(s.datapoints['attinfo'])
	print(s.datapoints['notes'])
	w.populate(s.datapoints)

	tdp = dict(w.collect(s.datapoints))

	#if amount owed is larger than amount paid, color amount owed in red
	if s.datapoints['tpa'] < s.datapoints['tpo']: tpo.entry.config(bg='red')

	def reset_checkin():
		reset_confirmation(w.lang, d.reset_checkin(w.s, confirm_reset(w.lang)))

	def collect():
		if not changed():
			t.destroy()
			return
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w.lang): return

		#if the barcode changes
		cbcode = bCode.getData()
		if s.datapoints['bCode'] != cbcode:
			if not ase(d.studentList[cbcode].datapoints['firstName'], w.lang):
				return
			else:
				dbcode = s.datapoints['bCode']
				d.studentList[cbcode] = s
				del d.studentList[dbcode]

		s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
		d.saveData()

		t.destroy()


	def changed():
		ctdp = dict(w.collect(s.datapoints))
		#print(ctdp)
		for key in tdp.keys():
			if ctdp[key] != tdp[key]:
				return True
		return False


	def quit():
		if not changed():
			t.destroy()
		elif ret('a', w.lang):
			t.destroy()


	#bind time sheet cells
	def sTbind(func_pass):
		def fsb(p):
			#function on click on cell
			#place a try here

			first_cell = w.attinfo.cells[p]
			if first_cell.bgcolor == 'tomato' or p[0] == 0: return
			if first_cell.bgcolor == first_cell.altbgcolor:
				pickRow(p)
				w.picked[p[0]] = w.attinfo.data[p[0]-1]
				print(w.picked)
			else:
				unpickRow(p)
				del w.picked[p[0]]
				print(w.picked)


		#bind cells
		#place a try here

		paid_alias = d.studentList[i].datapoints['paid_entries']
		for pos, cell in w.attinfo.cells.items():
			cell.config(bind=('<Button-1>', lambda event, pos=pos: fsb(pos)))
			if pos[0] in paid_alias:
				cell.config(bgcolor='tomato')


	#picked cells
	w.picked = {}

	def pickRow(entry):
		x, y = entry[0], entry[1]
		for cell in w.attinfo.cells.values():
			if cell.pos[0] == x:
				cell.altbgcolor = cell.bgcolor
				cell.config(bgcolor='lightblue')
		return

	def unpickRow(entry):
		x, y = entry[0], entry[1]
		for cell in w.attinfo.cells.values():
			if cell.pos[0] == x:
				cell.config(bgcolor=cell.altbgcolor)
		return

	sTbind(lambda i: pickCell(i))

	#print to file
	def print_to_file():
		if not confirm_print('a', w.lang): return
		file_name = filedialog.asksaveasfilename()
		d.print_pay_entries(file_name, i, w.picked, dollar_per_hour.getData())

	b_print_to_file = Buttonbox(text='print to file', lang=w.lang, repr='print_to_file')
	w.frames["Fifth Frame"].addWidget(b_print_to_file, (0, 0))
	b_print_to_file.selfframe.grid(padx=5)
	b_print_to_file.config(cmd=print_to_file)

	bclose = Buttonbox(text='close', lang=w.lang, repr='bclose')
	w.frames["Fifth Frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=quit)

	b_reset_checkin.config(cmd=reset_checkin)


	#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	
	t.mainloop()