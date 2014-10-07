from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(lang, d, top=False, i=0):

	d.loadData()

	t = Window(top=top)
	t.attributes('-fullscreen', False)
	t.geometry('1600x700')
	t.resizable(0, 0)
	t.grab_set()
	t.focus_set()

	w = AppWindow(t.mainFrame)

	w.lang = lang
	w.s = i

#frame initialization
	w.newFrame("First Frame", (1, 1))
	w.newFrame("Second Frame", (1, 2))
	w.newFrame("Third Frame", (2, 1))
	w.newFrame("Fourth Frame", (2, 1))
	w.newFrame("Fifth Frame", (5, 0))
	w.newFrame("Sixth Frame", (4, 2))
	w.newFrame("Seventh Frame", (1, 0))
	w.newFrame("Eigth Frame", (3, 2))
	w.newFrame("Ninth Frame", (3, 1))
	w.newFrame("Tenth Frame", (0, 1))
	w.newFrame("Eleventh Frame", (1, 3))
	w.newFrame("Twelfth Frame", (3, 0))

	w.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w.frames["Seventh Frame"].grid(rowspan=2)
	w.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	w.frames["Tenth Frame"].grid(columnspan=5)
	w.frames["Eleventh Frame"].grid(sticky=N)
	w.frames["Eigth Frame"].grid(sticky=S, rowspan=2)
	w.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=520)
	w.frames["Eigth Frame"].rowconfigure(0, weight=5, minsize=20)

#student info widgets
	w.frames["First Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(firstName, (1, 0))
	w.frames["First Frame"].addWidget(lastName, (2, 0))
	w.frames["First Frame"].addWidget(chineseName, (3, 0))
	w.frames["First Frame"].addWidget(dob, (4, 0))
	#w.frames["First Frame"].addWidget(age, (5, 0))
	#w.frames["First Frame"].addWidget(parentName, (6, 0))
	w.frames["First Frame"].addWidget(cp, (7, 0))

#address widgets
	w.frames["First Frame"].addWidget(ainfo, (8, 0))
	ainfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(city, (9, 0))
	w.frames["First Frame"].addWidget(state, (10, 0))
	w.frames["First Frame"].addWidget(zip, (11, 0))
	w.frames["First Frame"].addWidget(email, (12, 0))
	w.frames["First Frame"].addWidget(cPhone, (13, 0))
	w.frames["First Frame"].addWidget(cPhone2, (14, 0))

#contact widgets
	'''
	w.frames["Third Frame"].addWidget(cinfo, (0, 0))
	cinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	cinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["Third Frame"].addWidget(pup, (1, 0))
	w.frames["Third Frame"].addWidget(hPhone, (2, 0))
	w.frames["Third Frame"].addWidget(cPhone, (3, 0))
	w.frames["Third Frame"].addWidget(cPhone2, (4, 0))
	'''

#database info widgets
	w.frames["First Frame"].addWidget(pinfo, (15, 0))
	pinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(bCode, (16, 0))
	#w.frames["Fourth Frame"].addWidget(sid, (2, 0))
	
#payment widgets
	'''
	w.frames["Fourth Frame"].addWidget(tpd, (6, 0))
	w.frames["Fourth Frame"].addWidget(tpa, (7, 0))
	w.frames["Fourth Frame"].addWidget(tp, (8, 0))
	w.frames["Fourth Frame"].addWidget(tpo, (9, 0))
	'''

#class widget
	'''
	w.frames["Sixth Frame"].addWidget(sType, (4, 0))
	w.frames["Sixth Frame"].addWidget(cAwarded, (5, 0))
	w.frames["Sixth Frame"].addWidget(cRemaining, (6, 0))
	w.frames["Sixth Frame"].addWidget(ctime, (7, 0))
	'''

#notes widget
	w.frames["First Frame"].addWidget(ninfo, (17, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First Frame"].addWidget(notes, (18, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=2)
	notes.config(height=8, width=32)

	w.frames["Fourth Frame"].addWidget(checkin25, (0, 2))
	w.frames["Fourth Frame"].addWidget(checkin50, (0, 4))
	w.frames["Fourth Frame"].addWidget(checkin100, (0, 6))

	checkin25.label.config(width=4)
	checkin50.label.config(width=4)
	checkin100.label.config(width=4)

	checkin25.entry.config(width=3)
	checkin50.entry.config(width=3)
	checkin100.entry.config(width=3)

	checkin25.setData(d.studentList[w.s].datapoints['25s'])
	checkin50.setData(d.studentList[w.s].datapoints['50s'])
	checkin100.setData(d.studentList[w.s].datapoints['100s'])

	'''
	baclass = Buttonbox(text='awardclass', lang=w.lang, repr='aclass')
	baoclass = Buttonbox(text='awardoneclass', lang=w.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w.lang, repr='baaclasses')
	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')

	w.frames["Eigth Frame"].addWidget(bgold, (1, 0))
	w.frames["Eigth Frame"].addWidget(bbasic, (1, 1))
	w.frames["Eigth Frame"].addWidget(baoclass, (1, 2))

	baoclass.config(cmd=caddone, width=12)
	bgold.config(cmd=lambda: caddmorex(60), width=12)
	bbasic.config(cmd=lambda: caddmorex(15), width=12)

	baoclass.selfframe.grid(padx=2)
	bgold.selfframe.grid(padx=2)
	bbasic.selfframe.grid(padx=2)
	
	
	#w.frames["Sixth Frame"].addWidget(baclass, (0, 0))
	#w.frames["Sixth Frame"].addWidget(baac, (2, 0))
	#baclass.config(cmd=lambda: cpicker(w.lang))
	#baac.config(cmd=cadd)
	'''





	w.frames["Seventh Frame"].addWidget(portr, (0, 0))

	w.attinfo = attinfo
	w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Eleventh Frame"].grid(rowspan=3, sticky=W)
	w.attinfo.canvas.config(width=720)
	w.attinfo.editwidget = False
	w.attinfo.clast = False

#renew classes button
	'''
	def renC():
		try:
			d.studentList[w.s]
		except:
			return

		r = renew(w.lang)
		dp = d.studentList[w.s].datapoints
		dp['cRemaining'] = dp['cRemaining'] + r
		dp['cAwarded'] = dp['cAwarded'] + r
		dp['expire'] = d.calcExpir(datetime.now().date(), r)
		cRemaining.setData(dp['cRemaining'])
		cAwarded.setData(dp['cAwarded'])

	w.ren = Buttonbox(text='Renew classes', lang=w.lang, repr='ren')
	w.frames["Twelfth Frame"].addWidget(w.ren, (1, 0))
	w.ren.selfframe.grid(sticky=S)
	w.ren.config(cmd=renC)
	'''
	
	w.attinfo.editwidget=False
	w.attinfo.canvas.config(width=700, height=520)

	#reset portrait
	portr.setData('monet_sm.jpg')

	s = d.studentList[i]
	#print(s.datapoints['attinfo'])
	print(s.datapoints['notes'])
	w.populate(s.datapoints)

	tdp = dict(w.collect(s.datapoints))

	#if amount owed is larger than amount paid, color amount owed in red
	if s.datapoints['tpa'] < s.datapoints['tpo']: tpo.entry.config(bg='red')

	def collect():
		if not changed():
			t.destroy()
			return
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w.lang): return

		#if the barcode changes
		cbcode = bCode.getData()
		if s.datapoints['bCode'] != cbcode:
			if not ase(d.studentList[cbcode].datapoints['firstName'], w.lang):
				return
			else:
				dbcode = s.datapoints['bCode']
				d.studentList[cbcode] = s
				del d.studentList[dbcode]

		s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
		d.saveData()

		t.destroy()


	def changed():
		ctdp = dict(w.collect(s.datapoints))
		#print(ctdp)
		for key in tdp.keys():
			if ctdp[key] != tdp[key]:
				return True
		return False


	def quit():
		if not changed():
			t.destroy()
		elif ret('a', w.lang):
			t.destroy()


	sstudent = Buttonbox(text='savestudent', lang=w.lang, repr='sstudent')
	w.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)

	bclose = Buttonbox(text='close', lang=w.lang, repr='bclose')
	w.frames["Fifth Frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=quit)

	w.frames["Seventh Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

	#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	
	t.mainloop()