import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')

from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from translate_ import translate


def main(parent_frame, lang, database, return_to_main):
	'''addS3'''

	window_ = AppWindow(parent_frame)
	window_.lang = lang

	window_.newFrame("Image Frame", (0, 0))
	window_.newFrame("General Info Frame", (0, 1))
	window_.newFrame("Contact Frame", (1, 1))
	window_.newFrame("Notes Frame", (1, 0))
	window_.newFrame("Button Frame", (2, 0))

	window_.frames["Notes Frame"].grid(rowspan=3)
	window_.frames["Button Frame"].grid(columnspan=5, sticky=S)
	window_.frames["Image Frame"].grid(rowspan=2)
	window_.frames["Notes Frame"].grid(rowspan=2, sticky=E)

	window_.sectioncolor = "#3B5C8D"

	general_header = Labelbox(text='General', lang=language, repr='sinfo')
	adress_header = Labelbox(text="Address", lang=language, repr='ainfo')
	notes_header = Labelbox(text='Notes', lang=language, repr='ninfo')
	first_name = Textbox(text="First name", lang=language, repr='firstName')
	last_name = Textbox(text="Last name", lang=language, repr='lastName')
	chinese_name = Textbox(text="Chinese name", lang=language, repr='chineseName')
	date_of_birth = Datebox(text="Date of birth", lang=language, repr='dob')
	card_print_status = Textbox(text="Card printed", lang=language, repr='cp')
	barcode = TextboxNoEdit(text="Barcode", lang=language, repr='bCode')
	address = Textbox(text="Address", lang=language, repr='addr')
	city = Textbox(text="City", lang=language, repr='city')
	state = Textbox(text="State", lang=language, repr='state')
	email = Textbox(text="E-mail", lang=language, repr='email')
	cell_phone = Textbox(text="Cell phone", lang=language, repr='cPhone')
	cell_phone_2 = Textbox(text="Cell phone 2", lang=language, repr='cPhone2')
	zipcode = IntTextbox(text="Zipcode", lang=language, repr='zip')
	add_student_button = Buttonbox(text='Add Teacher', lang=language, repr='sadd')

	window_.frames["General Info Frame"].addWidget(general_header, (0, 0))
	window_.frames["General Info Frame"].addWidget(first_name, (1, 0))
	window_.frames["General Info Frame"].addWidget(last_name, (2, 0))
	window_.frames["General Info Frame"].addWidget(chinese_name, (3, 0))
	window_.frames["General Info Frame"].addWidget(date_of_birth, (4, 0))
	window_.frames["General Info Frame"].addWidget(barcode, (5, 0))
	window_.frames["General Info Frame"].addWidget(card_print_status, (7, 0)) #card printed
	window_.frames["Contact Frame"].addWidget(adress_header, (0, 0))
	window_.frames["Contact Frame"].addWidget(address, (3, 0))
	window_.frames["Contact Frame"].addWidget(city, (4, 0))
	window_.frames["Contact Frame"].addWidget(state, (5, 0))
	window_.frames["Contact Frame"].addWidget(zip, (6, 0))
	window_.frames["Contact Frame"].addWidget(email, (7, 0))
	window_.frames["Contact Frame"].addWidget(cell_phone, (8, 0))
	window_.frames["Contact Frame"].addWidget(cell_phone_2, (9, 0))
	window_.frames["Image Frame"].addWidget(portr, (0, 0))
	window_.frames["Notes Frame"].addWidget(notes_header, (0, 0))
	window_.frames["Notes Frame"].addWidget(notes, (1, 0))
	window_.frames["Button Frame"].addWidget(add_student_button, (0, 0))

	def collect():
		new_student = StudentInfo()
		new_student.datapoints = dict(list(new_student.datapoints.items()) + list(window_.collect(new_student.datapoints).items()))

		new_student_id = new_student.datapoints['bCode']
		if (database.checkCode(new_student_id) and \
			(not confirm_overwrite_teacher(database.studentList[new_student_id].datapoints['firstName'], window_.lang))) \
			or not confirm_teacher_addition(window_.lang):
			return
 
		new_student.datapoints['attinfo'] = [['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time', 'School'], []]
		database.addStudent(new_student.datapoints['bCode'], new_student)
		database.saveData()

		teacher_added(window_.lang)
		portr.setData('monet_sm.jpg')

		return_to_main(False)

	add_student_button.label.config(height=5, font=('Verdana', '12'))
	notes.label.grid_forget()
	notes.config(height=8, width=32)
	portr.label.config(bg='black')
	add_student_button.config(cmd=collect)

	database.loadData()
	barcode.setData(database.formatCode())
	translate(window_, lang)