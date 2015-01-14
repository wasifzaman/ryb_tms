import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir) + '\miscellaneous')
sys.path.append(os.path.abspath(os.pardir) + '\windows')
images = os.path.abspath(os.pardir) + '\images\\'


from tkinter import *
from datetime import datetime
import tkinter.ttk as ttk

from mbox2 import Mbox
from uiHandler22 import *
from date_textbox import Datebox
from button import Buttonbox
from simple_label import Labelbox
from photoWidget2 import Photo
from languages import languages
from deny_messages import date_error

language = languages["english"]

hs = Photo(repr='hs', path=images + 'halt_sm.png')
ws = Photo(repr='ws', path=images + 'ws_sm.png')

def date_to_date(lang):
	def return_():
		if start_date_input.getData() == '01/01/1900' or \
			end_date_input.getData() == '01/01/1900':
			date_error(lang)
			return	
		confirm_date_range.start_date_input = datetime.strptime(start_date_input.getData(), '%m/%d/%Y')
		confirm_date_range.end_date_input = datetime.strptime(end_date_input.getData(), '%m/%d/%Y')
		confirm_date_range.root.destroy()

	confirm_date_range = Mbox()
	confirm_date_range.root.resizable(0, 0)
	confirm_date_range.root.grab_set()
	confirm_date_range.root.focus_set()
	confirm_date_range.start_date_input = False
	confirm_date_range.end_date_input = False

	confirm_window = AppWindow(confirm_date_range.mainFrame)

	start_date_input = Datebox(text='Date', lang=lang, repr='dateinput')
	end_date_input = Datebox(text='Date', lang=lang, repr='dateinput')
	return_button = Buttonbox(text='Confirm', lang=lang, repr='rbutton')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancelbutton')

	confirm_window.newFrame("First Frame", (0, 0))
	confirm_window.newFrame("Button Frame", (1, 0))

	confirm_window.frames["First Frame"].addWidget(start_date_input, (0, 0))
	confirm_window.frames["First Frame"].addWidget(end_date_input, (1, 0))
	confirm_window.frames["Button Frame"].addWidget(return_button, (1, 0))
	confirm_window.frames["Button Frame"].addWidget(cancel_button, (2, 0))

	return_button.selfframe.grid(columnspan=6, pady=(20, 0))
	cancel_button.selfframe.grid(columnspan=6)
	start_date_input.label.config(width=11)
	end_date_input.label.config(width=11)

	return_button.config(cmd=return_)
	cancel_button.config(cmd=confirm_date_range.root.destroy)

	confirm_date_range.root.wait_window()

	return confirm_date_range.start_date_input, confirm_date_range.end_date_input