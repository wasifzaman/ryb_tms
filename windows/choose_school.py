import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')

from tkinter import *

from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox
from languages import languages

language = languages["english"]

bcancel = Buttonbox(text='Cancel', lang=language, repr='bcancel')

def choose_school(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	t.root.overrideredirect(0)
	t.root.protocol('WM_DELETE_WINDOW', lambda: False)

	t.newFrame("First Frame", (0, 0))

	cstext = Labelbox(text='Choose School', lang=lang, repr='creset')


	button_brooklyn = Buttonbox(text='Brooklyn', lang=lang, repr='bklyn')
	button_elmhurst = Buttonbox(text='Elmhurst', lang=lang, repr='el')
	button_flushing = Buttonbox(text='Flushing', lang=lang, repr='flu')
	button_chinatown = Buttonbox(text='Chinatown', lang=lang, repr='ct')


	t.frames["First Frame"].addWidget(button_flushing, (0, 0))
	t.frames["First Frame"].addWidget(button_chinatown, (1, 0))
	t.frames["First Frame"].addWidget(button_elmhurst, (2, 0))
	t.frames["First Frame"].addWidget(button_brooklyn, (3, 0))
	t.frames["First Frame"].addWidget(bcancel, (4, 0))

	button_brooklyn.config(cmd=lambda: d('Brooklyn'), lang=lang)
	button_elmhurst.config(cmd=lambda: d('Elmhurst'), lang=lang)
	button_flushing.config(cmd=lambda: d('Flushing'), lang=lang)
	button_chinatown.config(cmd=lambda: d('Chinatown'), lang=lang)
	bcancel.config(cmd=lambda: d('cancel'), lang=lang)

	t.root.wait_window()
	
	return t.z