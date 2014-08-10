from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from datetime import datetime
import importwiz
import os


def main(t, lang, d):

	def cdb():
		try:
			p = filedialog.askopenfile(mode='r').name
			y = os.path.abspath(p)
			p = p.split('/')[-1]
			if p[p.rfind('.'):]!= '.db':
				print("invalid file")
				return
			else:
				curdb.config(text=y)
				d.file = y
				#d.loadData()
		except:
			print("error opening file.")


	def ctdb():
		#try:
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
		#except:
		#	return
			#print("error opening file.")


	def ss():
		d.file = curdb.cget('text')
		dbs(w.lang)


	def expf():
		try:
			p = filedialog.askdirectory()
			d.exportxlsx(p + '/student_list.xlsx')
			d.exporttxlsx(p + '/student_att.xlsx')
			d.exportdb(p + '/backup_' + str(datetime.now().date()) + '.db')
		except:
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

#title
	#w.frames["Title Frame"].grid(columnspan=4, sticky=E+W)
	#Label(w.frames["Title Frame"], text='Database Management', bg='#3B5C8D', fg='white', \
	#	height=3, font=('Jumbo', '12', 'bold')).pack(fill='both', expand=True)

#import export widgets
	w.frames["First Frame"].addWidget(imp, (0, 0))
	#w.frames["First Frame"].addWidget(sepr, (1, 0))
	w.frames["First Frame"].addWidget(bimp, (2, 0))

	w.frames["Fifth Frame"].addWidget(impt, (0, 0))
	#w.frames["Fifth Frame"].addWidget(sepr, (1, 0))
	w.frames["Fifth Frame"].addWidget(bimpt, (2, 0))

	w.frames["Second Frame"].addWidget(exp, (0, 0))
	#w.frames["Second Frame"].addWidget(sepr, (1, 0))
	w.frames["Second Frame"].addWidget(bexp, (2, 0))

	curdb = Label(w.frames['Third Frame'], text=d.file, wraplength=200, bg='#DBDBDB')
	w.frames["Third Frame"].addWidget(curfile, (0, 0))
	curfile.label.config(bg='#DBDBDB')
	curdb.grid(row=2, column=0, pady=10)

	w.frames["Third Frame"].addWidget(bcdb, (1, 0))


	#w.frames['Fourth Frame'].addWidget(bsav, (0, 0))

	#bsav.config(cmd=ss)
	bimp.config(cmd=lambda: importwiz.main(w.lang, d))
	bcdb.config(cmd=cdb)
	bimpt.config(cmd=ctdb)
	bexp.config(cmd=expf)
	#curdb.config(text=s.config['dbFile'])
	#exp.config(cmd=importwiz.main)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)


if __name__ == '__main__':
	t = Window()
	main(t, language)
	
	t.mainloop()