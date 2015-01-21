import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')

from tkinter import *

from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox


def choose_school(lang):
	def d(z):
		message_box.z = z
		message_box.dw()

	message_box = Mbox()
	message_box.root.protocol('WM_DELETE_WINDOW', lambda: False)

	message_box.newFrame("First Frame", (0, 0))

	button_brooklyn = Buttonbox(text='Brooklyn', lang=lang, repr='bklyn')
	button_elmhurst = Buttonbox(text='Elmhurst', lang=lang, repr='el')
	button_flushing = Buttonbox(text='Flushing', lang=lang, repr='flu')
	button_chinatown = Buttonbox(text='Chinatown', lang=lang, repr='ct')
	bcancel = Buttonbox(text='Cancel', lang=lang, repr='bcancel')

	message_box.frames["First Frame"].addWidget(button_flushing, (0, 0))
	message_box.frames["First Frame"].addWidget(button_chinatown, (1, 0))
	message_box.frames["First Frame"].addWidget(button_elmhurst, (2, 0))
	message_box.frames["First Frame"].addWidget(button_brooklyn, (3, 0))
	message_box.frames["First Frame"].addWidget(bcancel, (4, 0))

	button_brooklyn.config(cmd=lambda: d('Brooklyn'), lang=lang)
	button_elmhurst.config(cmd=lambda: d('Elmhurst'), lang=lang)
	button_flushing.config(cmd=lambda: d('Flushing'), lang=lang)
	button_chinatown.config(cmd=lambda: d('Chinatown'), lang=lang)
	bcancel.config(cmd=lambda: d('cancel'), lang=lang)

	bcancel.idlebg = 'tomato'
	bcancel.fg = 'black'
	bcancel.hoverfg = 'white'
	bcancel.hoverbg = 'crimson'
	bcancel.button.config(bg=bcancel.idlebg, fg=bcancel.fg)

	message_box.root.wait_window()
	
	return message_box.z