from tkinter import *
from tkinter.scrolledtext import ScrolledText

'''

Notes:
	- widget language attribute must be a dictionary




'''


class Textbox(Widget):

	def __init__(self, **kwargs):
		def apply_attribute(attrib):
			return kwargs[attrib] if attrib in kwargs else False

		self.language = apply_attribute('language')
		self.fill_tag = apply_attribute('fill_tag')

		self.label_attributes = {'text': self.language[apply_attribute('label_text')].strip(),
			'width': apply_attribute('label_width'),
			'anchor': apply_attribute('anchor')}
		
		self.entry_attributes = {'width': apply_attribute('entry_width')}

	def config(self, **kwargs):
		if 'entry_text' in kwargs:
			field_string = StringVar()
			field_string.set(kwargs['entry_text'])
			self.entry_text.config(textvariable=field_string)

		if 'language' in kwargs:
			self.language = kwargs['language']
			self.label_text.config(text=self.language[self.label_text].strip())

		return

	def OnValidate(self, d, i, P, s, S, v, V, W):
		return True

	def create_widget(self, **kwargs):

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(kwargs['parent_obj'])
		self.entry = Entry(kwargs['parent_obj'])

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)
		
		self.label.grid(row=self.grid_row, column=self.grid_column)
		self.entry.grid(row=self.grid_row, column=self.grid_column + 1)

	def get_data(self):
		return self.entry.get()

	def set_data(self, data):
		self.config(entry_text=data)

	def hide_widget(self):
		self.label.grid_forget()
		self.entry.grid_forget()

	def show_widget(self, new_grid_row=False, new_grid_column=False):
		self.grid_row = new_grid_row if new_grid_row else self.grid_row
		self.grid_column = new_grid_column if new_grid_column else self.grid_column

		self.label.grid(row=self.grid_row, column=self.grid_column)
		self.entry.grid(row=self.grid_row, column=self.grid_column + 1)