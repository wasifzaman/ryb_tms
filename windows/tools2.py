import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir) + '\messages windows')
sys.path.append(os.path.abspath(os.pardir))

from datetime import datetime

from master_list import *
from uiHandler22 import Window, AppWindow
from preBuilts2 import *
from button import Buttonbox
from simple_label import Labelbox
from choose_school import choose_school
from create_new_db import create_new_db
from convert_to_encrypted import convert_to_encrypted
from password_prompt import password_prompt
from date_to_date import date_to_date
from find_all import find_all
from translations import english_to_chinese, chinese_to_english
from translate_ import translate
import keeper
import importwiz
import sdb_salrep
import print_reports


def main(parent_frame, lang, database):
	encr_config_file = keeper.Keeper('keeper.db')

	def change_database():
		file_path = filedialog.askopenfilename(filetypes=[('RYB database file', '.rybdb')])
		if len(file_path) == 0: return

		curdb.config(text=file_path)
		database.file = file_path
		encr_config_file.files['cfilepath'] = file_path
		encr_config_file.save()

	def ctdb():
		file_path = filedialog.askopenfilename(filetypes=[('Excel 97-2003 Workbook', '.xls'), ('Excel Workbook', '.xlsx')])
		if len(file_path) == 0: return

		database.loadData()
		ns, nt = database.importtimexlsx(file_path)
		ctimp(window_.lang, ns, nt)

	def set_pwfile():
		file_path = filedialog.askopenfilename(filetypes=[('RYB database file', '.rybdb')])
		if len(file_path) == 0: return

		file_ = open(file_path, 'rb')
		curpwfile.config(text=file_path)
		database.pwfile = file_path
		encr_config_file.files['pwfile'] = file_path
		encr_config_file.save()

	def set_markerfile(label):
		file_path = filedialog.askopenfilename(filetypes=[('RYB database file', '.rybdb')])
		if len(file_path) == 0: return

		label.config(text=open_f.name)
		encr_config_file.files['markerfile'] = open_f.name
		encr_config_file.save()

	def print_report_by_range():
		start_date, end_date = date_to_date(window_.lang)
		if not start_date: return

		dest_path = filedialog.askdirectory()
		if dest_path == None: return
		
		print_reports.print_teacher_attendance(database, dest_path, start_date, end_date)

	def print_report_by_range_simple():
		start_date, end_date = date_to_date(window_.lang)
		if not start_date: return

		dest_path = filedialog.askdirectory()
		if dest_path == None: return

		print_reports.print_teacher_attendance_simple(database, dest_path, start_date, end_date)

	def salrep():
		app_window_widgets = []
		find_all(parent_frame, app_window_widgets, 'all')

		for widget in app_window_widgets:
			widget.destroy()

		sdb_salrep.main(parent_frame, window_.lang, database, encr_config_file.files['markerfile'])

	def choose_school_(event):
		school = choose_school(window_.lang)
		if school == 'cancel': return

		encr_config_file.files['school'] = school
		database.school = encr_config_file.files['school']
		current_school.setData(database.school)
		encr_config_file.save()

	def reset_dbmanager_pw(lang):
		new_pw = password_prompt(lang, encr_config_file.files['dbpw'])
		if new_pw == 'cancel': return
		if encr_config_file.hashpw(new_pw[0]) != encr_config_file.files['dbpw']:
			wrong_password(window_.lang)
			return
		encr_config_file.files['dbpw'] = encr_config_file.hashpw(new_pw[1])
		encr_config_file.files['resetpw'] = False
		encr_config_file.save()
		pw_reset_confirm(window_.lang)

	def switch_frame(frame):
		if hasattr(window_, 'current_frame'):
			if frame == window_.current_frame: return
			window_.frames[window_.current_frame].grid_forget()

		window_.current_frame = frame		
		window_.frames[window_.current_frame].grid(row=0, column=1, sticky=NW)

	def create_new_markerfile():
		out_file = filedialog.asksaveasfilename()
		if len(out_file) == 0: return
		pickle.dump({}, open(out_file + '.rybdb', "wb"))

	window_ = AppWindow(parent_frame)

	window_.lang = lang

	window_.newFrame("Toggle Frame", (0, 0))
	window_.newFrame("Import/Export Frame", (0, 0))
	window_.newFrame("Print Reports Frame", (0, 0))
	window_.newFrame("School Frame", (0, 0))
	window_.newFrame("Database Frame", (0, 0))
	window_.newFrame("Password Frame", (0, 0))

	window_.frames["Toggle Frame"].grid(padx=(0, 10))
	window_.frames["Import/Export Frame"].grid_forget()
	window_.frames["Print Reports Frame"].grid_forget()
	window_.frames["School Frame"].grid_forget()
	window_.frames["Database Frame"].grid_forget()
	window_.frames["Password Frame"].grid_forget()
	
	import_export_toggle = Buttonbox(text='Import/export', repr=None)
	print_reports_toggle = Buttonbox(text='Print reports', repr=None)
	school_toggle = Buttonbox(text='School', repr=None)
	database_toggle = Buttonbox(text='Database', repr=None)
	password_toggle = Buttonbox(text='Passwords', repr=None)
	bchoose_school = Buttonbox(text='Choose school', lang=window_.lang, repr='bcschool')
	reset_db_manager_pw = Buttonbox(text='Reset DB manager PW', lang=window_.lang, repr='resetdbmanagerpw')
	print_report_button = Buttonbox(text='Print report', lang=window_.lang, repr='printreport')
	curdb = TextboxNoEdit(text='Database', repr=None)
	curpwfile = TextboxNoEdit(text='PW file', repr=None)
	curmarkerfile = TextboxNoEdit(text='Marker', repr=None)
	current_school = TextboxNoEdit(text='School', repr=None)
	choose_pwfile = Buttonbox(text='Choose PW file', lang=window_.lang, repr='cpwfile')
	choose_markerfile = Buttonbox(text='Choose Marker File', lang=window_.lang, repr='cmarkerfile')
	create_db = Buttonbox(text='Create new database', lang=window_.lang, repr='createdb')
	create_markerfile = Buttonbox(text='Create new markerfile', lang=window_.lang, repr='createmfile')
	convert_db = Buttonbox(text='Convert to encrypted DB', lang=window_.lang, repr='convertdb')
	print_simple_attendance = Buttonbox(text='Print simple report', lang=window_.lang, repr='simplereport')
	import_data_button = Buttonbox(text='Import data', repr=None)
	import_time_data_button = Buttonbox(text='Import time data', repr=None)
	salary_report_button = Buttonbox(text='Salary report', repr=None)
	change_database_button = Buttonbox(text='Change database', repr=None)

	window_.frames["Toggle Frame"].addWidget(import_export_toggle, (0, 0))
	window_.frames["Toggle Frame"].addWidget(print_reports_toggle, (1, 0))
	window_.frames["Toggle Frame"].addWidget(school_toggle, (2, 0))
	window_.frames["Toggle Frame"].addWidget(database_toggle, (3, 0))
	window_.frames["Toggle Frame"].addWidget(password_toggle, (4, 0))
	window_.frames["Import/Export Frame"].addWidget(import_data_button, (1, 0))
	window_.frames["Import/Export Frame"].addWidget(import_time_data_button, (2, 0))
	window_.frames["Print Reports Frame"].addWidget(salary_report_button, (3, 0))
	window_.frames["Print Reports Frame"].addWidget(print_report_button, (4, 0))
	window_.frames["Print Reports Frame"].addWidget(print_simple_attendance, (5, 0))
	window_.frames["School Frame"].addWidget(current_school, (0, 0))
	window_.frames["School Frame"].addWidget(bchoose_school, (1, 0))
	window_.frames["Database Frame"].addWidget(curdb, (0, 0))
	window_.frames["Database Frame"].addWidget(curpwfile, (1, 0))
	window_.frames["Database Frame"].addWidget(curmarkerfile, (2, 0))
	window_.frames["Database Frame"].addWidget(change_database_button, (3, 0))
	window_.frames["Database Frame"].addWidget(choose_pwfile, (4, 0))
	window_.frames["Database Frame"].addWidget(choose_markerfile, (5, 0))
	window_.frames["Database Frame"].addWidget(create_db, (3, 1))
	window_.frames["Database Frame"].addWidget(create_markerfile, (4, 1))
	window_.frames["Database Frame"].addWidget(convert_db, (5, 1))
	window_.frames["Password Frame"].addWidget(reset_db_manager_pw, (1, 0))

	current_school.widget_frame.grid(pady=(0, 10))
	curdb.widget_frame.grid(columnspan=2, sticky=NW)
	curpwfile.widget_frame.grid(columnspan=2, sticky=NW)
	curmarkerfile.widget_frame.grid(columnspan=2, sticky=NW, pady=(0, 10))
	choose_pwfile.widget_frame.grid(padx=(0, 10))
	change_database_button.widget_frame.grid(padx=(0, 10))
	choose_markerfile.widget_frame.grid(padx=(0, 10))
	current_school.label.config(width=7)
	bchoose_school.widget_frame.grid(sticky=W)
	window_.grid_propagate(False)
	window_.config(width=850, height=300)
	#window_.grid_columnconfigure(1, minsize=300)
	#window_.grid_rowconfigure(0, minsize=500)
	
	curdb.setData(encr_config_file.files['cfilepath'])
	curpwfile.setData(encr_config_file.files['pwfile'])
	curmarkerfile.setData(encr_config_file.files['markerfile'])
	current_school.setData(database.school)
	switch_frame('Import/Export Frame')

	import_export_toggle.config(cmd=lambda: switch_frame('Import/Export Frame'))
	print_reports_toggle.config(cmd=lambda: switch_frame('Print Reports Frame'))
	school_toggle.config(cmd=lambda: switch_frame('School Frame'))
	database_toggle.config(cmd=lambda: switch_frame('Database Frame'))
	password_toggle.config(cmd=lambda: switch_frame('Password Frame'))
	bchoose_school.config(cmd=lambda: choose_school_(window_.lang))
	import_data_button.config(cmd=lambda: importwiz.main(window_.lang, database))
	change_database_button.config(cmd=lambda: change_database())
	import_time_data_button.config(cmd=ctdb)
	salary_report_button.config(cmd=salrep)
	choose_pwfile.config(cmd=lambda: set_pwfile())
	convert_db.config(cmd=lambda: convert_to_encrypted(window_.lang, database))
	create_db.config(cmd=lambda: create_new_db(window_.lang, database))
	create_markerfile.config(cmd=create_new_markerfile)
	choose_markerfile.config(cmd=lambda: set_markerfile(curmarkerfile))
	reset_db_manager_pw.config(cmd=lambda: reset_dbmanager_pw(window_.lang))
	print_report_button.config(cmd=print_report_by_range)
	print_simple_attendance.config(cmd=print_report_by_range_simple)
	
	'''
	window_.mmbuttoncol = 'tomato'
	window_.mmbuttonfg = 'black'

	bsalrep.idlebg = window_.mmbuttoncol
	bsalrep.fg = window_.mmbuttonfg
	bsalrep.hoverfg = 'white'
	bsalrep.hoverbg = 'crimson'
	bsalrep.label.config(bg=bsalrep.idlebg, fg=bsalrep.fg)

	bcdb.idlebg = window_.mmbuttoncol
	bcdb.fg = window_.mmbuttonfg
	bcdb.hoverfg = 'white'
	bcdb.hoverbg = 'crimson'
	bcdb.label.config(bg=bcdb.idlebg, fg=bcdb.fg)
	'''

	if lang == 'chinese':
		translate(window_, english_to_chinese)