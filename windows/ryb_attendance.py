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


def main():
	def switch_language():
		if window_.lang == 'english':
			window_.lang = 'chinese'
			translate(window_, english_to_chinese)
			bclang.label.config(text='E')
		else:
			window_.lang = 'english'
			translate(window_, chinese_to_english)
			bclang.label.config(text='中文')

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
			f(window_.frames["App Frame"], window_.lang, database, main_window_.require_confirm, return_to_main)
		else:	
			f(window_.frames["App Frame"], window_.lang, database)

		''' hide main window '''
		main_window_.titleFrame.config(height=1)
		main_window_.wintitle.place_forget()
		window_.frames["Button Frame"].grid_forget()
		window_.frames["Image Frame"].grid_forget()
		window_.frames["Dock Frame"].grid_forget()

		''' show opened window '''
		window_.frames["App Frame"].grid(row=1, padx=10, pady=10)
		window_.frames["Return Button Frame"].grid()

	def return_to_main():
		if hasattr(main_window_, 'require_confirm') and main_window_.require_confirm[0]:
			if not confirm_return_to_main_window(window_.lang): return
			main_window_.require_confirm = [False]

		app_window_widgets = []
		find_all(window_.frames['App Frame'], app_window_widgets, 'all')

		for widget in app_window_widgets:
			widget.destroy()

		window_.frames['App Frame'].grid_forget()
		main_window_.titleFrame.config(height=60)
		main_window_.wintitle.place(in_=main_window_.titleFrame, anchor="c", relx=.5, rely=.5)

		window_.frames['App Frame'].grid_forget()
		window_.frames["Button Frame"].grid(row=0, column=0, sticky=N+W)
		window_.frames["Image Frame"].grid(row=0, column=1, rowspan=2)
		window_.frames["Dock Frame"].grid(row=1, column=0, sticky=SE+W)
		window_.frames['Return Button Frame'].grid_forget()

		#encr_config_file.files['cfilepath'] = database.file
		#encr_config_file.save()

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
	config = configparser.ConfigParser()
	config.read(os.path.abspath(os.pardir) + '\config.ini', encoding='utf-8')
	window_.lang = config['DEFAULT']['DEFAULT_LANGUAGE']

	window_.newFrame("Button Frame", (0, 0))
	window_.newFrame("Image Frame", (0, 1))
	window_.newFrame("Dock Frame", (1, 0))
	window_.newFrame("App Frame", (1, 0))
	window_.newFrame("Return Button Frame", (2, 0))

	window_.frames['App Frame'].grid_forget()
	window_.frames['Return Button Frame'].grid_forget()

	bchoose_school = Buttonbox(text='Choose school', repr='bcschool')
	bsadd = Buttonbox(text='Add teacher', repr='bsadd') #Add Student
	bsscan = Buttonbox(text='Check-in teacher', repr='bsscan') #Scan Student
	bsscan2 = Buttonbox(text='Check-out teacher', repr='bsscan2') #Scan Student
	bssdb = Buttonbox(text='Teacher database', repr='bssdb') #Student Database
	bstools = Buttonbox(text='Tools', repr='bstools') #Database Management
	bsbmm = Buttonbox(text='Back to main menu', repr='bsbmm') #Return to Main Menu
	bsexit = Buttonbox(text='', repr='bsexit') #Exit
	bprint = Buttonbox(text='Print report', repr='bprint') #Print end of day report
	bexp = Buttonbox(text='Export database', repr='bexp')
	splash_image = Photo(repr='splash', path=os.path.abspath(images + 'background_IMG.jpg'))
	bclang = Buttonbox(text='E', repr='bclang') #Change Language

	window_.frames["Button Frame"].addWidget(bsadd, (0, 0))
	window_.frames["Button Frame"].addWidget(bsscan, (1, 0))
	window_.frames["Button Frame"].addWidget(bsscan2, (2, 0))
	window_.frames["Button Frame"].addWidget(bssdb, (3, 0))
	window_.frames["Button Frame"].addWidget(bstools, (4, 0))
	window_.frames["Image Frame"].addWidget(splash_image, (0, 0))
	window_.frames["Return Button Frame"].addWidget(bsbmm, (0, 0))
	window_.frames["Dock Frame"].addWidget(bexp, (0, 1))
	window_.frames["Dock Frame"].addWidget(bprint, (0, 2))
	window_.frames["Dock Frame"].addWidget(bsexit, (0, 3))
	#window_.frames["Button Frame"].addWidget(bclang, (7, 0))
	
	window_.frames["Image Frame"].grid(rowspan=2)
	window_.frames["Dock Frame"].addWidget(bclang, (0, 0))
	window_.frames["Dock Frame"].config(bg='#B9B8E0')
	window_.frames["Button Frame"].config(bg='black')
	window_.frames["Button Frame"].grid(sticky=N+W)
	window_.frames["Dock Frame"].grid(sticky=SE+W)

	''' hover button colors '''
	label_bg = '#4DBCE9'
	hover_bg = '#26ADE4'

	''' widget settings '''
	bsadd.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bsscan.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bsscan2.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bssdb.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bstools.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bexp.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bprint.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bsbmm.config(label_bg=label_bg, hover_bg=hover_bg, label_fg='black')
	bexp.config(image=images + 'backup.png', image_resize=(28, 28))
	bprint.config(label_bg='#366BFF', hover_bg='#4785FF', image=images + 'print.png', image_resize=(28, 28))
	bsexit.config(label_bg='#FC354C', hover_bg='#CC0C39', image=images + 'close.png', image_resize=(28, 28))
	bclang.config(label_bg='#C0D860', hover_bg='#789048')
	bclang.label.config(width=4)
	bclang.widget_frame.grid(pady=0)
	splash_image.label.config(bg='black')
	bstools.widget_frame.grid_forget()
	main_window_.titleFrame.config(bg='#353432')
	main_window_.wintitle.config(bg='#353432')
	main_window_.wintitle.config(text='RYB Student Management')
	main_window_.iconbitmap(os.path.abspath(images + 'RYB_Attendance.ico'))
	bexp.label.config(width=4)
	bexp.widget_frame.grid(pady=0)
	bprint.label.config(width=4)
	bprint.widget_frame.grid(pady=0)
	bsexit.label.config(width=4)
	bsexit.widget_frame.grid(pady=0)

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
	splash_image.label.bind('<Control-Alt-Shift-D>', lambda event: showWindow(tools2.main, 'tools'))

	if window_.lang == 'chinese':
		translate(window_, english_to_chinese)
		bclang.label.config(text='E')
	else:
		bclang.label.config(text='中文')

	main_window_.mainloop()

main()