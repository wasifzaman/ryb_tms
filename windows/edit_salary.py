import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')

from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
import print_reports


def main(lang, database, markerfile=False, top=False, i=0): #i is the id of the student passed in

	database.loadData()

	top_window_ = Window(top=top)
	top_window_.attributes('-fullscreen', False)
	top_window_.geometry('1280x720')
	top_window_.resizable(0, 0)
	top_window_.grab_set()
	top_window_.focus_set()
	top_window_.titleFrame.pack_forget()

	window_ = AppWindow(top_window_.mainFrame)
	window_.lang = lang
	window_.student_id = i
	window_.picked = {}

	marker = pickle.load(open(markerfile, "rb")) if markerfile else False

	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Ninth Frame", (2, 0)) #notes
	window_.newFrame("Fifth Frame", (3, 0))
	window_.newFrame("Eleventh Frame", (1, 2))

	window_.frames["Fifth Frame"].grid(sticky=S)
	window_.frames["Ninth Frame"].grid(sticky=N+E)
	window_.frames["Eleventh Frame"].grid(rowspan=2, sticky=N)
	window_.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=720)

	today = TextboxNoEdit(text="today's date", lang=window_.lang, repr='today_date')
	firstName_noedit = TextboxNoEdit(text="First Name", lang=language, repr='firstName')
	lastName_noedit = TextboxNoEdit(text="Last Name", lang=language, repr='lastName')
	chineseName_noedit = TextboxNoEdit(text="Chinese Name", lang=language, repr='chineseName')
	last_payment = TextboxNoEdit(text="last payment", lang=window_.lang, repr='last_pay_date')
	dollar_per_hour = MoneyTextbox(text="dollar per hour", lang=window_.lang, repr='dollar_p_hour')
	max_hours = IntTextbox(text="max hours", lang=window_.lang, repr='max_hours')
	b_print_to_file = Buttonbox(text='print to file', lang=window_.lang, repr='print_to_file')
	bclose = Buttonbox(text='close', lang=window_.lang, repr='bclose')
	window_.attinfo = attinfo
	#b_reset_checkin = Buttonbox(text='resetcheckin', lang=language, repr='bresetcheckin')

	window_.frames["First Frame"].addWidget(today, (0, 0))
	window_.frames["First Frame"].addWidget(last_payment, (1, 0))
	window_.frames["First Frame"].addWidget(dollar_per_hour, (2, 0))
	window_.frames["First Frame"].addWidget(sinfo, (4, 0))
	window_.frames["First Frame"].addWidget(firstName_noedit, (5, 0))
	window_.frames["First Frame"].addWidget(lastName_noedit, (6, 0))
	window_.frames["First Frame"].addWidget(chineseName_noedit, (7, 0))
	window_.frames["Fifth Frame"].addWidget(b_print_to_file, (0, 0))
	window_.frames["Fifth Frame"].addWidget(bclose, (1, 0))
	window_.frames["Ninth Frame"].addWidget(ninfo, (0, 0))
	window_.frames["Ninth Frame"].addWidget(notes, (1, 0))
	window_.frames["Eleventh Frame"].addWidget(window_.attinfo, (0, 0))
	window_.frames["Eleventh Frame"].grid(rowspan=3, sticky=W)
	#window_.frames["Ninth Frame"].addWidget(b_reset_checkin, (2, 1))

	today.config(text=str(datetime.strftime(datetime.now().date(), '%m/%d/%Y')))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	notes.label.grid_forget()
	notes.config(height=8, width=32)
	b_print_to_file.selfframe.grid(padx=5)
	if database.studentList[i].datapoints['last_payment']:
		last_payment.config(text=datetime.strftime(database.studentList[i].datapoints['last_payment'], '%m/%d/%Y'))
	
	window_.attinfo.canvas.config(width=720, height=500)
	window_.attinfo.editwidget = False
	window_.attinfo.clast = False

	student_ = database.studentList[i]
	window_.populate(student_.datapoints)

	def pick_cell(p, i):
		first_cell = window_.attinfo.cells[p]
		if p[0] == 0: return
		if marker and first_cell.bgcolor in marker[i]['color_set']:
			print('already printed')
			pickRow(p, True)
			window_.picked[p[0]] = window_.attinfo.data[p[0]-1]
		elif first_cell.bgcolor == first_cell.altbgcolor:
			print('picked!')
			pickRow(p)
			window_.picked[p[0]] = window_.attinfo.data[p[0]-1]
			print(window_.picked)
		else:
			print('unpicked!')
			unpickRow(p)
			del window_.picked[p[0]]
			print(window_.picked)

	for pos, cell in window_.attinfo.cells.items():
		cell.config(bind=('<Button-1>', lambda event, pos=pos: pick_cell(pos, i)))
		if marker and (pos[0] in marker[i]['paid_set']):
			cell.config(bgcolor=marker[i]['row_color'][pos[0]])

	def pickRow(entry, printed=False):
		x, y = entry[0], entry[1]
		for cell in window_.attinfo.cells.values():
			if cell.pos[0] == x:
				cell.altbgcolor = cell.bgcolor
				if not printed:
					cell.config(bgcolor='lightblue')
				else:
					cell.config(bgcolor='pink')

	def unpickRow(entry):
		x, y = entry[0], entry[1]
		for cell in window_.attinfo.cells.values():
			if cell.pos[0] == x:
				cell.config(bgcolor=cell.altbgcolor)

	def print_to_file():
		if not confirm_print(window_.lang): return
		file_path = filedialog.askdirectory()
		today = datetime.now()
		date = today.strftime('%m.%d.%y')
		time = today.strftime('%I.%M.%p')
		file_name = file_path + '/Salary Report ' + database.school + ' ' + date + ' ' + time + '.xlsx'
		printed = print_reports.print_pay_entries(database, file_name, i, window_.picked, dollar_per_hour.getData(), False) #false is for max_hours
		if markerfile:
			if i not in marker:
				marker[i] = {}
				marker[i]['paid_set'] = window_.picked
				marker[i]['color_set'] = ['tomato', 'cornflowerblue']
				marker[i]['current_color'] = 0
				marker[i]['row_color'] = {}
				for row_num in window_.picked:
					marker[i]['row_color'][row_num] = marker[i]['color_set'][marker[i]['current_color']]
			else:
				print(i, ' in marker file, appending..')
				marker[i]['current_color'] = (marker[i]['current_color'] + 1) % len(marker[i]['color_set'])
				print(marker[i]['current_color'])
				for row_num in window_.picked:
					marker[i]['row_color'][row_num] = marker[i]['color_set'][marker[i]['current_color']]
				marker[i]['paid_set'].update(window_.picked)
			print(marker)
			pickle.dump(marker, open(markerfile, "wb"))
		if printed:
			print_succesful(window_.lang)
			top_window_.destroy()

	for frame in window_.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=window_.lang)

	b_print_to_file.config(cmd=print_to_file)
	bclose.config(cmd=top_window_.destroy)
	#b_reset_checkin.config(cmd=reset_checkin)
	
	top_window_.mainloop()