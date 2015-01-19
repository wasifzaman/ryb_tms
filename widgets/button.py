from tkinter import *
import inspect

from textbox import Textbox


class Buttonbox(Textbox):

	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.repr = kwargs['repr']
		self.width = 30
		self.idlebg = '#657FCF'
		self.hoverbg = '#405DB2'
		self.idleborder = '#7D9DFF'
		self.hoverborder = '#5C7DBD'
		self.fg = 'white'
		self.hoverfg = 'white'

	def config(self, **kwargs):
		if 'lang' in kwargs:
			pass
			#self.lang = kwargs['lang']
			#self.label.config(text=self.lang[self.text])
		if 'cmd' in kwargs:
			self.command = kwargs['cmd']
			self.label.bind('<Button-1>', lambda event: self.command())
		if 'width' in kwargs:
			self.width = kwargs['width']
			self.label.config(width=self.width)

	def enter(self, event):
		self.label.config(bg=self.hoverbg, fg=self.hoverfg)
		self.selfframe.config(bg=self.hoverborder)

	def leave(self, event):
		self.label.config(bg=self.idlebg, fg=self.fg)
		self.selfframe.config(bg=self.idleborder)
		
	def setData(self, data):
		self.config(text=data)

	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.selfframe = Frame(self.parent, bg=self.idleborder, bd=1)
		self.label = Label(self.selfframe, text=self.text, width=self.width, bg=self.idlebg, fg=self.fg, \
			font=('Verdana', 11), pady=3)

		self.label.pack()
		
		self.label.bind('<Enter>', self.enter)
		self.label.bind('<Leave>', self.leave)

		self.selfframe.grid(row=self.row, column=self.column, pady=2)