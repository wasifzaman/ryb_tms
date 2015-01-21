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

def convert_to_encrypted(lang, d):

	def get_return(z):
		t.z = z
		t.to_encrypt_file = to_encrypt_file_textbox.getData()
		t.db_file = db_file_textbox.getData()
		t.pw_file = pw_file_textbox.getData()
		t.pw = pw_textbox.getData()
		t.dw()

	def set_file(textbox):
		out_file = filedialog.asksaveasfilename()
		if len(out_file) != 0:
			textbox.setData(out_file + '.rybdb')

	def open_file(textbox):
		out_file = filedialog.askopenfile()
		if out_file != None:
			textbox.setData(out_file.name)

	t = Mbox()
	#t.root.overrideredirect(0)
	#t.root.bind("<Destroy>", lambda event: None)

	t.newFrame("First Frame", (0, 0))


	to_encrypt_file_textbox = Textbox(text='Unencrypted File', lang={'Unencrypted File': 'Unencrypted File'}, repr='unc_db_file')
	db_file_textbox = Textbox(text='Encrypt File To', lang={'Encrypt File To': 'Encrypt File To'}, repr='db_file')
	pw_file_textbox = Textbox(text='Password File', lang={'Password File': 'Password File'}, repr='pw_file')
	pw_textbox = Textbox(text='Password', lang={'Password': 'Password'}, repr='pw')

	brw1 = Buttonbox(text='browse', lang=language, repr='brw1')
	brw2 = Buttonbox(text='browse', lang=language, repr='brw2')
	brw3 = Buttonbox(text='browse', lang=language, repr='brw3')

	t.frames["First Frame"].addWidget(to_encrypt_file_textbox, (0, 0))
	t.frames["First Frame"].addWidget(db_file_textbox,(1, 0))
	t.frames["First Frame"].addWidget(pw_file_textbox,(2, 0))
	t.frames["First Frame"].addWidget(brw3, (0, 2))
	t.frames["First Frame"].addWidget(brw1, (1, 2))
	t.frames["First Frame"].addWidget(brw2, (2, 2))
	t.frames["First Frame"].addWidget(pw_textbox, (3, 0))
	t.frames["First Frame"].addWidget(bsav, (4, 1))
	t.frames["First Frame"].addWidget(bcancel, (5, 1))


	db_file_textbox.label.config(width=12)
	pw_file_textbox.label.config(width=12)
	to_encrypt_file_textbox.config(width=12)
	pw_textbox.label.config(width=12)
	brw1.button.config(width=7)
	brw2.button.config(width=7)
	brw3.button.config(width=7)
	bsav.button.config(width=22)

	brw1.config(cmd=lambda: set_file(db_file_textbox))
	brw2.config(cmd=lambda: set_file(pw_file_textbox))
	brw3.config(cmd=lambda: open_file(to_encrypt_file_textbox))
	bsav.config(cmd=lambda: get_return('success'))
	bcancel.config(cmd=lambda: get_return('cancel'), lang=lang)



	t.root.wait_window()

	if t.z == 'cancel':
		return

	key = str.encode(t.pw)
	studentList = pickle.load(open(t.to_encrypt_file, 'rb'))
	cipher = AES.new(key, AES.MODE_CFB, d.iv)
	binary_string = pickle.dumps(studentList)
	encrypted = cipher.encrypt(binary_string)

	f = open(t.db_file, 'wb')
	f.write(bytearray(encrypted))
	f.close()

	f = open(t.pw_file, 'wb')
	f.write(bytearray(str.encode(t.pw)))
	f.close()