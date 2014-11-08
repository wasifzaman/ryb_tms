from tkinter import *
from uiHandler22 import *
from dataHandler import *
from languages import *
from labelWidgets2 import *
from photoWidget2 import *
from preBuilts2 import ret, titlePic, bexp, password_prompt, wrong_password, pw_reset_confirm
from tkinter import filedialog
import addS3
import scanS22
import scanOut
import sDb22
import tools2
import sdb_salrep
import preBuilts2

def main():

#language changer
	def clang():
		if w.lang['self'] == 'english':
			w.lang = languages['chinese']
		else:
			w.lang = languages['english']
		for frame in w.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=w.lang)


	t = Window(top=False)
	t.attributes('-fullscreen', False)
	t.geometry('1440x900+100+100')
	t.wm_title("RYB Teacher Attendance")

#confirm closing of the add student window
	t.con = False

#show and hide sub-windows
	def showWindow(f):
		#try:
		#w.frames["Title Frame"].grid_forget()
		w.frames["First Frame"].grid_forget()
		print(f.__doc__)
		if (f.__doc__) == 'addS3':
			t.con = True
			w.t = f(w.frames["Second Frame"], w.lang, w.d, showMain)
		elif (f.__doc__) == 'tools2':
			if w.k.files['resetpw'] == True:
				new_pw = password_prompt(w.lang, w.k.files['dbpw'])
				if new_pw == 'cancel' or w.k.hashpw(new_pw[0]) != w.k.files['dbpw']:
					wrong_password(w.lang)
					showMain(t.con)
					return
				w.k.files['dbpw'] = w.k.hashpw(new_pw[1])
				w.k.files['resetpw'] = False
				w.k.save()
				pw_reset_confirm(w.lang)
			else:
				pw_input = password_prompt(w.lang, False)
				if not w.k.hashpw(pw_input) == w.k.files['dbpw'] or pw_input == 'cancel':
					wrong_password(w.lang)
					showMain(t.con)
					return
			w.t = f(w.frames["Second Frame"], w.lang, w.d, w.k)
		else:
			t.con = False
			w.t = f(w.frames["Second Frame"], w.lang, w.d)
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()
		#except:
		#	print('unknown error', 'error in function showWindow', f.__doc__)

#show and hide main window
	def showMain(con):
		if con:
			if not ret('a', w.lang): return

		w.frames['Second Frame'].grid_forget()
		try:
			#to destroy the extra window in scan student
			w.t.destroy()
		except:
			pass

		for child in w.frames["Second Frame"].winfo_children():
			child.destroy()

		w.frames['Second Frame'].destroy()
		w.newFrame("Second Frame", (2, 0))
		w.frames['Second Frame'].grid_forget()

		w.frames["First Frame"].grid(row=1)
		w.frames['Third Frame'].grid_forget()

		w.k.files['cfilepath'] = w.d.file
		w.k.save()

#print report prompt
	def printPrompt():

		def out():
			try:
				p = filedialog.asksaveasfilename()
			except:
				return

			try:
				w.d.exportreport(p, rdate.getData())
			except:
				pass

			pt.destroy()

		pt = Window(top=True)
		pt.attributes('-fullscreen', False)
		pt.resizable(0, 0)
		pt.geometry('400x200+200+200')
		pt.grab_set()
		pt.focus_set()

		wpt = AppWindow(pt.mainFrame)

		rdate = Datebox(text=w.lang['sdate'], lang=w.lang, repr='rdate')
		rbutton = Buttonbox(text='Select Folder', lang=w.lang, repr='rbutton')

		wpt.newFrame("First Frame", (0, 0))

		wpt.frames["First Frame"].addWidget(rdate, (0, 0))
		wpt.frames["First Frame"].addWidget(rbutton, (1, 0))

		rdate.label.destroy()
		rbutton.selfframe.grid(columnspan=2, pady=20)

		rbutton.config(cmd=out)

	def choose_school(event):
		
		w.k.files['school'] = preBuilts2.choose_school(w.lang)
		w.d.school = w.k.files['school']
		w.k.save()

		return
	
	def expf():
		try:
			p = filedialog.askdirectory()
			d.exportdb(p + '/backup_' + str(datetime.now().date()) + '.rybdb')
		except:
			return

#main window and starting language
	w = AppWindow(t.mainFrame)
	w.lang = languages['chinese']

#title
	t.wintitle.config(text=w.lang['RYB Student Management'])


#load current database
	w.k = keeper.Keeper('keeper.db')
	w.d = StudentDB(file=w.k.files['cfilepath'], pwfile=w.k.files['pwfile'], cfile=w.k.fname)

	if 'school' not in w.k.files:
		w.k.files['school'] = preBuilts2.choose_school(w.lang)
		w.d.school = w.k.files['school']
		w.k.save()
	else:
		w.d.school = w.k.files['school']

#frame creation and positions
	#w.newFrame("Title Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (3, 0))

#hide sub-frames
	w.frames['Second Frame'].grid_forget()
	w.frames['Third Frame'].grid_forget()

#buttons to call sub-windows
	bchoose_school = Buttonbox(text='Choose School', lang=w.lang, repr='bcschool')
	bsadd = Buttonbox(text='Add Students', lang=w.lang, repr='bsadd') #Add Student
	bsscan = Buttonbox(text='Scan Students', lang=w.lang, repr='bsscan') #Scan Student
	bsscan2 = Buttonbox(text='Scan Out Teacher', lang=w.lang, repr='bsscan2') #Scan Student
	bssdb = Buttonbox(text='Student Database', lang=w.lang, repr='bssdb') #Student Database
	bstools = Buttonbox(text='Tools', lang=w.lang, repr='bstools') #Database Management
	bsbmm = Buttonbox(text='Back to Main Menu', lang=w.lang, repr='bsbmm') #Return to Main Menu
	bsexit = Buttonbox(text='Exit', lang=w.lang, repr='bsexit') #Exit
	bclang = Buttonbox(text='changelanguage', lang=w.lang, repr='bclang') #Change Language
	bprint = Buttonbox(text='print report', lang=w.lang, repr='bprint') #Print end of day report
	bexp = Buttonbox(text='expxls', lang=w.lang, repr='bexp')

#background image
	w.p = Photo(repr='splash', path='background_IMG.jpg')

#place buttons and background image
	#w.frames["First Frame"].addWidget(bchoose_school, (0, 0))
	w.frames["First Frame"].addWidget(bsadd, (1, 0))
	w.frames["First Frame"].addWidget(bsscan, (2, 0))
	w.frames["First Frame"].addWidget(bsscan2, (3, 0))
	w.frames["First Frame"].addWidget(bssdb, (4, 0))
	w.frames["First Frame"].addWidget(bstools, (5, 0))
	w.frames["First Frame"].addWidget(bexp, (6, 0))
	w.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	w.frames["First Frame"].addWidget(bclang, (7, 0))
	w.frames["First Frame"].addWidget(bprint, (8, 0))
	w.frames["First Frame"].addWidget(bsexit, (9, 0))
	w.frames["First Frame"].addWidget(w.p, (0, 2))
	Label(w.frames["First Frame"], text='  ').grid(column=1) #separator between buttons and background image

#set commands for each button
	#bchoose_school.config(cmd=lambda: choose_school(w.lang))
	bsadd.config(cmd=lambda: showWindow(addS3.main))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bsscan2.config(cmd=lambda: showWindow(scanOut.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main))
	bsbmm.config(cmd=lambda: showMain(t.con))
	bprint.config(cmd=printPrompt)
	bsexit.config(cmd=t.destroy)
	bclang.config(cmd=clang)
	bexp.config(cmd=expf)
	bstools.selfframe.grid_forget()
	#secret configuration to call Database Management
	w.p.label.bind('<Control-Alt-Shift-D>', lambda e: showWindow(tools2.main))

	w.p.label.grid(rowspan=100, sticky=E)

	w.mmbuttoncol = '#E3E9F9'
	w.mmbuttonfg = 'black'

	#bchoose_school.idlebg = w.mmbuttoncol
	#bchoose_school.fg = w.mmbuttonfg
	#bchoose_school.hoverfg = 'white'
	#bchoose_school.button.config(bg=bchoose_school.idlebg, fg=bchoose_school.fg)

	bsbmm.idlebg = w.mmbuttoncol
	bsbmm.fg = w.mmbuttonfg
	bsbmm.hoverfg = 'white'
	bsbmm.button.config(bg=bsbmm.idlebg, fg=bsbmm.fg)

	bsadd.idlebg = w.mmbuttoncol
	bsadd.fg = w.mmbuttonfg
	bsadd.hoverfg = 'white'
	bsadd.button.config(bg=bsadd.idlebg, fg=bsadd.fg)

	bsscan.idlebg = w.mmbuttoncol
	bsscan.fg = w.mmbuttonfg
	bsscan.hoverfg = 'white'
	bsscan.button.config(bg=bsscan.idlebg, fg=bsscan.fg)

	bsscan2.idlebg = w.mmbuttoncol
	bsscan2.fg = w.mmbuttonfg
	bsscan2.hoverfg = 'white'
	bsscan2.button.config(bg=bsscan2.idlebg, fg=bsscan2.fg)

	bssdb.idlebg = w.mmbuttoncol
	bssdb.fg = w.mmbuttonfg
	bssdb.hoverfg = 'white'
	bssdb.button.config(bg=bssdb.idlebg, fg=bssdb.fg)

	bclang.idlebg = w.mmbuttoncol
	bclang.fg = w.mmbuttonfg
	bclang.hoverfg = 'white'
	bclang.button.config(bg=bclang.idlebg, fg=bclang.fg)

	bsexit.idlebg = w.mmbuttoncol
	bsexit.fg = w.mmbuttonfg
	bsexit.hoverfg = 'white'
	bsexit.button.config(bg=bsexit.idlebg, fg=bsexit.fg)

	bprint.idlebg = w.mmbuttoncol
	bprint.fg = w.mmbuttonfg
	bprint.hoverfg = 'white'
	bprint.button.config(bg=bprint.idlebg, fg=bprint.fg)

	bstools.idlebg = w.mmbuttoncol
	bstools.fg = w.mmbuttonfg
	bstools.hoverfg = 'white'
	bstools.button.config(bg=bstools.idlebg, fg=bstools.fg)

	bexp.idlebg = w.mmbuttoncol
	bexp.fg = w.mmbuttonfg
	bexp.hoverfg = 'white'
	bexp.button.config(bg=bexp.idlebg, fg=bexp.fg)

	t.iconbitmap('RYB_Attendance.ico')
	t.mainloop()


if __name__ == '__main__':
	main()

	'''
	key = '0123456789abcdef'
	IV = 16 * '\x00'           # Initialization vector: discussed later
	mode = AES.MODE_CBC
	encryptor = AES.new(key, mode, IV=IV)

	text = 'j' * 64 + 'i' * 128
	ciphertext = encryptor.encrypt(text)
	print(ciphertext)
	'''