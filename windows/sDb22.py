from uiHandler22 import *
import editS2
from dataHandler import *
from preBuilts2 import *
from student_picker import multiple_match


def main(parent_frame, lang, database):
	database.loadData()

	window_ = AppWindow(parent_frame)

	window_.lang = lang

	window_.sT = Table(repr='stable', edit=False)
	stableh = [window_.lang['Barcode'], window_.lang['First Name'], \
				window_.lang['Last Name'], window_.lang['Chinese Name'], window_.lang['Date of Birth']]

	def sTbind(f):
		def fsb(p):
			i = window_.sT.data[p[0]-1][0]
			f(i)
		for pos, cell in window_.sT.cells.items():
			if pos[0] == 0: continue
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))

	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Second Frame", (2, 0))
	window_.newFrame("Third Frame", (2, 1))
	window_.newFrame("Fourth Frame", (4, 1))
	window_.newFrame("Fifth Frame", (3, 0))

	window_.frames["Second Frame"].rowconfigure(0, weight=5, minsize=350)
	window_.frames["Second Frame"].columnconfigure(0, weight=5, minsize=630)
	window_.frames["Second Frame"].config(bg='red')

	window_.frames["Fifth Frame"].grid(columnspan=3)

	window_.sby = Picker(repr='sby', text=window_.lang['Search By'], rads=[(window_.lang['Barcode'], 'bCode'), \
		(window_.lang['First Name'], 'firstName'), \
		(window_.lang['Last Name'], 'lastName'), \
		(window_.lang['Chinese Name'], 'chineseName')])

	window_.frames["First Frame"].addWidget(window_.sby, (0, 0))
	window_.frames["First Frame"].addWidget(bsearch, (1, 0))
	
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

	window_.frames["Second Frame"].addWidget(window_.sT, (2, 0))

	sL = [[]]
	for student in database.studentList.values():
		data_points = student.datapoints
		sL[0].append([data_points['bCode'], data_points['firstName'], data_points['lastName'], data_points['chineseName'], data_points['dob']])

	sL[0].sort()

#create pages
	#print(len(sL[0]))
	if len(sL[0]) > 15:
		l = []
		for student in sL[0]:
			l.append(student)
			if len(l) >= 15:
				sL.append(l)
				l = []
		sL.append(l)

	#if last page is blank (if num students is multiple of 30)
	if len(sL[-1]) == 0 and len(sL) != 1: sL.pop()

	window_.pNum = 1

		
	def toPage(p):
		#window_.frames["Second Frame"].addWidget(window_.sT, (2, 0))
		window_.sT.setData(headers=stableh, data=sL[p])
		window_.sT.canvas.config(width=700, height=350)
		window_.sT.set_width(2, 5, 14)
		sTbind(lambda i: editS2.main(window_.lang, database, top=True, i=i))

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

	if len(sL[0]) > 15:
		toPage(1)
		fward.config(cmd=f)
		bward.config(cmd=b)
		blast.config(cmd=l)
	else:
		toPage(0)
#
	def search():
		search_value = window_.sby.getData()[1]

		if len(search_value) == 0: return
		if window_.sby.getData()[0] == 'bCode' and search_value not in database.studentList:
			student_does_not_exist(window_.lang)
			return

		if window_.sby.getData()[0] != 'bCode':
			scan_type = window_.sby.getData()[0]
			scan_value = window_.sby.getData()[1]

			student_list = []

			for student in database.studentList:
				data_points = False
				if scan_type == 'phoneNumber':
					if database.studentList[student].datapoints['hPhone'] == scan_value or \
						database.studentList[student].datapoints['cPhone'] == scan_value or \
						database.studentList[student].datapoints['cPhone2'] == scan_value:
						data_points = database.studentList[student].datapoints

				elif database.studentList[student].datapoints[scan_type] == scan_value:
					data_points = database.studentList[student].datapoints
				
				if data_points:
					student_list.append([data_points['bCode'], data_points['firstName'], data_points['lastName'], data_points['chineseName']])

			if len(student_list) == 0:
				student_does_not_exist(window_.lang)
				return

			search_value = student_list[0][0]

			if len(student_list) > 1:
				student_list.sort()
				search_value = multiple_match(student_list)
				if not search_value: return

		editS2.main(window_.lang, database, top=True, i=search_value)


	window_.sby.entry.bind("<Return>", lambda x: search())

	bsearch.button.config(width=20)
	bsearch.config(cmd=search)