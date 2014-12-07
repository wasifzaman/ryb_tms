from uiHandler22 import *
import editS2
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

#
	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#sT
	w.sT = Table(repr='stable', edit=False)
	stableh = [w.lang['Barcode'], w.lang['First Name'], \
	w.lang['Last Name'], w.lang['Chinese Name'], w.lang['Date of Birth']]
	w.sT.build(headers=stableh, data=[[]])

	def sTbind(f):
		def fsb(p):
			i = w.sT.data[p[0]-1][0]
			try:
				f(i)
			except:
				pass
				#print(w.sT.data[p[0]-1][0])

		try:
			for pos, cell in w.sT.cells.items():
				cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))
		except:
			pass
			#print("cells could not be bound")

#frame initialization
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (2, 1))
	w.newFrame("Fourth Frame", (4, 1))
	w.newFrame("Fifth Frame", (3, 0))

	w.frames["Second Frame"].rowconfigure(0, weight=5, minsize=470)
	w.frames["Second Frame"].columnconfigure(0, weight=5, minsize=630)

	w.frames["Fifth Frame"].grid(columnspan=3)

#widget for scan
	w.sby = Picker(repr='sby', text=w.lang['Search By'], rads=[(w.lang['Barcode'], 'bCode'), \
		(w.lang['First Name'], 'firstName'), \
		(w.lang['Last Name'], 'lastName'), \
		(w.lang['Chinese Name'], 'chineseName'), \
		(w.lang['Phone Number'], 'phoneNumber'), \
		(w.lang['Date of Birth'], 'dob')])

	w.frames["First Frame"].addWidget(w.sby, (0, 0))
	w.frames["First Frame"].addWidget(bsearch, (1, 0))
	
#buttons for scrolling db
	fward = Buttonbox(text='>> Next 30 >>', lang=w.lang, repr='>>')
	bward = Buttonbox(text='<< Previous 30 <<', lang=w.lang, repr='<<')
	blast = Buttonbox(text='>>> Last Page >>>', lang=w.lang, repr='>>>')
	w.frames["Fifth Frame"].addWidget(fward, (1, 1))
	w.frames["Fifth Frame"].addWidget(bward, (1, 0))
	w.frames["Fifth Frame"].addWidget(blast, (1, 2))

	fward.config(width=17)
	bward.config(width=17)
	blast.config(width=17)

	fward.selfframe.grid(padx=2)
	bward.selfframe.grid(padx=2)
	blast.selfframe.grid(padx=2)

	w.frames["Second Frame"].addWidget(w.sT, (2, 0))
	w.sT.canvas.config(width=700, height=480)

	#sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), \
	#	('Last Name', 'lastName'), ('Chinese Name', 'chineseName'), \
	#	('Phone Number', 'phoneNumber')]

	sL = [[]]
	for s in d.studentList.values():
		dp = s.datapoints
		sL[0].append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL[0].sort()

#create pages
	#print(len(sL[0]))
	if len(sL[0]) > 30:
		l = []
		for s in sL[0]:
			l.append(s)
			if len(l) >= 30:
				sL.append(l)
				l = []
		sL.append(l)

	#if last page is blank (if num students is multiple of 30)
	if len(sL[-1]) == 0 and len(sL) != 1: sL.pop()

	w.pNum = 1

		
	def toPage(p):
		#temp workaround while table is fixed
		for child in w.frames["Second Frame"].winfo_children():
			child.destroy()

		w.sT.build(headers=stableh, data=sL[p])
		w.frames["Second Frame"].addWidget(w.sT, (2, 0))
		w.sT.canvas.config(width=700, height=450)
		sTbind(lambda i: editS2.main(w.lang, top=True, i=i, d=d))

	def f():
		if w.pNum == len(sL) - 1: return
		toPage(w.pNum + 1)
		w.pNum = w.pNum + 1
		
	def b():
		if w.pNum == 1: return
		toPage(w.pNum - 1)
		w.pNum = w.pNum - 1

	def l():
		w.pNum = len(sL) - 1
		toPage(w.pNum)	

	if len(sL[0]) > 30:
		toPage(1)
		fward.config(cmd=f)
		bward.config(cmd=b)
		blast.config(cmd=l)
	else:
		toPage(0)
#
	def s():
		try:
			w.s = w.sby.getData()[1]


			if w.sby.getData()[0] != 'bCode':
				sty = w.sby.getData()[0]
				sdp = w.sby.getData()[1]

				sl = []

				for s in d.studentList:
					dp = False
					if sty == 'phoneNumber':
						if d.studentList[s].datapoints['hPhone'] == sdp or \
							d.studentList[s].datapoints['cPhone'] == sdp or \
							d.studentList[s].datapoints['cPhone2'] == sdp:
							dp = d.studentList[s].datapoints

					elif d.studentList[s].datapoints[sty] == sdp:
						dp = d.studentList[s].datapoints
					
					if dp:
						sl.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName']])


				if len(sl) == 0:
					nos(w.lang)
					return

				w.s = sl[0][0]
				if len(sl) > 1:
					sl.sort()
					w.s = spicker(sl)
					if not w.s: return

			editS2.main(w.lang, d=d, top=True, i=w.s)
		except:
			nos(w.lang)
			return


	w.frames["First Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())

	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

	#button for scan
	#Button(w.frames["First Frame"], text="try", command=s).grid()