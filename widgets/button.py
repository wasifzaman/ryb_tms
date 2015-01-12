from tkinter import *
import inspect

from textbox import Textbox

class Buttonbox(Textbox):

	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.repr = kwargs['repr']
		self.lang = kwargs['lang']
		self.width = 30
		self.idlebg = '#657FCF'
		self.hoverbg = '#405DB2'
		self.idleborder = '#7D9DFF'
		self.hoverborder = '#5C7DBD'
		self.fg = 'white'
		self.hoverfg = 'white'

	def config(self, **kwargs):
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.button.config(text=self.lang[self.text])
		if 'cmd' in kwargs:
			self.cmd = kwargs['cmd']
			self.args = inspect.getargspec(kwargs['cmd']).args
			if len(self.args) > 0 and self.args[0] != 'self':
				self.button.bind('<ButtonRelease-1>', self.cmd)
				self.button.bind('<Button-1>', self.button.config(bg='#195CBF'))
				self.button.bind('<space>', self.cmd)
			else:
				self.button.bind('<ButtonRelease-1>', lambda e: self.cmd())
				self.button.bind('<space>', lambda e: self.cmd())
			if hasattr(self, 'timeslot_'):
				self.timeslot_.bind('<ButtonRelease-1>', self.cmd)
		if 'width' in kwargs:
			self.width = kwargs['width']
			self.button.config(width=self.width)

	def enter(self, event):
		self.button.config(bg=self.hoverbg, fg=self.hoverfg)
		self.selfframe.config(bg=self.hoverborder)

	def leave(self, event):
		self.button.config(bg=self.idlebg, fg=self.fg)
		self.selfframe.config(bg=self.idleborder)
		
	def setData(self, data):
		self.config(text=data)

	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.selfframe = Frame(self.parent, bg=self.idleborder, bd=1)
		self.button = Label(self.selfframe, text=self.lang[self.text], width=self.width, bg=self.idlebg, fg=self.fg, \
			font=('Verdana', 11), pady=3)

		self.button.bind('<Enter>', self.enter)
		self.button.bind('<Leave>', self.leave)

		self.selfframe.grid(row=self.row, column=self.column, pady=2)
		self.button.pack()