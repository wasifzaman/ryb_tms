from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(parent_frame, lang, database, return_to_main):
	'''addS3'''

	window_ = AppWindow(parent_frame)
	window_.lang = lang

	window_.newFrame("First Frame", (1, 1))
	window_.newFrame("Second Frame", (1, 2))
	window_.newFrame("Fourth Frame", (2, 2))
	window_.newFrame("Fifth Frame", (5, 0))
	window_.newFrame("Sixth Frame", (4, 2))
	window_.newFrame("Seventh Frame", (1, 0))
	window_.newFrame("Eigth Frame", (3, 2))
	window_.newFrame("Ninth Frame", (2, 1))

	window_.frames["Ninth Frame"].grid(rowspan=3)
	window_.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	window_.frames["Seventh Frame"].grid(rowspan=2)
	window_.frames["Ninth Frame"].grid(rowspan=2, sticky=E)

	add_student_button = Buttonbox(text='addstudent', lang=language, repr='sadd')

	window_.sectioncolor = "#3B5C8D"

	window_.frames["First Frame"].addWidget(sinfo, (0, 0))
	window_.frames["First Frame"].addWidget(firstName, (1, 0))
	window_.frames["First Frame"].addWidget(lastName, (2, 0))
	window_.frames["First Frame"].addWidget(chineseName, (3, 0))
	window_.frames["First Frame"].addWidget(dob, (4, 0))
	window_.frames["First Frame"].addWidget(cp, (7, 0)) #card printed
	window_.frames["Second Frame"].addWidget(ainfo, (0, 0))
	window_.frames["Second Frame"].addWidget(addr, (3, 0))
	window_.frames["Second Frame"].addWidget(city, (4, 0))
	window_.frames["Second Frame"].addWidget(state, (5, 0))
	window_.frames["Second Frame"].addWidget(zip, (6, 0))
	window_.frames["Second Frame"].addWidget(email, (7, 0))
	window_.frames["Second Frame"].addWidget(cPhone, (8, 0))
	window_.frames["Second Frame"].addWidget(cPhone2, (9, 0))
	window_.frames["Fourth Frame"].addWidget(pinfo, (0, 0))
	window_.frames["Fourth Frame"].addWidget(bCode, (1, 0))
	window_.frames["Fifth Frame"].addWidget(add_student_button, (0, 0))
	window_.frames["Seventh Frame"].addWidget(portr, (0, 0))
	window_.frames["Ninth Frame"].addWidget(ninfo, (0, 0))
	window_.frames["Ninth Frame"].addWidget(notes, (1, 0))

	ainfo.label.config(bg=window_.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	sinfo.label.config(bg=window_.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'), text=window_.lang['Student information'])
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	pinfo.label.config(bg=window_.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	add_student_button.button.config(height=5, font=('Verdana', '12'))
	notes.label.grid_forget()
	notes.config(height=8, width=32)
	portr.label.config(bg='black')
	
	database.loadData()
	bCode.setData(database.formatCode())

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

	add_student_button.config(cmd=collect)

	for frame in window_.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=window_.lang)