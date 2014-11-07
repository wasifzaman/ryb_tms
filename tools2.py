from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from datetime import datetime
import importwiz
import os
import sdb_salrep
import preBuilts2


def main(t, lang, d, k):
	'''tools2'''

	def cdb(label):
		try:
			p = filedialog.askopenfile(mode='r').name
			y = os.path.abspath(p)
			p = p.split('/')[-1]
			if p[p.rfind('.'):]!= '.rybdb':
				print("invalid file")
				return
			else:
				label.config(text=y)
				d.file = y
				#d.loadData()
		except:
			print("error opening file.")


	def ctdb():
		try:
			p = filedialog.askopenfile(mode='r').name
			l = p.split('/')[-1]
			ext = l[l.rfind('.'):]
			if ext != '.xls' and ext != '.xlsx':
				print("invalid file")
				return
			else:
				d.loadData()
				ns, nt = d.importtimexlsx(p)
				ctimp(w.lang, ns, nt)
				#d.saveData()
		except:
			return
			#print("error opening file.")


	def ss():
		d.file = curdb.cget('text')
		dbs(w.lang)


	def set_pwfile(label):
		open_f = filedialog.askopenfile()
		f = open(open_f.name)
		d.key = f.read()
		label.config(text=open_f.name)
		d.pwfile = open_f.name
		k.files['pwfile'] = open_f.name
		k.save()




	def expf():
		try:
			p = filedialog.askdirectory()
			#d.exportxlsx(p + '/student_list.xlsx')
			#d.exporttxlsx(p + '/student_att.xlsx')
			d.exportdb(p + '/backup_' + str(datetime.now().date()) + '.rybdb')
		except:
			return


	def salrep(f):
		try:
			for child in t.winfo_children():
				child.destroy()
			sdb_salrep.main(t, w.lang, d)
		except:
			return


	def choose_school_(event):
		print(d.school)

		school = preBuilts2.choose_school(w.lang)
		if school == 'cancel': return

		k.files['school'] = school
		d.school = k.files['school']
		k.save()

		return

		


	def it():
		return


	#d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	#w.newFrame("Title Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Fifth Frame", (2, 0))
	w.newFrame("Second Frame", (3, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (4, 1))

	w.frames["Third Frame"].config(bg='#DBDBDB')
	w.frames["Third Frame"].grid(rowspan=3)

	bchoose_school = Buttonbox(text='Choose School', lang=w.lang, repr='bcschool')

#title
	#w.frames["Title Frame"].grid(columnspan=4, sticky=E+W)
	#Label(w.frames["Title Frame"], text='Database Management', bg='#3B5C8D', fg='white', \
	#	height=3, font=('Jumbo', '12', 'bold')).pack(fill='both', expand=True)

#import export widgets
	w.frames["First Frame"].addWidget(imp, (0, 0))
	w.frames["First Frame"].addWidget(bimp, (2, 0))

	#w.frames["Fifth Frame"].addWidget(impt, (0, 0))
	w.frames["Fifth Frame"].addWidget(bimpt, (0, 0))

	#w.frames["Second Frame"].addWidget(exp, (0, 0))
	#w.frames["Second Frame"].addWidget(bexp, (0, 0))

	#salary report
	w.frames["Second Frame"].addWidget(bsalrep, (3, 0))

	#choose school
	w.frames["Second Frame"].addWidget(bchoose_school, (4, 0))

	curdb = Label(w.frames['Third Frame'], text=d.file, wraplength=200, bg='#DBDBDB')
	w.frames["Third Frame"].addWidget(curfile, (0, 0))
	curfile.label.config(bg='#DBDBDB')
	curdb.grid(row=3, column=0, pady=10)

	curpwfile = Label(w.frames['Third Frame'], text=d.pwfile, wraplength=200, bg='#DBDBDB')
	curpwfile.grid(row=5, column=0, pady=10)

	choose_pwfile = Buttonbox(text='Choose PW File', lang=w.lang, repr='cpwfile')
	create_db = Buttonbox(text='Create new Database', lang=w.lang, repr='createdb')
	convert_db = Buttonbox(text='Convert to Encrypted DB', lang=w.lang, repr='convertdb')

	w.frames["Third Frame"].addWidget(bcdb, (2, 0))
	w.frames["Third Frame"].addWidget(choose_pwfile, (4, 0))
	w.frames["Third Frame"].addWidget(create_db, (1, 0))

	w.frames["Second Frame"].addWidget(convert_db, (5, 0))

	#w.frames['Fourth Frame'].addWidget(bsav, (0, 0))

	#bsav.config(cmd=ss)
	bchoose_school.config(cmd=lambda: choose_school_(w.lang))
	bimp.config(cmd=lambda: importwiz.main(w.lang, d))
	bcdb.config(cmd=lambda: cdb(curdb))
	bimpt.config(cmd=ctdb)
	#bexp.config(cmd=expf)
	bsalrep.config(cmd=salrep)
	choose_pwfile.config(cmd=lambda: set_pwfile(curpwfile))
	convert_db.config(cmd=lambda: convert_to_encrypted(w.lang, d))
	create_db.config(cmd=lambda: create_new_db(w.lang, d))
	#curdb.config(text=s.config['dbFile'])
	#exp.config(cmd=importwiz.main)

	w.mmbuttoncol = 'tomato'
	w.mmbuttonfg = 'black'

	bsalrep.idlebg = w.mmbuttoncol
	bsalrep.fg = w.mmbuttonfg
	bsalrep.hoverfg = 'white'
	bsalrep.hoverbg = 'crimson'
	bsalrep.button.config(bg=bsalrep.idlebg, fg=bsalrep.fg)


#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)