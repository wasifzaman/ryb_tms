from tkinter import *

from widget import Widget

class Textbox(Widget):
	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.repr = kwargs['repr']
		self.lang = kwargs['lang']
		self.height = 1
		self.width = 2

	def config(self, **kwargs):
		if 'text' in kwargs:
			s = StringVar()
			s.set(kwargs['text'])
			self.entry.config(textvariable=s)
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text].strip())

	def OnValidate(self, d, i, P, s, S, v, V, W):
		return True

	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text].strip(), width=12, anchor=E)
		self.entry = Entry(self.parent, relief=SOLID)

		self.label.grid(row=self.row, column=self.column, sticky=E)
		self.entry.grid(row=self.row, column=self.column+1)

		self.bind()

	def bind(self):
		vcmd = (self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entry.config(validate="all", validatecommand=vcmd)

	def getData(self):
		return self.entry.get()

	def setData(self, data):
		self.config(text=data)

	def hide(self):
		self.label.grid_forget()
		self.entry.grid_forget()

class TextboxNoEdit(Textbox):
	def config(self, **kwargs):
		if 'text' in kwargs:
			s = StringVar()
			s.set(kwargs['text'])
			self.entry.config(state=NORMAL)
			self.entry.config(textvariable=s)
			self.entry.config(state=DISABLED)
		if 'lang' in kwargs:			
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text].strip())
		
	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text].strip(), width=15, anchor=E)
		self.entry = Entry(self.parent, relief=SOLID, state=DISABLED,
			disabledbackground='white', disabledforeground='black')

		self.label.grid(row=self.row, column=self.column)
		self.entry.grid(row=self.row, column=self.column+1)

		self.bind()

class IntTextbox(Textbox):
	def OnValidate(self, d, i, P, s, S, v, V, W):
		if S.isdigit():
			return True
		return False

	def getData(self):
		entry_ = self.entry.get()
		if not entry_.isdigit() or len(entry_.strip()) == 0:
			return 0
		else:
			return int(entry_)

class MoneyTextbox(IntTextbox):
	def OnValidate(self, d, i, P, s, S, v, V, W):
		if S.isdigit():
			return True
		else:
			return S == '.' and '.' not in self.entry.get()# or False
		return False

	def getData(self):
		e = self.entry.get()
		if e == '': return 0.00
		try:
			return float("%.2f" % float(e))
		except:
			return 0.00