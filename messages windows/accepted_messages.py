import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
images = os.path.abspath(os.pardir) + '\images\\'

from tkinter import *

from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox
from photoWidget2 import Photo
from languages import languages


def teacher_added(lang):
	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	teacher_added_text = Labelbox(text='Teacher has been added to the database', lang=lang, repr='tatext')
	confirm_image = Photo(repr='confirm_image', path=images + 'check_mark_sm.png')
	ok_button = Buttonbox(text='ok', lang=lang, repr='ok_button')
	
	message_box.frames["First Frame"].addWidget(confirm_image, (0, 0))
	message_box.frames["First Frame"].addWidget(teacher_added_text, (0, 1))
	message_box.frames["Second Frame"].addWidget(ok_button, (0, 0))

	confirm_image.label.grid(padx=5, pady=5)
	teacher_added_text.label.config(wraplength=200)
	ok_button.config(cmd=message_box.dw, lang=lang, width=10)

	message_box.root.wait_window()

def print_succesful(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	print_succesful_text = Labelbox(text='Print Successful', lang=lang, repr='printsuccesful')
	confirm_image = Photo(repr='confirm_image', path=images + 'check_mark_sm.png')
	ok_button = Buttonbox(text='ok', lang=lang, repr='ok_button')

	message_box.frames["First Frame"].addWidget(confirm_image, (0, 0))
	message_box.frames["First Frame"].addWidget(print_succesful_text, (1, 0))
	message_box.frames["Second Frame"].addWidget(ok_button, (2, 0))
	
	ok_button.config(cmd=lambda: return_(True), lang=lang)

	message_box.root.wait_window()

	return message_box.value

def teacher_report_print_successful(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()
	
	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	teacher_report_printed_text = Labelbox(text='Teacher Print Successful', lang=lang, repr='teacherreportprinted')
	confirm_image = Photo(repr='confirm_image', path=images + 'check_mark_sm.png')
	ok_button = Buttonbox(text='ok', lang=lang, repr='ok_button')

	message_box.frames["First Frame"].addWidget(confirm_image, (0, 0))
	message_box.frames["First Frame"].addWidget(teacher_report_printed_text, (1, 0))
	message_box.frames["Second Frame"].addWidget(ok_button, (2, 0))
	
	ok_button.config(cmd=lambda: return_(True), lang=lang)

	message_box.root.wait_window()

	return message_box.value

def pw_reset_confirm(lang):
	message_box = Mbox()
	message_box.root.overrideredirect(0)
	
	message_box.newFrame("First Frame", (0, 0))

	confirmed_reset_text = Labelbox(text='confirmed reset', lang=lang, repr='confirmedreset')
	ok_button = Buttonbox(text='ok', lang=lang, repr='ok_button')

	message_box.frames["First Frame"].addWidget(confirmed_reset_text, (0, 0))
	message_box.frames["First Frame"].addWidget(ok_button, (1, 0))

	ok_button.config(cmd=message_box.dw)

	message_box.root.wait_window()

def database_backup_successful(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()
	
	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	db_backup_success_text = Labelbox(text='Database Backup Successful', lang=lang, repr='dbbackupsuccess')
	confirm_image = Photo(repr='confirm_image', path=images + 'check_mark_sm.png')
	ok_button = Buttonbox(text='ok', lang=lang, repr='ok_button')

	message_box.frames["First Frame"].addWidget(confirm_image, (0, 0))
	message_box.frames["First Frame"].addWidget(db_backup_success_text, (1, 0))
	message_box.frames["Second Frame"].addWidget(ok_button, (2, 0))
	
	ok_button.config(cmd=lambda: return_(True), lang=lang)

	message_box.root.wait_window()

	return message_box.value

def reset_confirmation(lang, value):
	if value != True: return

	message_box = Mbox()
	
	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	early_checkin_reset_text = Labelbox(text='Early Check-ins have been reset', lang=lang, repr='earlycheckinreset')
	confirm_image = Photo(repr='confirm_image', path=images + 'check_mark_sm.png')
	ok_button = Buttonbox(text='ok', lang=lang, repr='ok_button')

	message_box.frames["First Frame"].addWidget(confirm_image, (0, 0))
	message_box.frames["First Frame"].addWidget(early_checkin_reset_text, (1, 0))
	message_box.frames["Second Frame"].addWidget(ok_button, (2, 0))

	ok_button.config(cmd=message_box.dw, lang=lang)

	message_box.root.wait_window()

'''
** depreciated? **
def dbs(lang):

	message_box = Mbox()
	
	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	dbupdate = Labelbox(text='Database succesfully updated!', lang=lang, repr='dbupdate')

	message_box.frames["First Frame"].addWidget(warning_image, (0, 0))
	message_box.frames["First Frame"].addWidget(dbupdate, (1, 0))
	message_box.frames["Second Frame"].addWidget(ok_button, (2, 0))

	ok_button.config(cmd=message_box.dw, lang=lang)

	message_box.root.wait_window()
'''