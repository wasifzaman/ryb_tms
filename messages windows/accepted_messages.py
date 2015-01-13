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

language = languages["english"]

ws = Photo(repr='ws', path=images + 'ws_sm.png')
hs = Photo(repr='hs', path=images + 'halt_sm.png')
cm = Photo(repr='cm', path=images + 'check_mark_sm.png')
bok = Buttonbox(text='ok', lang=language, repr='bok')

def sa(s, lang):


	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	t.frames["First Frame"].addWidget(cm, (0, 0))
	t.frames["Second Frame"].addWidget(bok, (4, 0))

	satext = Labelbox(text='Sa student', lang=lang, repr='satext')
	
	t.frames["First Frame"].addWidget(satext, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def print_succesful(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Print Successful', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

	return t.z

def teacher_report_print_successful(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Teacher Print Successful', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

	return t.z

def pw_reset_confirm(lang):

	t = Mbox()
	t.root.overrideredirect(0)
	
	t.newFrame("First Frame", (0, 0))

	t.frames["First Frame"].addWidget(bok, (1, 0))

	confirmed_reset = Labelbox(text='confirmed reset', lang=lang, repr='confirmedreset')

	t.frames["First Frame"].addWidget(confirmed_reset, (0, 0))
	t.frames["First Frame"].addWidget(bok, (1, 0))

	bok.config(cmd=t.dw)

	t.root.wait_window()

	return

def database_backup_successful(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Database Backup Successful', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

	return t.z

def reset_confirmation(lang, value):

	if value != True: return

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	dbupdate = Labelbox(text='Early Check-ins have been reset', lang=lang, repr='dbupdate')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(dbupdate, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

'''
** depreciated? **
def dbs(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	dbupdate = Labelbox(text='Database succesfully updated!', lang=lang, repr='dbupdate')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(dbupdate, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()
'''