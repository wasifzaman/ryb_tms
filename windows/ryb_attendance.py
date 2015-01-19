import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\windows')
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir) + '\messages windows')
sys.path.append(os.path.abspath(os.pardir))
images = os.path.abspath(os.pardir) + '\images\\' #image directory

from tkinter import *
from tkinter import filedialog
from datetime import datetime
import configparser

from master_list import *
from choose_school import choose_school
from password_prompt import password_prompt
from uiHandler22 import Window, AppWindow, AppFrame
from dataHandler import StudentDB
from translations import english_to_chinese, chinese_to_english
from translate_ import translate
from photoWidget2 import Photo
from find_all import find_all
import keeper
import print_reports
import addS3
import scanS22
import scanOut
import sDb22
import tools2
#from languages import *

def main():
	def switch_language():
		if window_.lang['self'] == 'english':
			window_.lang = languages['chinese']
		else:
			window_.lang = languages['english']
		for frame in window_.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=window_.lang)
		bclang.config(lang=window_.lang)

	def showWindow(f, optional=False):
		if optional and optional == 'add':
			main_window_.require_confirm = [True] #pass it as list to preserve reference
		elif optional and optional == 'tools':
			if encr_config_file.files['resetpw']:
				new_pw = password_prompt(window_.lang, encr_config_file.files['dbpw'])
				if new_pw == 'cancel':
					return
				if encr_config_file.hashpw(new_pw[0]) != encr_config_file.files['dbpw']:
					wrong_password(window_.lang)
					return
				encr_config_file.files['dbpw'] = encr_config_file.hashpw(new_pw[1])
				encr_config_file.files['resetpw'] = False
				encr_config_file.save()
				pw_reset_confirm(window_.lang)
			else:
				pw_input = password_prompt(window_.lang, False)
				if pw_input == 'cancel':
					return
				if not encr_config_file.hashpw(pw_input) == encr_config_file.files['dbpw']:
					wrong_password(window_.lang)
					return

		if optional and optional == 'add':
			f(window_.frames["Second Frame"], english_to_chinese, database, main_window_.require_confirm, return_to_main)
		else:	
			f(window_.frames["Second Frame"], english_to_chinese, database)

		''' hide main window '''
		main_window_.titleFrame.config(height=1)
		main_window_.wintitle.place_forget()
		window_.frames["First Frame"].grid_forget()

		''' show opened window '''
		window_.frames["Second Frame"].grid(row=1)
		window_.frames["Third Frame"].grid()

	def return_to_main():
		if hasattr(main_window_, 'require_confirm') and main_window_.require_confirm[0]:
			if not confirm_return_to_main_window(window_.lang): return
			main_window_.require_confirm = [False]

		app_window_widgets = []
		find_all(window_.frames['Second Frame'], app_window_widgets, 'all')

		for widget in app_window_widgets:
			widget.destroy()

		window_.frames['Second Frame'].grid_forget()
		main_window_.titleFrame.config(height=60)
		main_window_.wintitle.place(in_=main_window_.titleFrame, anchor="c", relx=.5, rely=.5)

		window_.frames['Second Frame'].grid_forget()
		window_.frames["First Frame"].grid(row=1)
		window_.frames['Third Frame'].grid_forget()

		encr_config_file.files['cfilepath'] = database.file
		encr_config_file.save()

	def printPrompt():
		output_path = filedialog.askdirectory()
		if output_path != '':
			print_reports.exportreport(database, output_path, datetime.strftime(datetime.now(), '%m/%d/%Y'))
		else:
			return
		teacher_report_print_successful(window_.lang)
	
	def export_database():
		output_path = filedialog.askdirectory()
		if output_path != '':
			output_path = filedialog.askdirectory()
		else:
			return
		today = datetime.now()
		date = today.strftime('%m.%d.%y')
		time = today.strftime('%I.%M.%p')
		database.exportdb(output_path + '/RYB Teacher Backup - ' + database.school + ' ' + date + ' ' + time + '.rybdb')			
		database_backup_successful(window_.lang)
	
	main_window_ = Window()
	main_window_.attributes('-fullscreen', False)
	main_window_.geometry('1280x740+1+1')
	main_window_.wm_title("RYB Teacher Attendance")

	window_ = AppWindow(main_window_.mainFrame)

	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Second Frame", (2, 0))
	window_.newFrame("Third Frame", (3, 0))

	window_.frames['Second Frame'].grid_forget()
	window_.frames['Third Frame'].grid_forget()

	bchoose_school = Buttonbox(text='Choose school', repr='bcschool')
	bsadd = Buttonbox(text='Add Teacher', repr='bsadd') #Add Student
	bsscan = Buttonbox(text='Check-in teacher', repr='bsscan') #Scan Student
	bsscan2 = Buttonbox(text='Check-out teacher', repr='bsscan2') #Scan Student
	bssdb = Buttonbox(text='Teacher database', repr='bssdb') #Student Database
	bstools = Buttonbox(text='Tools', repr='bstools') #Database Management
	bsbmm = Buttonbox(text='Back to main menu', repr='bsbmm') #Return to Main Menu
	bsexit = Buttonbox(text='Exit', repr='bsexit') #Exit
	bclang = Buttonbox(text='changelanguage', repr='bclang') #Change Language
	bprint = Buttonbox(text='Print report', repr='bprint') #Print end of day report
	bexp = Buttonbox(text='Export database', repr='bexp')
	window_.p = Photo(repr='splash', path=os.path.abspath(images + 'background_IMG.jpg'))

	window_.frames["First Frame"].addWidget(bsadd, (1, 0))
	window_.frames["First Frame"].addWidget(bsscan, (2, 0))
	window_.frames["First Frame"].addWidget(bsscan2, (3, 0))
	window_.frames["First Frame"].addWidget(bssdb, (4, 0))
	window_.frames["First Frame"].addWidget(bstools, (5, 0))
	window_.frames["First Frame"].addWidget(bexp, (6, 0))
	window_.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	window_.frames["First Frame"].addWidget(bprint, (8, 0))
	window_.frames["First Frame"].addWidget(bsexit, (9, 0))
	window_.frames["First Frame"].addWidget(window_.p, (0, 2))
	#window_.frames["First Frame"].addWidget(bclang, (7, 0))
	
	bstools.selfframe.grid_forget()
	window_.p.label.grid(rowspan=100, sticky=E)

	#'''
	dock_frame = AppFrame(window_.frames["First Frame"], bg='#C2DAFF', padx=10, pady=5)
	dock_frame.grid(column=0, row=10, sticky=SE+W, rowspan=100)
	bclang = Buttonbox(text='changelanguage_alt', repr='bclang') #Change Language
	dock_frame.addWidget(bclang, (0, 0))
	window_.frames["First Frame"].grid(sticky=N+W)
	bclang.label.config(width=3)
	#'''

	config = configparser.ConfigParser()
	config.read(os.path.abspath(os.pardir) + '\config.ini', encoding='utf-8')

	window_.lang = languages[config['DEFAULT']['DEFAULT_LANGUAGE']]
	main_window_.wintitle.config(text=window_.lang['RYB Student Management'])

	encr_config_file = keeper.Keeper('keeper.db')
	database = StudentDB(file=encr_config_file.files['cfilepath'], pwfile=encr_config_file.files['pwfile'], cfile=encr_config_file.fname)

	if 'school' not in encr_config_file.files:
		encr_config_file.files['school'] = choose_school(window_.lang)
		if encr_config_file.files['school'] == 'cancel': encr_config_file.files['school'] = 'Flushing'
		database.school = encr_config_file.files['school']
		encr_config_file.save()
	else:
		print(encr_config_file.files['school'])
		database.school = encr_config_file.files['school']
	
	#translate(window_, english_to_chinese)
	bsadd.config(cmd=lambda: showWindow(addS3.main, 'add'))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bsscan2.config(cmd=lambda: showWindow(scanOut.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main, 'tools'))
	bsbmm.config(cmd=return_to_main)
	bprint.config(cmd=printPrompt)
	bsexit.config(cmd=main_window_.destroy)
	bclang.config(cmd=switch_language)
	bexp.config(cmd=export_database)
	window_.p.label.bind('<Control-Alt-Shift-D>', lambda e: showWindow(tools2.main, 'tools'))

	main_window_.iconbitmap(os.path.abspath(images + 'RYB_Attendance.ico'))
	main_window_.mainloop()

main()