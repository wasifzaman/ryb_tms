import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')

from tkinter import *
from Crypto.Cipher import AES
import pickle

from textbox import Textbox, TextboxNoEdit, IntTextbox, MoneyTextbox
from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox
from languages import languages

language = languages["english"]

bsav = Buttonbox(text='Save', lang=language, repr='bsav')
bcancel = Buttonbox(text='Cancel', lang=language, repr='bcancel')

def create_new_markerfile(lang):
	def get_return(z):
		t.z = z
		t.marker_file = marker_file_textbox.getData()
		t.dw()

	def set_file(textbox):
		out_file = filedialog.asksaveasfilename()
		if len(out_file) != 0:
			textbox.setData(out_file + '.rybdb')

	t = Mbox()

	t.newFrame("First Frame", (0, 0))


	marker_file_textbox = TextboxNoEdit(text='Marker File', lang={'Marker File': 'Marker File'}, repr='marker_file')
	
	brw3 = Buttonbox(text='browse', lang=language, repr='brw3')

	t.frames["First Frame"].addWidget(marker_file_textbox,(2, 0))
	t.frames["First Frame"].addWidget(brw3,(2, 2))
	t.frames["First Frame"].addWidget(bsav, (4, 1))
	t.frames["First Frame"].addWidget(bcancel, (5, 1))


	marker_file_textbox.label.config(width=12)
	brw3.button.config(width=7)
	bsav.button.config(width=22)

	brw3.config(cmd=lambda: set_file(marker_file_textbox))
	bsav.config(cmd=lambda: get_return('success'))
	bcancel.config(cmd=lambda: get_return('cancel'), lang=lang)



	t.root.wait_window()

	if t.z == 'cancel':
		return

	if t.marker_file.strip() != "":
		pickle.dump({}, open(t.marker_file, "wb"))

	print(t.z)
