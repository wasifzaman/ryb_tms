from uiHandler22 import *
import edit_salary
from dataHandler import *
from preBuilts2 import *
from student_picker import multiple_match


def main(parent_frame, lang, database, markerfile):

	if os.path.isfile(markerfile):
		print('found', markerfile)
	else:
		markerfile = False
		print('not found', markerfile)

	database.loadData()

	window_ = AppWindow(parent_frame)

	window_.lang = lang

#sT
	teacher_table = Table(repr='stable', edit=False)
	teacher_table_headers = [lang[text] for text in ['Barcode', 'First Name', 'Last Name', 'Chinese Name', 'Date of Birth']]

	def sTbind(func_pass):
		def fsb(p):
			student_id = teacher_table.data[p[0]-1][0]
			func_pass(student_id)
		for pos, cell in teacher_table.cells.items():
			if pos[0] == 0: continue
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))

#frame initialization
	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Second Frame", (2, 0))
	window_.newFrame("Third Frame", (2, 1))
	window_.newFrame("Fourth Frame", (4, 1))
	window_.newFrame("Fifth Frame", (3, 0))

	window_.frames["Second Frame"].rowconfigure(0, weight=5, minsize=470)
	window_.frames["Second Frame"].columnconfigure(0, weight=5, minsize=630)

	window_.frames["Fifth Frame"].grid(columnspan=3)

#widget for scan
	window_.sby = Picker(repr='sby', text=window_.lang['Search By'], rads=[(window_.lang['Barcode'], 'bCode'), \
		(window_.lang['First Name'], 'firstName'), \
		(window_.lang['Last Name'], 'lastName'), \
		(window_.lang['Chinese Name'], 'chineseName')])

	window_.frames["First Frame"].addWidget(window_.sby, (0, 0))
	window_.frames["First Frame"].addWidget(bsearch, (1, 0))
	
#buttons for scrolling db
	fward = Buttonbox(text='>> Next 30 >>', lang=window_.lang, repr='>>')
	bward = Buttonbox(text='<< Previous 30 <<', lang=window_.lang, repr='<<')
	blast = Buttonbox(text='>>> Last Page >>>', lang=window_.lang, repr='>>>')
	window_.frames["Fifth Frame"].addWidget(fward, (1, 1))
	window_.frames["Fifth Frame"].addWidget(bward, (1, 0))
	window_.frames["Fifth Frame"].addWidget(blast, (1, 2))

	fward.config(width=17)
	bward.config(width=17)
	blast.config(width=17)

	fward.selfframe.grid(padx=2)
	bward.selfframe.grid(padx=2)
	blast.selfframe.grid(padx=2)

	window_.frames["Second Frame"].addWidget(teacher_table, (2, 0))
	teacher_table.canvas.config(width=700, height=480)

	#sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), \
	#	('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
	#	('Phone Number', 'phoneNumber')]

	sL = [[]]
	for s in database.studentList.values():
		dp = s.datapoints
		sL[0].append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL[0].sort()

#create pages
	#print(len(sL[0]))
	if len(sL[0]) > 30:
		l = []
		for s in sL[0]:
			l.append(s)
			if len(l) >= 30:
				sL.append(l)
				l = []
		sL.append(l)

	#if last page is blank (if num students is multiple of 30)
	if len(sL[-1]) == 0 and len(sL) != 1: sL.pop()

	window_.pNum = 1

		
	def toPage(p):
		teacher_table.canvas.config(width=700, height=450)
		teacher_table.setData(
			headers=teacher_table_headers,
			data=sL[p])
		teacher_table.set_width(2, 5, 14)

		sTbind(lambda student_id: edit_salary.main(window_.lang, database=database, markerfile=markerfile, top=True, student_id=student_id))

	def f():
		if window_.pNum == len(sL) - 1: return
		toPage(window_.pNum + 1)
		window_.pNum = window_.pNum + 1
		
	def b():
		if window_.pNum == 1: return
		toPage(window_.pNum - 1)
		window_.pNum = window_.pNum - 1

	def l():
		window_.pNum = len(sL) - 1
		toPage(window_.pNum)	

	if len(sL[0]) > 30:
		toPage(1)
		fward.config(cmd=f)
		bward.config(cmd=b)
		blast.config(cmd=l)
	else:
		toPage(0)
#
	def s():
		student_id = window_.sby.getData()[1]

		if len(student_id) == 0: return
		if window_.sby.getData()[0] == 'bCode' and student_id not in database.studentList:
			student_does_not_exist(window_.lang)
			return

		if window_.sby.getData()[0] != 'bCode':
			scan_type = window_.sby.getData()[0]
			scan_value = window_.sby.getData()[1]

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
				student_does_not_exist(window_.lang)
				return

			student_id = student_list[0][0]
			if len(student_list) > 1:
				student_list.sort()
				student_id = multiple_match(student_list)
				if not student_id: return

		edit_salary.main(window_.lang, database=database, top=True, student_id=student_id, markerfile=markerfile)

	window_.sby.entry.bind("<Return>", lambda x: s())

	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

	#button for scan
	#Button(window_.frames["First Frame"], text="try", command=s).grid()