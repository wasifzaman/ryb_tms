from tkinter import *
from datetime import time, date, datetime

from textbox import IntTextbox

class Datebox(IntTextbox):

	def config(self, **kwargs):

		if 'm' in kwargs and 'd' in kwargs and 'y' in kwargs:
			m, d, y = StringVar(), StringVar(), StringVar()
			m.set(kwargs['m'])
			d.set(kwargs['d'])
			y.set(kwargs['y'])
			self.mEntry.config(textvariable=m)
			self.dEntry.config(textvariable=d)
			self.yEntry.config(textvariable=y)
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.selfframe = Frame(self.parent, bg='black')
		self.mdy_frame = Frame(self.selfframe, relief=FLAT, bg='white')
		self.mdy_continaer = Frame(self.mdy_frame, relief=FLAT, bg='white')
		self.label = Label(self.parent, text=self.text, width=15, anchor=E)
		self.dLabel = Label(self.mdy_continaer, text='/', bg='white')
		self.yLable = Label(self.mdy_continaer, text='/', bg='white')

		self.mEntry = Entry(self.mdy_continaer, relief=FLAT, width=4, justify=CENTER)
		self.dEntry = Entry(self.mdy_continaer, relief=FLAT, width=4, justify=CENTER)
		self.yEntry = Entry(self.mdy_continaer, relief=FLAT, width=7, justify=CENTER)

		self.mdy_frame.pack(padx=1, pady=1, fill=X)
		self.mdy_continaer.pack()
		self.selfframe.grid(row=self.row, column=self.column+1, stick=E+W)

		self.label.grid(row=self.row, column=self.column)
		self.dLabel.grid(row=1, column=2)
		self.yLable.grid(row=1, column=4)

		self.mEntry.grid(row=1, column=1, padx=(1, 0))
		self.dEntry.grid(row=1, column=3)
		self.yEntry.grid(row=1, column=5, padx=(0, 1))

		self.bind()

	def OnValidate(self, d, i, P, s, S, v, V, W, digit_type):
		if d == '0': return True
		if not S.isdigit(): return False
		if digit_type == 'date' or digit_type == 'month':
			if len(s) == 2: return False
		elif digit_type == 'year':
			if len(s) == 4: return False
		return True

	def bind(self):
		self.mEntry.config(validate="all", validatecommand=(self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'date'))
		self.dEntry.config(validate="all", validatecommand=(self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'month'))
		self.yEntry.config(validate="all", validatecommand=(self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'year'))

	def getData(self):
		try:
			date = self.mEntry.get() + '/' + self.dEntry.get() + '/' + self.yEntry.get()
			dt = datetime.strptime(date, '%m/%d/%Y')
			return datetime.strftime(dt, '%m/%d/%Y')
		except ValueError:
			return '01/01/1900'

	def setData(self, data):
		date = data.split('/')
		m, d, y = date[0], date[1], date[2]

		self.config(m=m, d=d, y=y)
