import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')

from tkinter import *
from datetime import datetime
import tkinter.ttk as ttk

from uiHandler22 import *
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

def time_entry(lang):

	def return_():
		time_input = hour_input_stringvar.get() + ':' + minute_input_stringvar.get() + ' ' + am_pm_stringvar.get()
		dt = datetime.strftime(datetime.strptime(time_input, '%I:%M %p'), '%I:%M %p')
		confirm_time.time_input_confirmed = dt
		confirm_time.destroy()

	confirm_time = Window(top=True)
	confirm_time.attributes('-fullscreen', False)
	confirm_time.resizable(0, 0)
	confirm_time.geometry('400x200+200+200')
	confirm_time.grab_set()
	confirm_time.focus_set()
	confirm_time.titleFrame.pack_forget()
	confirm_time.time_input_confirmed = False

	confirm_window = AppWindow(confirm_time.mainFrame)

	hour_input_stringvar = StringVar()
	minute_input_stringvar = StringVar()
	am_pm_stringvar = StringVar()
	hour_input_stringvar.set(datetime.strftime(datetime.now(), '%I'))
	minute_input_stringvar.set('00')
	am_pm_stringvar.set(datetime.strftime(datetime.now(), '%p'))
	return_button = Buttonbox(text='Confirm', lang=lang, repr='rbutton')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancelbutton')

	confirm_window.newFrame("First Frame", (0, 0))

	Label(confirm_window.frames["First Frame"], text=lang['Time']).grid(row=0, column=0, sticky=E)
	hour_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=hour_input_stringvar, width=3, state='readonly')
	hour_input.grid(row=0, column=1)
	minute_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=minute_input_stringvar, width=3, state='readonly')
	minute_input.grid(row=0, column=2)
	am_pm_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=am_pm_stringvar, width=3, state='readonly')
	am_pm_input.grid(row=0, column=3)
	confirm_window.frames["First Frame"].addWidget(return_button, (1, 0))
	confirm_window.frames["First Frame"].addWidget(cancel_button, (2, 0))

	hour_input['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	minute_input['values'] = ('00', '30')
	am_pm_input['values'] = ('AM', 'PM')

	return_button.selfframe.grid(columnspan=6, pady=(20, 0))
	cancel_button.selfframe.grid(columnspan=6)

	return_button.config(cmd=return_)
	cancel_button.config(cmd=confirm_time.destroy)

	confirm_time.wait_window()

	return confirm_time.time_input_confirmed