import sys, os, shutil
sys.path.append(os.path.abspath(os.pardir) + '\messages windows')
temp = os.path.abspath(os.pardir) + '\\temp\\'

from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from tkinter import filedialog
from random import randrange
from master_list import *

def main(lang, database):
	def open_excel():
		excel_file = filedialog.askopenfile(mode='r')
		if excel_file != None:
			source_path.setData(excel_file.name)
		
	def preview_database():
		if hasattr(window_, 'randfile') and os.path.exists(window_.randfile):
			os.remove(window_.randfile)
		if hasattr(window_, 'randpwfile') and os.path.exists(window_.randpwfile):
			os.remove(window_.randpwfile)

		if len(source_path.getData()) == 0: return

		rand_int = str(randrange(0, 100000))
		window_.randfile = temp + '\\temp' + rand_int + '.rybdb'
		window_.randpwfile = temp + '\\temp_pw_file' + rand_int + '.rybdb'
		new_database = StudentDB(file=window_.randfile, cfile='', pwfile=window_.randpwfile)
		
		try:
			new_database.importxlsx(source_path.getData())
		except xlrd.biffh.XLRDError:
			invalid_file_type(window_.lang)
			os.remove(window_.randfile)
			os.remove(window_.randpwfile)

		student_list = []
		for student in new_database.studentList.values():
			data_points = student.datapoints
			student_list.append([data_points['bCode'], data_points['firstName'], data_points['lastName'], data_points['chineseName'], data_points['dob']])

		student_list.sort()
		window_.student_table.setData((window_.student_table_headers, student_list))
		window_.student_table.canvas.config(width=700)

	def set_file(textbox):
		out_file = filedialog.asksaveasfilename()
		if len(out_file) != 0:
			textbox.setData(out_file + '.rybdb')
		out_file = out_file.split('/')
		file_name = out_file[-1]
		dest_path = '/'.join(out_file[:-1])

	def save_():
		if len(dest_path.getData()) == 0 or \
			len(source_path.getData()) == 0 or \
			len(pw_fpath.getData()) == 0 or \
			not hasattr(window_, 'randfile'):
			return
		out_file = dest_path.getData().split('/')
		file_name = temp + out_file[-1]
		dest_path_ = '/'.join(out_file[:-1])
		pw_out_file = pw_fpath.getData().split('/')
		pw_file_name = temp + pw_out_file[-1]
		pw_dest_path = '/'.join(out_file[:-1])

		os.rename(window_.randfile, file_name)
		os.rename(window_.randpwfile, pw_file_name)
		shutil.move(file_name, dest_path_)
		shutil.move(pw_file_name, pw_dest_path)

		top_window_.destroy()

	def exit_():
		if hasattr(window_, 'randfile') and os.path.exists(window_.randfile):
			os.remove(window_.randfile)
		if hasattr(window_, 'randpwfile') and os.path.exists(window_.randpwfile):
			os.remove(window_.randpwfile)

		top_window_.destroy()

	database.loadData()

	top_window_ = Window(top=True)
	top_window_.geometry('900x500')
	top_window_.attributes('-fullscreen', False)
	top_window_.focus_set()
	top_window_.grab_set()
	top_window_.titleFrame.pack_forget()

	window_ = AppWindow(top_window_.mainFrame)
	window_.lang = lang

	window_.student_table = Table(repr='stable', edit=False)
	window_.student_table_headers = [window_.lang['Barcode'], window_.lang['First Name'], \
		window_.lang['Last Name'], window_.lang['Chinese Name'], window_.lang['Date of Birth']]
	window_.student_table.build(headers=window_.student_table_headers, data=[[]])

	window_.newFrame("Open Excel Frame", (0, 0))
	window_.newFrame("Table Frame", (1, 0))
	window_.newFrame("Password File Frame", (2, 0))
	window_.newFrame("Confirm Frame", (3, 0))

	window_.bsav = bsav
	source_path = TextboxNoEdit(text='Source Excel', lang=window_.lang, repr='sourceexcel')
	dest_path = TextboxNoEdit(text='Output File', lang=window_.lang, repr='outputfile')
	pw_fpath = TextboxNoEdit(text='Password File', lang=window_.lang, repr='pwfilepath')
	pw_fpath_brw = Buttonbox(text='browse', lang=window_.lang, repr='pwfilebrw')
	preview_button = Buttonbox(text='Preview', lang=window_.lang, repr='previewbutton')
	bcancel1 = Buttonbox(text='Cancel', lang=window_.lang, repr='cancel')
	
	window_.frames["Open Excel Frame"].addWidget(source_path, (0, 0))
	window_.frames["Open Excel Frame"].addWidget(brw, (0, 2))
	window_.frames["Open Excel Frame"].addWidget(preview_button, (0, 3))
	window_.frames["Table Frame"].addWidget(window_.student_table, (1, 0))
	window_.frames["Password File Frame"].addWidget(dest_path, (1, 0))
	window_.frames["Password File Frame"].addWidget(brw2, (1, 3))
	window_.frames["Password File Frame"].addWidget(pw_fpath, (2, 0))
	window_.frames["Password File Frame"].addWidget(pw_fpath_brw, (2, 3))
	window_.frames["Confirm Frame"].addWidget(window_.bsav, (3, 1))
	window_.frames["Confirm Frame"].addWidget(bcancel1, (3, 2))

	brw.config(cmd=open_excel)
	brw2.config(cmd=lambda: set_file(dest_path))
	pw_fpath_brw.config(cmd=lambda: set_file(pw_fpath))
	preview_button.config(cmd=preview_database)
	window_.bsav.config(cmd=save_)
	bcancel1.config(cmd=exit_)

	brw.button.config(width=12, pady=1)
	brw.selfframe.grid(padx=10)
	brw2.button.config(width=12, pady=1)
	brw2.selfframe.grid(padx=10)
	pw_fpath_brw.button.config(width=12, pady=1)
	pw_fpath_brw.selfframe.grid(padx=10)
	preview_button.button.config(width=10, pady=1)
	window_.bsav.button.config(width=10)
	window_.bsav.selfframe.grid(padx=10)
	bcancel1.button.config(width=10)
	bcancel1.selfframe.grid(padx=10)
	
	for frame in window_.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=window_.lang)
	
	top_window_.mainloop()