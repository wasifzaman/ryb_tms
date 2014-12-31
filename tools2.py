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
		if open_f == None: return
		f = open(open_f.name)
		d.key = f.read()
		label.config(text=open_f.name)
		d.pwfile = open_f.name
		k.files['pwfile'] = open_f.name
		k.save()

	def set_markerfile(label):
		open_f = filedialog.askopenfile()
		if open_f == None: return
		label.config(text=open_f.name)
		k.files['markerfile'] = open_f.name
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
			sdb_salrep.main(t, w.lang, d, k.files['markerfile'])
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

	def reset_dbmanager_pw(lang):

		new_pw = password_prompt(lang, k.files['dbpw'])
		if new_pw == 'cancel' or k.hashpw(new_pw[0]) != k.files['dbpw']:
			wrong_password(w.lang)
			return
		k.files['dbpw'] = k.hashpw(new_pw[1])
		k.files['resetpw'] = False
		k.save()
		pw_reset_confirm(w.lang)
		
	def choose_makerfile(lang):

		return

	def it():
		return


	#d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	#w.newFrame("Title Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	#w.newFrame("Fifth Frame", (2, 0))
	w.newFrame("Second Frame", (3, 0))
	w.newFrame("Third Frame", (1, 1))
	#w.newFrame("Fourth Frame", (4, 1))

	w.frames["Third Frame"].config(bg='#DBDBDB')
	w.frames["Third Frame"].grid(rowspan=3)

	bchoose_school = Buttonbox(text='Choose School', lang=w.lang, repr='bcschool')
	reset_db_manager_pw = Buttonbox(text='Reset DB Manager PW', lang=w.lang, repr='resetdbmanagerpw')

#title
	#w.frames["Title Frame"].grid(columnspan=4, sticky=E+W)
	#Label(w.frames["Title Frame"], text='Database Management', bg='#3B5C8D', fg='white', \
	#	height=3, font=('Jumbo', '12', 'bold')).pack(fill='both', expand=True)

#import export widgets
	w.frames["First Frame"].addWidget(imp, (0, 0))
	w.frames["First Frame"].addWidget(bimp, (1, 0))

	#w.frames["Fifth Frame"].addWidget(impt, (0, 0))
	w.frames["First Frame"].addWidget(bimpt, (2, 0))

	#w.frames["Second Frame"].addWidget(exp, (0, 0))
	#w.frames["Second Frame"].addWidget(bexp, (0, 0))

	#salary report
	w.frames["First Frame"].addWidget(bsalrep, (3, 0))

	#choose school
	w.frames["First Frame"].addWidget(bchoose_school, (4, 0))
	w.frames["First Frame"].addWidget(reset_db_manager_pw, (5, 0))

	curdb = Label(w.frames['Third Frame'], text=d.file, wraplength=200, bg='#DBDBDB')
	w.frames["Third Frame"].addWidget(curfile, (0, 0))
	curfile.label.config(bg='#DBDBDB')
	curdb.grid(row=3, column=0, pady=10)

	curpwfile = Label(w.frames['Third Frame'], text=d.pwfile, wraplength=200, bg='#DBDBDB')
	curpwfile.grid(row=5, column=0, pady=10)
	curmarkerfile = Label(w.frames['Third Frame'], text=k.files['markerfile'], wraplength=200, bg='#DBDBDB')
	curmarkerfile.grid(row=8, column=0, pady=10)

	choose_pwfile = Buttonbox(text='Choose PW File', lang=w.lang, repr='cpwfile')
	choose_markerfile = Buttonbox(text='Choose Maker File', lang=w.lang, repr='cmarkerfile')
	create_db = Buttonbox(text='Create new Database', lang=w.lang, repr='createdb')
	create_markerfile = Buttonbox(text='Create new Markerfile', lang=w.lang, repr='createmfile')
	convert_db = Buttonbox(text='Convert to Encrypted DB', lang=w.lang, repr='convertdb')

	w.frames["Third Frame"].addWidget(bcdb, (2, 0))
	w.frames["Third Frame"].addWidget(choose_pwfile, (4, 0))
	w.frames["Third Frame"].addWidget(create_db, (1, 0))
	w.frames["Third Frame"].addWidget(create_markerfile, (6, 0))
	w.frames["Third Frame"].addWidget(choose_markerfile, (7, 0))

	w.frames["First Frame"].addWidget(convert_db, (6, 0))

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
	create_markerfile.config(cmd=lambda: create_new_markerfile(w.lang))
	choose_markerfile.config(cmd=lambda: set_markerfile(curmarkerfile))
	reset_db_manager_pw.config(cmd=lambda: reset_dbmanager_pw(w.lang))
	#curdb.config(text=s.config['dbFile'])
	#exp.config(cmd=importwiz.main)

	w.mmbuttoncol = 'tomato'
	w.mmbuttonfg = 'black'

	bsalrep.idlebg = w.mmbuttoncol
	bsalrep.fg = w.mmbuttonfg
	bsalrep.hoverfg = 'white'
	bsalrep.hoverbg = 'crimson'
	bsalrep.button.config(bg=bsalrep.idlebg, fg=bsalrep.fg)

	bcdb.idlebg = w.mmbuttoncol
	bcdb.fg = w.mmbuttonfg
	bcdb.hoverfg = 'white'
	bcdb.hoverbg = 'crimson'
	bcdb.button.config(bg=bcdb.idlebg, fg=bcdb.fg)


#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)