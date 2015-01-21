import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\windows')
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\database')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir))
images = os.path.abspath(os.pardir) + '\images\\' #image directory

from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from Crypto.Cipher import AES
from datetime import datetime, time, timedelta
import hashlib
import configparser
import pickle
import xlrd, xlsxwriter
import shutil, copy
import inspect

import addS3
import scanS22
import scanOut
import sDb22
import tools2
import sdb_salrep
import preBuilts2
from choose_school import choose_school
from password_prompt import password_prompt
import print_reports
from uiHandler22 import *
from dataHandler import *
from photoWidget2 import *
from preBuilts2 import *
from languages import *


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


	main_window_ = Window(top=False)
	main_window_.attributes('-fullscreen', False)
	main_window_.geometry('1280x740+1+1')
	main_window_.wm_title("RYB Teacher Attendance")

	main_window_.con = False

	def showWindow(f):
		main_window_.titleFrame.config(height=1)
		main_window_.wintitle.place_forget()
		window_.frames["First Frame"].grid_forget()
		print(f.__doc__)
		if (f.__doc__) == 'addS3':
			main_window_.con = True
			window_.main_window_ = f(window_.frames["Second Frame"], window_.lang, window_.d, return_to_main)
		elif (f.__doc__) == 'tools2':
			if window_.k.files['resetpw'] == True:
				new_pw = password_prompt(window_.lang, window_.k.files['dbpw'])
				if new_pw == 'cancel' or window_.k.hashpw(new_pw[0]) != window_.k.files['dbpw']:
					wrong_password(window_.lang)
					return_to_main(main_window_.con)
					return
				window_.k.files['dbpw'] = window_.k.hashpw(new_pw[1])
				window_.k.files['resetpw'] = False
				window_.k.save()
				pw_reset_confirm(window_.lang)
			else:
				pw_input = password_prompt(window_.lang, False)
				if not window_.k.hashpw(pw_input) == window_.k.files['dbpw'] or pw_input == 'cancel':
					wrong_password(window_.lang)
					return_to_main(main_window_.con)
					return
			window_.main_window_ = f(window_.frames["Second Frame"], window_.lang, window_.d, window_.k)
		else:
			main_window_.con = False
			window_.main_window_ = f(window_.frames["Second Frame"], window_.lang, window_.d)
		window_.frames["Second Frame"].grid()
		window_.frames["Third Frame"].grid()

	def return_to_main(con):
		if con:
			if not return_to_main_window(window_.lang): return

		window_.frames['Second Frame'].grid_forget()
		main_window_.titleFrame.config(height=60)
		main_window_.wintitle.place(in_=main_window_.titleFrame, anchor="c", relx=.5, rely=.5)
		
		window_.frames['Second Frame'].grid_forget()
		try:
			#to destroy the extra window in scan student
			window_.main_window_.destroy()
		except:
			pass

		for child in window_.frames["Second Frame"].winfo_children():
			child.destroy()

		window_.frames['Second Frame'].destroy()
		window_.newFrame("Second Frame", (2, 0))
		window_.frames['Second Frame'].grid_forget()

		window_.frames["First Frame"].grid(row=1)
		window_.frames['Third Frame'].grid_forget()

		window_.k.files['cfilepath'] = window_.d.file
		window_.k.save()

	def printPrompt():
		output_path = filedialog.askdirectory()
		if output_path != '':
			print_reports.exportreport(window_.d, output_path, datetime.strftime(datetime.now(), '%m/%d/%Y'))
		else:
			return
		teacher_report_print_successful(window_.lang)
	
	def expf():
		try:
			fpath = filedialog.askdirectory()
			today = datetime.now()
			date = today.strftime('%m.%d.%y')
			time = today.strftime('%I.%M.%p')
			window_.d.exportdb(fpath + '/RYB Teacher Backup - ' + window_.d.school + ' ' + date + ' ' + time + '.rybdb')			
			database_backup_successful(window_.lang)
		except:
			return
	
	config = configparser.ConfigParser()
	config.read(os.path.abspath(os.pardir) + '\config.ini', encoding='utf-8')

	window_ = AppWindow(main_window_.mainFrame)
	window_.lang = languages[config['DEFAULT']['DEFAULT_LANGUAGE']]
	main_window_.wintitle.config(text=window_.lang['RYB Student Management'])

	window_.k = keeper.Keeper('keeper.db')
	window_.d = StudentDB(file=window_.k.files['cfilepath'], pwfile=window_.k.files['pwfile'], cfile=window_.k.fname)

	if 'school' not in window_.k.files:
		window_.k.files['school'] = choose_school(window_.lang)
		if window_.k.files['school'] == 'cancel': window_.k.files['school'] = 'Flushing'
		window_.d.school = window_.k.files['school']
		window_.k.save()
	else:
		print(window_.k.files['school'])
		window_.d.school = window_.k.files['school']

	window_.newFrame("First Frame", (1, 0))
	window_.newFrame("Second Frame", (2, 0))
	window_.newFrame("Third Frame", (3, 0))

	window_.frames['Second Frame'].grid_forget()
	window_.frames['Third Frame'].grid_forget()

	bchoose_school = Buttonbox(text='Choose School', lang=window_.lang, repr='bcschool')
	bsadd = Buttonbox(text='Add Students', lang=window_.lang, repr='bsadd') #Add Student
	bsscan = Buttonbox(text='Scan Students', lang=window_.lang, repr='bsscan') #Scan Student
	bsscan2 = Buttonbox(text='Scan Out Teacher', lang=window_.lang, repr='bsscan2') #Scan Student
	bssdb = Buttonbox(text='Student Database', lang=window_.lang, repr='bssdb') #Student Database
	bstools = Buttonbox(text='Tools', lang=window_.lang, repr='bstools') #Database Management
	bsbmm = Buttonbox(text='Back to Main Menu', lang=window_.lang, repr='bsbmm') #Return to Main Menu
	bsexit = Buttonbox(text='Exit', lang=window_.lang, repr='bsexit') #Exit
	bclang = Buttonbox(text='changelanguage', lang=window_.lang, repr='bclang') #Change Language
	bprint = Buttonbox(text='print report', lang=window_.lang, repr='bprint') #Print end of day report
	bexp = Buttonbox(text='expxls', lang=window_.lang, repr='bexp')

	window_.p = Photo(repr='splash', path=os.path.abspath(images + 'background_IMG.jpg'))

	window_.frames["First Frame"].addWidget(bsadd, (1, 0))
	window_.frames["First Frame"].addWidget(bsscan, (2, 0))
	window_.frames["First Frame"].addWidget(bsscan2, (3, 0))
	window_.frames["First Frame"].addWidget(bssdb, (4, 0))
	window_.frames["First Frame"].addWidget(bstools, (5, 0))
	window_.frames["First Frame"].addWidget(bexp, (6, 0))
	window_.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	window_.frames["First Frame"].addWidget(bclang, (7, 0))
	window_.frames["First Frame"].addWidget(bprint, (8, 0))
	window_.frames["First Frame"].addWidget(bsexit, (9, 0))
	window_.frames["First Frame"].addWidget(window_.p, (0, 2))
	Label(window_.frames["First Frame"], text='  ').grid(column=1) #separator between buttons and background image
	
	'''
	dock_frame = AppFrame(window_.frames["First Frame"], bg='#C2DAFF', padx=10, pady=5)
	dock_frame.grid(column=0, row=10, sticky=SE+W, rowspan=100)
	bclang = Buttonbox(text='changelanguage_alt', lang=window_.lang, repr='bclang') #Change Language
	dock_frame.addWidget(bclang, (0, 0))
	window_.frames["First Frame"].grid(sticky=N+W)
	bclang.button.config(width=3)
	'''
	
	bsadd.config(cmd=lambda: showWindow(addS3.main))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bsscan2.config(cmd=lambda: showWindow(scanOut.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main))
	bsbmm.config(cmd=lambda: return_to_main(main_window_.con))
	bprint.config(cmd=printPrompt)
	bsexit.config(cmd=main_window_.destroy)
	bclang.config(cmd=switch_language)
	bexp.config(cmd=expf)
	bstools.selfframe.grid_forget()
	window_.p.label.bind('<Control-Alt-Shift-D>', lambda e: showWindow(tools2.main))

	window_.p.label.grid(rowspan=100, sticky=E)

	window_.mmbuttoncol = '#E3E9F9'
	window_.mmbuttonfg = 'black'

	bsbmm.idlebg = window_.mmbuttoncol
	bsbmm.fg = window_.mmbuttonfg
	bsbmm.hoverfg = 'white'
	bsbmm.button.config(bg=bsbmm.idlebg, fg=bsbmm.fg)

	bsadd.idlebg = window_.mmbuttoncol
	bsadd.fg = window_.mmbuttonfg
	bsadd.hoverfg = 'white'
	bsadd.button.config(bg=bsadd.idlebg, fg=bsadd.fg)

	bsscan.idlebg = window_.mmbuttoncol
	bsscan.fg = window_.mmbuttonfg
	bsscan.hoverfg = 'white'
	bsscan.button.config(bg=bsscan.idlebg, fg=bsscan.fg)

	bsscan2.idlebg = window_.mmbuttoncol
	bsscan2.fg = window_.mmbuttonfg
	bsscan2.hoverfg = 'white'
	bsscan2.button.config(bg=bsscan2.idlebg, fg=bsscan2.fg)

	bssdb.idlebg = window_.mmbuttoncol
	bssdb.fg = window_.mmbuttonfg
	bssdb.hoverfg = 'white'
	bssdb.button.config(bg=bssdb.idlebg, fg=bssdb.fg)

	bclang.idlebg = window_.mmbuttoncol
	bclang.fg = window_.mmbuttonfg
	bclang.hoverfg = 'white'
	bclang.button.config(bg=bclang.idlebg, fg=bclang.fg)

	bsexit.idlebg = window_.mmbuttoncol
	bsexit.fg = window_.mmbuttonfg
	bsexit.hoverfg = 'white'
	bsexit.button.config(bg=bsexit.idlebg, fg=bsexit.fg)

	bprint.idlebg = window_.mmbuttoncol
	bprint.fg = window_.mmbuttonfg
	bprint.hoverfg = 'white'
	bprint.button.config(bg=bprint.idlebg, fg=bprint.fg)

	bstools.idlebg = window_.mmbuttoncol
	bstools.fg = window_.mmbuttonfg
	bstools.hoverfg = 'white'
	bstools.button.config(bg=bstools.idlebg, fg=bstools.fg)

	bexp.idlebg = window_.mmbuttoncol
	bexp.fg = window_.mmbuttonfg
	bexp.hoverfg = 'white'
	bexp.button.config(bg=bexp.idlebg, fg=bexp.fg)

	main_window_.iconbitmap(os.path.abspath(images + 'RYB_Attendance.ico'))
	main_window_.mainloop()

main()