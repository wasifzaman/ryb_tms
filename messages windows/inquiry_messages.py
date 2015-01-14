import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
images = os.path.abspath(os.pardir) + '\images\\'

from tkinter import *
from datetime import datetime

from mbox2 import Mbox
from textbox import Textbox, TextboxNoEdit, IntTextbox, MoneyTextbox
from button import Buttonbox
from simple_label import Labelbox
from photoWidget2 import Photo
from languages import languages


def con(s, lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.title_.config(text='TEST')

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	context = Labelbox(text='Con student', lang=lang, repr='context')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(context, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	no_button.button.focus_set()

	verify_image.label.config(width=80)
	context.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def conS(s, lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	constext = Labelbox(text='Con S student', lang=lang, repr='constext')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(constext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)

	verify_image.label.config(width=80)
	constext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def ase(s, lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	asetext = Labelbox(text='Ase student', lang=lang, repr='asetext')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(asetext, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	no_button.button.focus_set()

	verify_image.label.config(width=80)
	asetext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def cs(s, lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Cs student', lang=lang, repr='cstext')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	yes_button.button.focus_set()

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def csout(s, lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='cstext')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	yes_button.button.focus_set()

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def confirm_check_in_time(lang, database):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	timeslot = database.findTimeSlot(datetime.now())

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')
	yes_button_current_time = Buttonbox(text='Check-in', lang=lang, repr='bok')
	yes_button_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='no_buttonk')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancel_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	yes_button_current_time.width = 20
	yes_button_enter_time.width = 20

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button_current_time, (0, 0))
	message_box.frames["Second Frame"].addWidget(yes_button_enter_time, (1, 0))
	message_box.frames["Second Frame"].addWidget(cancel_button, (2, 0))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button_current_time.selfframe.grid(sticky=E+W)
	yes_button_enter_time.selfframe.grid(sticky=E+W)
	cancel_button.selfframe.grid(sticky=E+W)
	yes_button_current_time.button.pack(fill=X)
	yes_button_enter_time.button.pack(fill=X)
	cancel_button.button.pack(fill=X)
	yes_button_current_time.config(cmd=lambda: return_(True))
	yes_button_enter_time.config(cmd=lambda: return_('manual'))
	cancel_button.config(cmd=lambda: return_(False))
	yes_button_current_time_text = yes_button_current_time.button.cget('text')
	yes_button_current_time.button.config(
		text=yes_button_current_time_text + ' ' + timeslot)
	
	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def confirm_check_out_time(lang, database):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	timeslot = database.findTimeSlot(datetime.now())

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')
	yes_button_current_time = Buttonbox(text='Check-out', lang=lang, repr='bok')
	yes_button_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='no_buttonk')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancel_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	yes_button_current_time.width = 20
	yes_button_enter_time.width = 20

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button_current_time, (0, 0))
	message_box.frames["Second Frame"].addWidget(yes_button_enter_time, (1, 0))
	message_box.frames["Second Frame"].addWidget(cancel_button, (2, 0))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button_current_time.selfframe.grid(sticky=E+W)
	yes_button_enter_time.selfframe.grid(sticky=E+W)
	cancel_button.selfframe.grid(sticky=E+W)
	yes_button_current_time.button.pack(fill=X)
	yes_button_enter_time.button.pack(fill=X)
	cancel_button.button.pack(fill=X)
	yes_button_current_time.config(cmd=lambda: return_(True), lang=lang)
	yes_button_enter_time.config(cmd=lambda: return_('manual'), lang=lang)
	cancel_button.config(cmd=lambda: return_(False))
	yes_button_current_time_text = yes_button_current_time.button.cget('text')
	yes_button_current_time.button.config(
		text=yes_button_current_time_text + ' ' + timeslot)

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def confirm_overwrite_checkout(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Checkout', lang=lang, repr='cprint')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	yes_button.button.focus_set()

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def confirm_print(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Con print', lang=lang, repr='cprint')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	yes_button.button.focus_set()

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def confirm_reset(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Confirm Reset', lang=lang, repr='creset')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancel_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["Second Frame"].addWidget(cancel_button, (0, 2))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	cancel_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	cancel_button.config(cmd=lambda: d('cancel'), width=10)

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def ret(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	rettext = Labelbox(text='Ret to Main', lang=lang, repr='rettext')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(rettext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	no_button.button.focus_set()

	verify_image.label.config(width=80)
	rettext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

def confirm_overwrite_checkin(lang):
	def return_(value):
		message_box.value = value
		message_box.dw()

	message_box = Mbox()

	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Check-In', lang=lang, repr='cprint')
	yes_button = Buttonbox(text='yes', lang=lang, repr='yes_button')
	no_button = Buttonbox(text='no', lang=lang, repr='no_button')
	verify_image = Photo(repr='verify_image', path=images + 'halt_sm.png')

	message_box.frames["First Frame"].addWidget(cstext, (0, 1))
	message_box.frames["Second Frame"].addWidget(yes_button, (0, 0))
	message_box.frames["Second Frame"].addWidget(no_button, (0, 1))
	message_box.frames["First Frame"].addWidget(verify_image, (0, 0))

	yes_button.selfframe.grid(sticky=E+W, padx=5)
	no_button.selfframe.grid(sticky=E+W, padx=5)
	yes_button.config(cmd=lambda: return_(True), width=10)
	no_button.config(cmd=lambda: return_(False), width=10)
	yes_button.button.focus_set()

	verify_image.label.config(width=80)
	cstext.label.config(wraplength=200, justify=LEFT)
	message_box.root.wait_window()

	return message_box.value

'''
** depreciated?? **
def pchoosefile(lang):

	message_box = Mbox()
	
	message_box.newFrame("First Frame", (0, 0))
	message_box.newFrame("Second Frame", (1, 0))

	pchoosefiletext = Labelbox(text='Please choose a file', lang=lang, repr='pchoosefiletext')

	message_box.frames["First Frame"].addWidget(ws, (0, 0))
	message_box.frames["First Frame"].addWidget(pchoosefiletext, (1, 0))
	message_box.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=message_box.dw, lang=lang)

	message_box.root.wait_window()
'''