import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')

from tkinter import *
import pickle

from textbox import Textbox, TextboxNoEdit, IntTextbox, MoneyTextbox
from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox
from languages import languages

language = languages["english"]

bok = Buttonbox(text='ok', lang=language, repr='bok')
bsav = Buttonbox(text='Save', lang=language, repr='bsav')
bcancel = Buttonbox(text='Cancel', lang=language, repr='bcancel')

def password_prompt(lang, reset_pw):

	def get_return(z):
		if z == 'pw_mismatch':
			return
		t.z = z
		t.dw()

	t = Mbox()
	#t.root.overrideredirect(0)

	t.newFrame("Top Frame", (0, 0))
	t.newFrame("First Frame", (1, 0))
	t.newFrame("Second Frame", (2, 0))

	no_pw_detected = Labelbox(text="no_pw_set_pw", lang=lang, repr='nopwsetpw')
	old_pw_textbox = Textbox(text="Old Password", lang={"Old Password": "Old Password"}, repr='oldpwtextbox')
	new_pw_textbox = Textbox(text="New Password", lang={"New Password": "New Password"}, repr='newpwtextbox')
	retype_new_pw_textbox = Textbox(text="Retype New Password", lang={"Retype New Password": "Retype New Password"}, repr='retypenewpwtextbox')
	pw_textbox = Textbox(text="Password", lang={"Password": "Password"}, repr='oldpwtextbox')

	if reset_pw:
		t.frames["Top Frame"].addWidget(no_pw_detected, (0, 0))
		t.frames["First Frame"].addWidget(old_pw_textbox, (1, 0))
		t.frames["First Frame"].addWidget(new_pw_textbox, (2, 0))
		t.frames["First Frame"].addWidget(retype_new_pw_textbox, (3, 0))
		t.frames["Second Frame"].addWidget(bsav, (0, 1))
		bsav.config(cmd=lambda: get_return((old_pw_textbox.getData(), new_pw_textbox.getData())) if new_pw_textbox.getData() == retype_new_pw_textbox.getData() else get_return('pw_mismatch'))
		bsav.button.config(width=10)
		old_pw_textbox.label.config(width=19)
		new_pw_textbox.label.config(width=19)
		retype_new_pw_textbox.label.config(width=19)
	else:
		t.frames["First Frame"].addWidget(pw_textbox, (0, 0))
		t.frames["Second Frame"].addWidget(bok, (0, 1))
		bok.config(cmd=lambda: get_return(pw_textbox.getData()))
		bok.button.config(width=10)

	t.frames["Second Frame"].addWidget(bcancel, (0, 0))

	bcancel.button.config(width=10)
	
	bcancel.config(cmd=lambda: get_return('cancel'))


	t.root.wait_window()

	return t.z