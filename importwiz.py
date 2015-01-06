from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from tkinter import filedialog
from random import randrange
import os

def main(lang, d):

	def odb():
		try:
			w.fpath.setData(filedialog.askopenfile(mode='r').name)
		except:
			pass

#		nd = StudentDB(file='temp.db')

	def sp():
		w.frames["First Frame"].grid()
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()

		w.frames["Fourth Frame"].grid_forget()
		w.frames["Fifth Frame"].grid_forget()
		w.frames["Sixth Frame"].grid_forget()

	def pvdb():
		#try:
		rand_int = str(randrange(0, 100000))
		w.randfile = 'temp' + rand_int + '.rybdb'
		w.randpwfile = 'temp_pw_file' + rand_int + '.rybdb'
		nd = StudentDB(file=w.randfile, cfile='', pwfile=w.randpwfile)
		nd.importxlsx(fpath.getData())

		w.sL = []
		for s in nd.studentList.values():
			dp = s.datapoints
			w.sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

		w.sL.sort()


		w.frames["First Frame"].grid_forget()
		w.frames["Second Frame"].grid_forget()
		w.frames["Third Frame"].grid_forget()

		w.frames["Fourth Frame"].grid()
		w.frames["Fifth Frame"].grid()
		w.frames["Sixth Frame"].grid()

		
		w.stable.setData((w.stableh, w.sL))
		w.stable.canvas.config(width=700)
		#except:
		#	noimp(w.lang)

	def pdb():
		try:
			fpath2.setData(filedialog.asksaveasfilename())
		except:
			pass
	def pw_path():
		try:
			pw_fpath.setData(filedialog.asksaveasfilename() + '.rybdb')
		except:

			pass

	def sav():
		#f = fpath2.getData().split('/')[-1] + '.db'
		f = fpath2.getData() + '.rybdb'
		nd = StudentDB(file=f, cfile='', pwfile=pw_fpath.getData())
		if f == '.db':
			pchoosefile(w.lang)
			return

		nd.importxlsx(fpath.getData())
		os.remove(w.randfile)
		t.destroy()



	d.loadData()

	t = Window(top=True)
	t.geometry('900x500')
	t.attributes('-fullscreen', False)
	t.focus_set()
	t.grab_set()

	w = AppWindow(t.mainFrame)

	w.lang = lang

	w.sL = []

	w.stable = stable
	w.stableh = [w.lang['Barcode'], w.lang['First Name'], \
		w.lang['Last Name'], w.lang['Chinese Name'], w.lang['Date of Birth']]
	w.stable.build(headers=w.stableh, data=[[]])

#frame initialization
	w.newFrame("L Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (3, 0))
	w.newFrame("Sixth Frame", (3, 0))
	w.newFrame("Fourth Frame", (4, 0))
	w.newFrame("Fifth Frame", (5, 0))

#hide next frame
	w.frames["Fourth Frame"].grid_forget()
	w.frames["Fifth Frame"].grid_forget()
	w.frames["Sixth Frame"].grid_forget()


	Label(w.frames["First Frame"], text="Welcome to the Import wizard.\n\n1. Please select the xls or xlsx file below.\n2. Then click Next.", justify=LEFT).grid()

	w.fpath = fpath

#intialize widgets
	w.bsav = bsav

	pw_fpath = Textbox(text='Password File', lang=w.lang, repr='pwfilepath')
	pw_fpath_brw = Buttonbox(text='browse', lang=language, repr='pwfilebrw')
	w.frames["Second Frame"].addWidget(w.fpath, (0, 0))
	#w.frames["Second Frame"].addWidget(sepr, (2, 0))
	w.frames["Second Frame"].addWidget(brw, (0, 2))
	w.frames["Third Frame"].addWidget(nxt, (0, 1))
	w.frames["Fourth Frame"].addWidget(w.stable, (0, 0))
	w.frames["Fifth Frame"].addWidget(fpath2, (0, 0))
	w.frames["Fifth Frame"].addWidget(brw2, (0, 3))
	w.frames["Fifth Frame"].addWidget(pw_fpath, (1, 0))
	w.frames["Fifth Frame"].addWidget(pw_fpath_brw, (1, 3))
	w.frames["Fifth Frame"].addWidget(sepr, (2, 0))
	w.frames["Sixth Frame"].addWidget(bk, (3, 0))
	w.frames["Sixth Frame"].addWidget(w.bsav, (3, 1))

	bcancel1 = Buttonbox(text='Cancel', lang=w.lang, repr='cancel')
	bcancel2 = Buttonbox(text='Cancel', lang=w.lang, repr='cancel')

	w.frames["Third Frame"].addWidget(bcancel1, (0, 2))
	w.frames["Sixth Frame"].addWidget(bcancel2, (3, 2))

	brw.config(cmd=odb)
	brw2.config(cmd=pdb)
	pw_fpath_brw.config(cmd=pw_path)
	bk.config(cmd=sp)
	nxt.config(cmd=pvdb)
	w.bsav.config(cmd=sav)
	bcancel1.config(cmd=t.destroy)
	bcancel2.config(cmd=t.destroy)

	w.fpath.label.config(anchor=N)
	brw.button.config(width=12, pady=1)
	brw.selfframe.grid(padx=10, columnspan=2)
	brw2.button.config(width=12, pady=1)
	brw2.selfframe.grid(padx=10)
	pw_fpath_brw.button.config(width=12, pady=1)
	pw_fpath_brw.selfframe.grid(padx=10)
	bk.button.config(width=10)
	bk.selfframe.grid(padx=10)
	nxt.button.config(width=10)
	nxt.selfframe.grid(padx=10)
	w.bsav.button.config(width=10)
	w.bsav.selfframe.grid(padx=10)
	bcancel1.button.config(width=10)
	bcancel1.selfframe.grid(padx=10)
	bcancel2.button.config(width=10)
	bcancel2.selfframe.grid(padx=10)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	
	t.mainloop()