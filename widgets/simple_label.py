from tkinter import *

from textbox import Textbox

class Labelbox(Textbox):
	def __init__(self, **kwargs):
		Textbox.__init__(self, **kwargs)
		self.bold = False
		if 'bold' in kwargs: self.bold = kwargs['bold']

	def config(self, **kwargs):
		if 'text' in kwargs:
			self.text=kwargs['text']
			self.label.config(text=self.text)
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])

	def getData(self):
		return self.text

	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text])
		self.label.grid(row=self.row, column=self.column)

		if self.bold:
			self.label.config(font=('Verdana', 11, 'bold'))

	def hide(self):
		self.label.grid_forget()

	def show(self):
		self.label.grid()