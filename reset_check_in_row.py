from tkinter import *
from dataHandler import *
from uiHandler22 import *
from preBuilts2 import *
from widget import Widget


def main(lang, d, s):

	d.loadData()

	t = Window(top='top')
	t.attributes('-fullscreen', False)
	t.geometry('250x250')
	t.resizable(0, 0)
	t.grab_set()
	t.focus_set()

	w = AppWindow(t.mainFrame)

	w.lang = lang
	w.s = s

	#frame initialization
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))

	bset = Buttonbox(text='set', lang=language, repr='bset')
	breset = Buttonbox(text='reset', lang=language, repr='breset')

	'''
	bset10 = Buttonbox(text='set', lang=language, repr='bset10')
	breset10 = Buttonbox(text='reset', lang=language, repr='breset10')
	bset20 = Buttonbox(text='set', lang=language, repr='bset20')
	breset20 = Buttonbox(text='reset', lang=language, repr='breset20')
	bset50 = Buttonbox(text='set', lang=language, repr='bset50')
	breset50 = Buttonbox(text='reset', lang=language, repr='breset50')
	bset100 = Buttonbox(text='set', lang=language, repr='bset100')
	breset100 = Buttonbox(text='reset', lang=language, repr='breset100')
	'''

	checkin10 = IntTextbox(text='10s', lang=language, repr='10s')
	checkin20 = IntTextbox(text='20s', lang=language, repr='20s')
	checkin50 = IntTextbox(text='50s', lang=language, repr='50s')
	checkin100 = IntTextbox(text='100s', lang=language, repr='100s')

	w.frames["First Frame"].addWidget(checkin10, (1, 0))
	w.frames["First Frame"].addWidget(checkin20, (2, 0))
	w.frames["First Frame"].addWidget(checkin50, (3, 0))
	w.frames["First Frame"].addWidget(checkin100, (4, 0))

	'''
	w.frames["First Frame"].addWidget(bset10, (1, 2))
	w.frames["First Frame"].addWidget(bset20, (2, 2))
	w.frames["First Frame"].addWidget(bset50, (3, 2))
	w.frames["First Frame"].addWidget(bset100, (4, 2))

	w.frames["First Frame"].addWidget(breset10, (1, 3))
	w.frames["First Frame"].addWidget(breset20, (2, 3))
	w.frames["First Frame"].addWidget(breset50, (3, 3))
	w.frames["First Frame"].addWidget(breset100, (4, 3))
	'''

	w.frames["Second Frame"].addWidget(bset, (1, 0))
	w.frames["Second Frame"].addWidget(breset, (1, 1))

	checkin10.label.config(width=4)
	checkin20.label.config(width=4)
	checkin50.label.config(width=4)
	checkin100.label.config(width=4)

	checkin10.entry.config(width=5)
	checkin20.entry.config(width=5)
	checkin50.entry.config(width=5)
	checkin100.entry.config(width=5)

	bset.button.config(width=5)
	breset.button.config(width=5)

	'''
	bset10.button.config(width=10)
	breset10.button.config(width=10)
	bset20.button.config(width=10)
	breset20.button.config(width=10)
	bset50.button.config(width=10)
	breset50.button.config(width=10)
	bset100.button.config(width=10)
	breset100.button.config(width=10)
	'''

	checkin10.setData(d.studentList[w.s].datapoints['10s'])
	checkin20.setData(d.studentList[w.s].datapoints['20s'])
	checkin50.setData(d.studentList[w.s].datapoints['50s'])
	checkin100.setData(d.studentList[w.s].datapoints['100s'])

	def set():
		s = d.studentList[w.s]
		s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
		d.saveData()
		t.destroy()

	def reset():
		checkin10.setData(0)
		checkin20.setData(0)
		checkin50.setData(0)
		checkin100.setData(0)
		d.saveData()

	bset.config(cmd=set)
	breset.config(cmd=reset)

	t.mainloop()