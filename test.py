from tkinter import *
from alpha_ui import *
from dataHandler import *
from languages import *
from labelWidgets2 import *
from photoWidget2 import *
from tkinter import filedialog

#modules
import addS3


def main():

	#button functions
	
	def change_language():
		if main_app_window.lang['self'] == 'english':
			main_app_window.lang = languages['chinese']
		else:
			main_app_window.lang = languages['english']
		for frame in main_app_window.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=main_app_window.lang)

	def showWindow(func_input):
		main_app_window.menu_frame.grid_forget()
		main_app_window.main_image_frame.grid_forget()
		if (func_input.__doc__) == 'addS3':
			main_app_window.t = func_input(main_app_window.app_frame, main_app_window.lang, main_app_window.teacher_database, showMain)
		else:
			main_app_window.t = func_input(main_app_window.app_frame, main_app_window.lang, main_app_window.teacher_database)
		main_app_window.app_frame.grid()
		main_app_window.return_button_frame.grid()

	def showMain(con):
		main_app_window.app_frame.grid_forget()

		for child in main_app_window.app_frame.winfo_children():
			child.destroy()

		main_app_window.app_frame.destroy()
		main_app_window.app_frame = main_app_window.newFrame("App Frame", (1, 1))
		main_app_window.app_frame.grid_forget()

		main_app_window.menu_frame.grid()
		main_app_window.main_image_frame.grid()
		main_app_window.return_button_frame.grid_forget()

		main_app_window.program_settings.files['cfilepath'] = main_app_window.teacher_database.file
		main_app_window.program_settings.save()

	def printPrompt():

		def out():
			file_name = filedialog.asksaveasfilename()

			try:
				main_app_window.teacher_database.exportreport(file_name, report_date.getData())
			except:
				return

			print_window.destroy()

		print_window = Window(top=True)
		print_window.attributes('-fullscreen', False)
		print_window.resizable(0, 0)
		print_window.geometry('400x200+200+200')
		print_window.float()

		main_print_window = AppWindow(print_window.mainFrame, (1, 1))

		main_print_window.main_app_frame = main_print_window.newFrame("First Frame")

		report_date = Datebox(text=main_app_window.lang['sdate'], lang=main_app_window.lang, repr='rdate')
		print_report_button = Buttonbox(text='Select Folder', lang=main_app_window.lang, repr='print_report_button')	

		main_print_window.main_app_frame.addWidget(report_date, (0, 0))
		main_print_window.main_app_frame.addWidget(print_report_button, (1, 0))

		report_date.label.destroy()
		print_report_button.selfframe.grid(columnspan=2, pady=20)

		print_report_button.config(cmd=out)

	main_window = Window(top=False)
	main_window.attributes('-fullscreen', False)
	main_window.geometry('1440x900+100+100')
	main_window.wintitle.config(text='RYB Student Management')

	main_app_window = AppWindow(main_window.main_frame, num_rows=3, num_columns=2)
	main_app_window.lang = languages['english']

	main_app_window.program_settings = keeper.Keeper('keeper.db')
	main_app_window.teacher_database = StudentDB(file=main_app_window.program_settings.files['cfilepath'], cfile=main_app_window.program_settings.fname)

	main_app_window.menu_frame = main_app_window.newFrame("Menu Frame", (4, 8), column=0)
	main_app_window.main_image_frame = main_app_window.newFrame("Main Image Frame", (1, 1), column=1)
	main_app_window.app_frame = main_app_window.newFrame("App Frame", (1, 1))
	main_app_window.return_button_frame = main_app_window.newFrame("Return Button Frame", (1, 1))

	#main_app_window.app_frame.grid_forget()
	#main_app_window.return_button_frame.grid_forget()

	button_add_student = Buttonbox(text='Add Students', lang=main_app_window.lang, repr='bsadd')
	button_scan_in_teacher = Buttonbox(text='Scan Students', lang=main_app_window.lang, repr='bsscan')
	button_scan_out_teacher = Buttonbox(text='Scan Out Teacher', lang=main_app_window.lang, repr='bsscan')
	button_studentdb = Buttonbox(text='Student Database', lang=main_app_window.lang, repr='bssdb')
	button_tools = Buttonbox(text='Tools', lang=main_app_window.lang, repr='bstools')
	button_back_to_menu = Buttonbox(text='Back to Main Menu', lang=main_app_window.lang, repr='bsbmm')
	button_exit = Buttonbox(text='Exit', lang=main_app_window.lang, repr='bsexit')
	button_change_language = Buttonbox(text='changelanguage', lang=main_app_window.lang, repr='bclang')
	button_print_report = Buttonbox(text='print report', lang=main_app_window.lang, repr='bprint')
	main_app_window.main_image = Photo(repr='splash', path='background_IMG.jpg')

	main_app_window.menu_frame.addWidget(button_add_student, column=0)
	main_app_window.menu_frame.addWidget(button_scan_in_teacher, column=0)
	main_app_window.menu_frame.addWidget(button_scan_out_teacher, column=0)
	main_app_window.menu_frame.addWidget(button_studentdb, column=0)
	main_app_window.menu_frame.addWidget(button_tools, column=0)
	main_app_window.menu_frame.addWidget(button_print_report, column=0)
	main_app_window.menu_frame.addWidget(button_exit, column=0)
	main_app_window.menu_frame.addWidget(button_change_language, column=0)
	main_app_window.return_button_frame.addWidget(button_back_to_menu)
	main_app_window.main_image_frame.addWidget(main_app_window.main_image)

	button_add_student.config(cmd=lambda: showWindow(addS3.main))





	main_window.mainloop()


if __name__ == '__main__':
	main()