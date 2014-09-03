import os.path
from tkinter import Label, N
from widget import Widget
from PIL import Image, ImageTk


class Photo(Widget):

	def __init__(self, **kwargs):

		try:
			self.repr = kwargs['repr']
			self.path = kwargs['path']
		except:
			print("widget could not be loaded")


	def config(self, **kwargs):

		try:
			self.path = kwargs['path']
			self.picture = Image.open(self.path)
			self.picture = self.picture.resize((200, 200), Image.ANTIALIAS)
			self.image = ImageTk.PhotoImage(self.picture)
			self.label.config(image=self.image)
		except:
			pass

		try:
			self.bgc = kwargs['bg']
			self.label.config(bg=self.bgc)
		except:
			pass


	def trytoplace(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']


	def place(self, **kwargs):

		try:
			self.trytoplace(**kwargs)
		except:
			print("widget could not be placed")

		self.picture = Image.open(self.path)
		self.image = ImageTk.PhotoImage(self.picture)

		self.label = Label(self.parent, image=self.image, bd=1)
		self.label.grid(row=self.row, column=self.column, pady=1)
		self.label.bind('<Button-1>', lambda e: self.label.focus_set())


	def getData(self):
		return self.path


	def setData(self, data):
		#le sigh
		if data == '' or 'N/A': return
		self.config(path=data)


	def hide(self):
		self.label.grid_forget()