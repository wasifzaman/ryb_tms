from tkinter import *
from tkinter.scrolledtext import ScrolledText

from textbox import Textbox


class LongTextbox(Textbox):

	def config(self, **kwargs):
		if 'height' in kwargs:
			self.sentry.config(height=kwargs['height'])
		if 'width' in kwargs:
			self.sentry.config(width=kwargs['width'])
		if 'text' in kwargs:	
			self.sentry.insert(END, kwargs['text'])
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
		
	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text])
		self.sentry = ScrolledText(self.parent, relief=SOLID)

		self.label.grid(row=self.row, column=self.column)
		self.sentry.grid(row=self.row, column=self.column+1, sticky=E)

	def getData(self):
		return self.sentry.get('1.0', END + '-1c')

	def setData(self, data):
		self.sentry.delete('1.0', END)
		self.config(text=data)