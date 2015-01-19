import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir) + '\messages windows')

from uiHandler22 import AppWindow
from master_list import *
from student_picker import spicker
from textbox import Textbox, TextboxNoEdit
from button import Buttonbox
from simple_label import Labelbox
from date_textbox import Datebox
from multiline_textbox import LongTextbox
from toggle_option import Toggle_option
from tableWidget2 import Table


def main(parent_frame, lang, database):
	database.loadData()

	window_ = AppWindow(parent_frame)

	window_.lang = None

	window_.newFrame("Search Frame", (0, 0))
	window_.newFrame("General Info Frame", (1, 0))
	window_.newFrame("Notes Frame", (2, 0))
	window_.newFrame("Button Frame", (3, 0))
	window_.newFrame("Table Frame", (1, 1))

	window_.frames["Search Frame"].grid(columnspan=2)
	window_.frames["Button Frame"].grid(columnspan=2)
	window_.frames["Table Frame"].grid(rowspan=2)

	attendance_table = Table(repr='attinfox')
	attendance_table_headers = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
	search_value = Textbox(text="Search", repr=None)
	search_options = Toggle_option(
		options=(('Barcode', 'bCode'),('First Name', 'firstName'), \
		('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
		('Phone Number', 'phoneNumber')), repr=None)
	general_header = Labelbox(text='General', lang=lang, repr='sinfo')
	notes_header = Labelbox(text='Notes', lang=lang, repr='ninfo')
	first_name = Textbox(text="First name", lang=lang, repr='firstName')
	last_name = Textbox(text="Last name", lang=lang, repr='lastName')
	chinese_name = Textbox(text="Chinese name", lang=lang, repr='chineseName')
	date_of_birth = Datebox(text="Date of birth", lang=lang, repr='dob')
	barcode = TextboxNoEdit(text="Barcode", lang=lang, repr='bCode')
	notes = LongTextbox(text="Notes", lang=lang, repr='notes')
	search_button = Buttonbox(text='Search', lang=window_.lang, repr='searchbutton')
	save_button = Buttonbox(text='Save', lang=window_.lang, repr='save_button')
	manual_entry_button = Buttonbox(text='Manual Entry', repr='manualentrybutton')

	window_.frames["Search Frame"].addWidget(search_value, (0, 0))
	window_.frames["Search Frame"].addWidget(search_options, (1, 0))
	window_.frames["Search Frame"].addWidget(search_button, (0, 1))
	window_.frames["General Info Frame"].addWidget(general_header, (0, 0))
	window_.frames["General Info Frame"].addWidget(first_name, (1, 0))
	window_.frames["General Info Frame"].addWidget(last_name, (2, 0))
	window_.frames["General Info Frame"].addWidget(chinese_name, (3, 0))
	window_.frames["General Info Frame"].addWidget(date_of_birth, (4, 0))
	window_.frames["General Info Frame"].addWidget(barcode, (7, 0))
	window_.frames["Notes Frame"].addWidget(notes_header, (8, 0))
	window_.frames["Notes Frame"].addWidget(notes, (9, 0))
	window_.frames["Table Frame"].addWidget(attendance_table, (0, 0))
	window_.frames["Button Frame"].addWidget(save_button, (0, 0))
	window_.frames["Button Frame"].addWidget(manual_entry_button, (0, 1))
	#window_.frames["Fourth Frame"].addWidget(early_checkin, (0, 0))

	search_options.widget_frame.grid(columnspan=2)
	notes.label.pack_forget()
	notes.config(height=6, width=30)
	search_options.config(width=15, inactive_bg='#AEE239', active_bg='#8FBE00')
	attendance_table.canvas.config(width=695, height=300)

	def search_student():
		window_.student_id = search_value.getData()

		if len(window_.student_id) == 0: return
		if search_options.stringvar.get() == 'bCode' and window_.student_id not in database.studentList:
			student_does_not_exist(window_.lang)
			return

		if search_options.stringvar.get() != 'bCode':
			scan_type = search_options.stringvar.get()
			scan_value = search_value.getData()
			student_list = []

			for student in database.studentList:
				matched_student_data_points = False
				if scan_type == 'phoneNumber':
					if database.studentList[student].datapoints['hPhone'] == scan_value or \
						database.studentList[student].datapoints['cPhone'] == scan_value or \
						database.studentList[student].datapoints['cPhone2'] == scan_value:
						matched_student_data_points = database.studentList[student].datapoints
				elif database.studentList[student].datapoints[scan_type] == scan_value:
					matched_student_data_points = database.studentList[student].datapoints
				
				if matched_student_data_points:
					student_list.append([
						matched_student_data_points['bCode'],
						matched_student_data_points['firstName'],
						matched_student_data_points['lastName'],
						matched_student_data_points['chineseName']])

			if len(student_list) == 0:
				student_does_not_exist(window_.lang)
				return

			if len(student_list) > 1:
				student_list.sort()
				window_.student_id = spicker(student_list)
				if not window_.student_id: return
			else:
				window_.student_id = student_list[0][0]

		search_value.entry.delete(0, END) #reset search

		data_points = database.studentList[window_.student_id].datapoints
		window_.populate(data_points)
		window_.original_data_points = window_.collect(database.studentList[window_.student_id].datapoints)

		dt = datetime.now()
		date = datetime.strftime(dt, '%m/%d/%Y')
		time = datetime.strftime(dt, '%I:%M %p')
		timeslot = database.findTimeSlot(dt)
		overwrite = False
		if date in [row[0] for row in data_points['attinfo'][1]]:
			if not confirm_overwrite_checkin(window_.lang):
				search_options.config(set_=0)
				return
			else: overwrite = True

		confirm_status = confirm_check_in_time(window_.lang, database)
		data = [date, time, timeslot, '', '', database.school]
		if confirm_status == 'manual':
			time_ = time_entry(window_.lang)
			if not time_: return
			data[1] = time
			data[2] = time_
			if overwrite:
				data_points['attinfo'][1][-1][1] = ''
				data_points['attinfo'][1][-1][2] = time_
			else:
				data_points['attinfo'][1].append(data)
		elif confirm_status:
			if overwrite:
				data_points['attinfo'][1][-1] = data
			else:
				database.scanStudent(window_.student_id)
		else:
			search_options.config(set_=0) #reset search bar
			return

		database.saveData()
		attendance_table.setData(
			headers=attendance_table_headers,
			data=[data_points['attinfo'][1][-1][:5]]) #display last entry
		attendance_table.set_width(2, 5, 14)
		search_options.config(set_=0) #reset search bar
		attendance_table.canvas.yview_moveto(1.0) #scroll to bottom of table

	def manual_scan():

		print(bCodeNE.getData())
		if (len(bCodeNE.getData())) == 0: return

		dt = date_time_entry(window_.lang)
		if not dt[0]: return
		if datetime.strptime(dt[0], '%m/%d/%Y') > datetime.now():
			deny_checkout_future(window_.lang, dt[0])
			return
		if not dt[0]: return
		date = dt[0]
		time = dt[1]
		time_entry = '' if datetime.strptime(date, '%m/%d/%Y').date() != datetime.now().date() else datetime.strftime(datetime.now(), '%I:%M %p') 

		print(date, time)

		data_points = database.studentList[bCodeNE.getData()].datapoints

		data = False
		for row in data_points['attinfo'][1]:
			if row[0] == date and confirm_overwrite_checkin(window_.lang):
				if len(row[4]) != 0 and datetime.strptime(date + ' ' + row[4], '%m/%d/%Y %I:%M %p') < datetime.strptime(date + ' ' + time, '%m/%d/%Y %I:%M %p'):
					checkout_earlier_checkin(window_.lang)
					return
				row[1] = time_entry
				row[2] = time
				database.saveData()
				attendance_table.setData(
					headers=attendance_table_headers,
					data=[[date, time_entry, time, '', '']])
				attendance_table.set_width(2, 5, 14)
				return

		data_points['attinfo'][1].append([date, time_entry, time, '', '', database.school])
		database.sort_attendance(bCodeNE.getData())
		database.saveData()
		attendance_table.setData(
			headers=attendance_table_headers,
			data=[[date, time_entry, time, '', '']])
		attendance_table.set_width(2, 5, 14)

	def collect():
		if not altered(): return
		if not confirm_save_teacher_data(window_.lang): return
		student = database.studentList[window_.student_id]
		student.datapoints.update(window_.collect(student.datapoints))
		window_.original_data_points = window_.collect(student.datapoints)
		database.saveData()
		
	def altered():
		current_data_points = window_.collect(window_.original_data_points)
		for key in current_data_points.keys():
			if current_data_points[key] != window_.original_data_points[key]:
				return True
		return False

	search_button.config(cmd=search_student)
	manual_entry_button.config(cmd=lambda: manual_scan())
	search_value.entry.bind("<Return>", lambda event: search_student())
	save_button.config(cmd=collect)