import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')

from tkinter import *

from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox
from photoWidget2 import Photo
from languages import languages

language = languages["english"]

hs = Photo(repr='hs', path='halt_sm.png')
ws = Photo(repr='ws', path='ws_sm.png')
bok = Buttonbox(text='ok', lang=language, repr='bok')

def nos(lang):
	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='No student', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def date_error(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Invalid Date', lang=lang, repr='invaliddate')
	breturn = Buttonbox(text='Return', lang=lang, repr='ok_')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(breturn, (2, 0))
	
	breturn.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

def invalid_path(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Invalid Path', lang={'Invalid Path': 'Invalid Path'}, repr='invaliddate')
	breturn = Buttonbox(text='Return', lang=lang, repr='ok_')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(breturn, (2, 0))
	
	breturn.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

def checkout_earlier_checkin(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	checkout_earlier_checkin_ = Labelbox(text='Check-Out Cannot be earlier than Check-In',
		lang=lang, 
		repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(checkout_earlier_checkin_, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def entry_not_found(lang, date):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	entry_not_found_ = Labelbox(text='No Check-In on that Date',
		lang=lang, 
		repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(entry_not_found_, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	entry_not_found_.label.config(text=entry_not_found_.label.cget('text') + ' ' + date)

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def deny_checkout_future(lang, date):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	entry_not_found_ = Labelbox(text='Cannot Check-In a future time',
		lang=lang, 
		repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(entry_not_found_, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	entry_not_found_.label.config(text=entry_not_found_.label.cget('text') + ' ' + date)

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def wrong_password(lang):

	t = Mbox()
	t.root.overrideredirect(0)
	
	t.newFrame("First Frame", (0, 0))

	wrong_pw_label = Labelbox(text='wrong password try again', lang=lang, repr='wrongpwtryagain')

	t.frames["First Frame"].addWidget(wrong_pw_label, (0, 0))
	t.frames["First Frame"].addWidget(bok, (1, 0))

	bok.config(cmd=t.dw)

	t.root.wait_window()

	return

def invalid_file_type(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	fimport = Labelbox(text='Invalid File Type', lang=lang, repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(fimport, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def no_checkin_today(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	fimport = Labelbox(text='No Check-in today', lang=lang, repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(fimport, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()