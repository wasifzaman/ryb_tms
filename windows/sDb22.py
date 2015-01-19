import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir) + '\messages windows')

from uiHandler22 import AppWindow
from dataHandler import *
from textbox import Textbox
from button import Buttonbox
from toggle_option import Toggle_option
from tableWidget2 import Table
import editS2


def main(t, lang, d):
	d.loadData()

	window_ = AppWindow(t)

	window_.lang = None

	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Second Frame", (2, 0))
	window_.newFrame("Third Frame", (2, 1))
	window_.newFrame("Fourth Frame", (4, 1))
	window_.newFrame("Fifth Frame", (3, 0))

	window_.frames["Second Frame"].rowconfigure(0, weight=5, minsize=350)
	window_.frames["Second Frame"].columnconfigure(0, weight=5, minsize=630)
	window_.frames["Fifth Frame"].grid(columnspan=3)

	teacher_table = Table(repr='teachertable')
	teacher_table_headers = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
	search_value = Textbox(text="Search", repr=None)
	search_options = Toggle_option(
		options=(('Barcode', 'bCode'),('First Name', 'firstName'), \
		('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
		('Phone Number', 'phoneNumber')), repr=None)
	search_button = Buttonbox(text='Search', lang=window_.lang, repr='searchbutton')
	fward = Buttonbox(text='>> Next 30 >>', lang=window_.lang, repr='>>')
	bward = Buttonbox(text='<< Previous 30 <<', lang=window_.lang, repr='<<')
	blast = Buttonbox(text='>>> Last Page >>>', lang=window_.lang, repr='>>>')

	window_.frames["First Frame"].addWidget(search_value, (0, 0))
	window_.frames["First Frame"].addWidget(search_options, (1, 0))
	window_.frames["First Frame"].addWidget(search_button, (0, 1))	
	window_.frames["Fifth Frame"].addWidget(fward, (1, 1))
	window_.frames["Fifth Frame"].addWidget(bward, (1, 0))
	window_.frames["Fifth Frame"].addWidget(blast, (1, 2))
	window_.frames["Second Frame"].addWidget(teacher_table, (2, 0))

	fward.config(width=17)
	bward.config(width=17)
	blast.config(width=17)
	fward.selfframe.grid(padx=2)
	bward.selfframe.grid(padx=2)
	blast.selfframe.grid(padx=2)

	teacher_list = [[]]
	for teacher in d.studentList.values():
		data_points = teacher.datapoints
		teacher_list[0].append([
			data_points['bCode'],
			data_points['firstName'],
			data_points['lastName'],
			data_points['chineseName'],
			data_points['dob']])

	teacher_list[0].sort()

	if len(teacher_list[0]) > 15:
		teacher_on_page = []
		for teacher in teacher_list[0]:
			teacher_on_page.append(teacher)
			if len(teacher_on_page) >= 15:
				teacher_list.append(teacher_on_page)
				teacher_on_page = []
		teacher_list.append(teacher_on_page)

	if len(teacher_list[-1]) == 0 and len(teacher_list) != 1: teacher_list.pop()

	window_.pNum = 1

	def toPage(p):
		if p == 'next':
			if window_.pNum == len(teacher_list) - 1: return
			window_.pNum = window_.pNum + 1
		elif p == 'previous':
			if window_.pNum == 1: return
			window_.pNum = window_.pNum - 1
		elif p == 'last':
			window_.pNum = len(teacher_list) - 1
		elif p == 'first':
			window_.pNum = 0

		teacher_table.setData(headers=teacher_table_headers, data=teacher_list[window_.pNum])
		teacher_table.canvas.config(width=700, height=350)
		teacher_table.set_width(1, 5, 14)
		def open_edit_window(pos):
			student_id = teacher_table.data[pos[0]-1][0]
			editS2.main(window_.lang, d, i=student_id)
		for pos, cell in teacher_table.cells.items():
			if pos[0] == 0: continue
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: open_edit_window(pos)))

	if len(teacher_list[0]) > 15:
		toPage(1)
		fward.config(cmd=lambda: toPage('next'))
		bward.config(cmd=lambda: toPage('previous'))
		blast.config(cmd=lambda: toPage('last'))
		#first_page.config(cmd=lambda: toPage(0))
	else:
		toPage(0)

	def s():
		window_.s = window_.search_value.getData()

		if search_options.stringvar.get() != 'bCode':
			sty = search_options.stringvar.get()
			sdp = window_.search_value.getData()

			teacher_list = []

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
					teacher_list.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName']])


			if len(teacher_list) == 0:
				student_does_not_exist(window_.lang)
				return

			window_.s = teacher_list[0][0]
			if len(teacher_list) > 1:
				teacher_list.sort()
				window_.s = spicker(teacher_list)
				if not window_.s: return

		editS2.main(window_.lang, d=d, top=True, i=window_.s)

	search_value.entry.bind("<Return>", lambda x: s())
	search_button.config(cmd=s)