import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')

from tkinter import *
from datetime import datetime

from mbox2 import Mbox
from textbox import Textbox, TextboxNoEdit, IntTextbox, MoneyTextbox
from button import Buttonbox
from simple_label import Labelbox
from photoWidget2 import Photo
from languages import languages

language = languages["english"]

hs = Photo(repr='hs', path='halt_sm.png')
ws = Photo(repr='ws', path='ws_sm.png')
byes = Buttonbox(text='yes', lang=language, repr='byes')
bno = Buttonbox(text='no', lang=language, repr='bno')
bcancel = Buttonbox(text='Cancel', lang=language, repr='bcancel')

def con(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	context = Labelbox(text='Con student', lang=lang, repr='context')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(context, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bno.button.focus_set()

	t.root.wait_window()

	return t.z

def conS(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	constext = Labelbox(text='Con S student', lang=lang, repr='constext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(constext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)

	t.root.wait_window()

	return t.z

def ase(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	asetext = Labelbox(text='Ase student', lang=lang, repr='asetext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(asetext, (2, 0))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bno.button.focus_set()

	t.root.wait_window()

	return t.z

def cs(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Cs student', lang=lang, repr='cstext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def csout(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='cstext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def confirm_check_in_time(lang, database):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')

	timeslot = database.findTimeSlot(datetime.now())

	byes_current_time = Buttonbox(text='Check-in', lang=lang, repr='bok')
	byes_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='bnok')

	byes_current_time.width = 20
	byes_enter_time.width = 20

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes_current_time, (0, 0))
	t.frames["Second Frame"].addWidget(byes_enter_time, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes_current_time.selfframe.grid(sticky=E+W, padx=5)
	byes_enter_time.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes_current_time.config(cmd=lambda: return_(True))
	byes_enter_time.config(cmd=lambda: return_('manual'))
	bcancel.config(cmd=lambda: return_(False))
	byes_current_time_text = byes_current_time.button.cget('text')
	byes_current_time.button.config(
		text=byes_current_time_text + ' ' + timeslot)
	
	t.root.wait_window()

	return t.value

def confirm_overwrite_checkout(lang):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Checkout', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: return_(True), lang=lang)
	bno.config(cmd=lambda: return_(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.value

def confirm_check_out_time(lang, database):
	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')
	
	timeslot = database.findTimeSlot(datetime.now())

	byes_current_time = Buttonbox(text='Check-out', lang=lang, repr='bok')
	byes_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='bnok')

	byes_current_time.width = 20
	byes_enter_time.width = 20

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes_current_time, (0, 0))
	t.frames["Second Frame"].addWidget(byes_enter_time, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes_current_time.selfframe.grid(sticky=E+W, padx=5)
	byes_enter_time.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes_current_time.config(cmd=lambda: return_(True), lang=lang)
	byes_enter_time.config(cmd=lambda: return_('manual'), lang=lang)
	bcancel.config(cmd=lambda: return_(False), lang=lang)
	byes_current_time_text = byes_current_time.button.cget('text')
	byes_current_time.button.config(
		text=byes_current_time_text + ' ' + timeslot)

	t.root.wait_window()

	return t.value

def confirm_print(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Con print', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def confirm_reset(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Confirm Reset', lang=lang, repr='creset')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bcancel.config(cmd=lambda: d('cancel'), lang=lang)

	t.root.wait_window()

	return t.z

def ret(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	rettext = Labelbox(text='Ret to Main', lang=lang, repr='rettext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(rettext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bno.button.focus_set()

	t.root.wait_window()

	return t.z

def confirm_check_in_time(lang, database):
	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')

	timeslot = database.findTimeSlot(datetime.now())

	byes_current_time = Buttonbox(text='Check-in', lang=lang, repr='bok')
	byes_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='bnok')

	byes_current_time.width = 20
	byes_enter_time.width = 20

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes_current_time, (0, 0))
	t.frames["Second Frame"].addWidget(byes_enter_time, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes_current_time.selfframe.grid(sticky=E+W, padx=5)
	byes_enter_time.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes_current_time.config(cmd=lambda: return_(True))
	byes_enter_time.config(cmd=lambda: return_('manual'))
	bcancel.config(cmd=lambda: return_(False))
	byes_current_time_text = byes_current_time.button.cget('text')
	byes_current_time.button.config(
		text=byes_current_time_text + ' ' + timeslot)
	
	t.root.wait_window()

	return t.value

def confirm_overwrite_checkout(lang):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Checkout', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: return_(True), lang=lang)
	bno.config(cmd=lambda: return_(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.value

def confirm_overwrite_checkin(lang):
	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Check-In', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: return_(True), lang=lang)
	bno.config(cmd=lambda: return_(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.value

def confirm_check_out_time(lang, database):
	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')
	
	timeslot = database.findTimeSlot(datetime.now())

	byes_current_time = Buttonbox(text='Check-out', lang=lang, repr='bok')
	byes_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='bnok')

	byes_current_time.width = 20
	byes_enter_time.width = 20

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes_current_time, (0, 0))
	t.frames["Second Frame"].addWidget(byes_enter_time, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes_current_time.selfframe.grid(sticky=E+W, padx=5)
	byes_enter_time.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes_current_time.config(cmd=lambda: return_(True), lang=lang)
	byes_enter_time.config(cmd=lambda: return_('manual'), lang=lang)
	bcancel.config(cmd=lambda: return_(False), lang=lang)
	byes_current_time_text = byes_current_time.button.cget('text')
	byes_current_time.button.config(
		text=byes_current_time_text + ' ' + timeslot)

	t.root.wait_window()

	return t.value

'''
** depreciated?? **
def pchoosefile(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	pchoosefiletext = Labelbox(text='Please choose a file', lang=lang, repr='pchoosefiletext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(pchoosefiletext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()
'''