import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
sys.path.append(os.path.abspath(os.pardir))

from tkinter import *

from tableWidget2 import Table
from photoWidget2 import Photo
from languages import *

language = languages["english"]

stable = Table(repr='stable', edit=False, dimension=(0, 0, 100, 100))
portr = Photo(repr='portr', path='monet_sm.jpg')
stableh = [language['Barcode'], language['First Name'], \
	language['Last Name'], language['Chinese Name'], language['Date of Birth']]

#stable.build(headers=stableh, data=[[]])

def sbind(f):
	def fsb(p):
		i = stable.data[p[0]-1][0]
		f(i)
		
	for pos, cell in stable.cells.items():
		cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))

def spicker(d):
	def sets(i):
		stable.s = i
		t.destroy()

	def destroy():
		stable.s = False
		t.destroy()

	t = Toplevel()
	frame = Frame(t, padx=10, pady=10)
	frame.pack()
	t.grab_set()
	t.focus_set()
	t.protocol('WM_DELETE_WINDOW', destroy)
	t.geometry('570x440')

	stable.build(headers=stableh, data=d)
	stable.place(parent=frame, row=0, column=0)
	stable.canvas.config(widt=530, height=400)

	sbind(lambda i: sets(i=i))

	t.resizable(0, 0)

	t.wait_window()

	return stable.s