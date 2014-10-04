from tkinter import *
from tkinter.scrolledtext import ScrolledText
import inspect

'''

Notes:
	- widget language attribute must be a dictionary
	- when copying widget settings, use dict(settings) to make copy




'''


class Textbox:

	def __init__(self, **kwargs):
		def apply_attribute(attrib):
			return kwargs[attrib] if attrib in kwargs else False

		self.language = apply_attribute('language')
		self.fill_tag = apply_attribute('fill_tag')
		self.filter = apply_attribute('filter')

		self.label_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'label_settings') else dict(apply_attribute('settings').label_settings)
		for attrib, value in {'text': self.language[apply_attribute('label_text')].strip(),
			'width': apply_attribute('label_width'),
			'anchor': apply_attribute('anchor')
			}.items():
			if value: self.label_attributes.update({attrib: value})
		
		self.entry_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'entry_settings') else dict(apply_attribute('settings').entry_settings)
		for attrib, value in {'width': apply_attribute('entry_width')
			}.items():
			if value: self.entry_attributes.update({attrib, value})

		
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
		if self.filter == 'int' and S.isdigit(): 
			return True
		if not self.filter:
			return True
		return False

	def create_widget(self, **kwargs):

		self.encompass_frame = Frame(kwargs['parent_obj'])

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_frame)
		self.entry = Entry(self.encompass_frame)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)
		
		self.label.grid(row=0, column=0)
		self.entry.grid(row=0, column=1)
		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)

		vcmd = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entry.config(validate="all", validatecommand=vcmd)

	def get_data(self):
		return self.entry.get()

	def set_data(self, data):
		self.config(entry_text=data)

	def hide_widget(self):
		self.encompass_frame.grid_forget()

	def show_widget(self, new_grid_row=False, new_grid_column=False):
		self.grid_row = new_grid_row if new_grid_row else self.grid_row
		self.grid_column = new_grid_column if new_grid_column else self.grid_column

		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)


class Button:

	def __init__(self, **kwargs):
		def apply_attribute(attrib):
			return kwargs[attrib] if attrib in kwargs else False

		self.language = apply_attribute('language')

		self.label_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'label_settings') else dict(apply_attribute('settings').label_settings)
		for attrib, value in {'text': self.language[apply_attribute('text')].strip(),
			'width': apply_attribute('width'),
			'bg': apply_attribute('bg'),
			'fg': apply_attribute('fg')
			}.items():
			if value: self.label_attributes.update({attrib: value})

		self.hover_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'hover_settings') else dict(apply_attribute('settings').hover_settings)
		for attrib, value in {'bg': apply_attribute('hover_bg'),
			'fg': apply_attribute('hover_fg')
			}.items():
			if value: self.hover_attributes.update({attrib: value})

	def config(self, **kwargs):
		if 'language' in kwargs:
			self.language = kwargs['language']
			self.label_text.config(text=self.language[self.label_text].strip())

		if 'command' in kwargs:
			self.command = kwargs['command']
			self.args = inspect.getargspec(kwargs['command']).args
			if len(self.args) > 0 and self.args[0] != 'self':
				self.label.bind('<ButtonRelease-1>', self.command)
				self.label.bind('<Button-1>', self.label.config(bg='#195CBF'))
				self.label.bind('<space>', self.command)
			else:
				self.label.bind('<ButtonRelease-1>', lambda event: self.command())
				self.label.bind('<space>', lambda event: self.command())

		return

	def enter(self, event):
		for attrib, value in self.hover_attributes.items():
			if value: self.label.__setitem__(attrib, value)

	def leave(self, event):
		for attrib, value in self.label_attributes.items():
			if value and (attrib == 'fg' or attrib == 'bg'):
				self.label.__setitem__(attrib, value)

	def create_widget(self, **kwargs):

		self.encompass_frame = Frame(kwargs['parent_obj'])

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_frame)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		self.label.bind('<Enter>', self.enter)
		self.label.bind('<Leave>', self.leave)

		self.label.grid()
		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)


class Coin_widget:

	def __init__(self, **kwargs):
		def apply_attribute(attrib):
			return kwargs[attrib] if attrib in kwargs else False

		self.language = apply_attribute('language')
		self.fill_tag = apply_attribute('fill_tag')

		self.label_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'label_settings') else dict(apply_attribute('settings').label_settings)
		for attrib, value in {'text': self.language[apply_attribute('label_text')].strip(),
			'width': apply_attribute('label_width'),
			'anchor': apply_attribute('anchor')
			}.items():
			if value: self.label_attributes.update({attrib: value})
		
		self.whole_entry_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'whole_entry_settings') else dict(apply_attribute('settings').whole_entry_settings)
		for attrib, value in {'width': apply_attribute('whole_entry_width')
			}.items():
			if value: self.whole_entry_attributes.update({attrib, value})

		self.cent_entry_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'cent_entry_settings') else dict(apply_attribute('settings').cent_entry_settings)
		for attrib, value in {'widget': apply_attribute('cent_entry_width')
			}.items():
			if value: self.cent_entry_attributes.update({attrib, value})

	def config(self, **kwargs):
		if 'language' in kwargs:
			self.language = kwargs['language']
			self.label_text.config(text=self.language[self.label_text].strip())

		return

	def OnValidate(self, d, i, P, s, S, v, V, W, widget=False, limit=False):
		if limit and len(getattr(self, widget).get()) >= int(limit):
			if len(P) < len(getattr(self, widget).get()): return True
			return False
		if S.isdigit(): 
			return True
		return False

	def create_widget(self, **kwargs):

		self.encompass_frame = Frame(kwargs['parent_obj'])

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_frame)
		self.whole_entry = Entry(self.encompass_frame)
		self.cent_entry = Entry(self.encompass_frame)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.whole_entry_attributes.items():
			if value: self.whole_entry.__setitem__(attrib, value)

		for attrib, value in self.cent_entry_attributes.items():
			if value: self.cent_entry.__setitem__(attrib, value)
		
		self.label.grid(row=0, column=0)
		self.whole_entry.grid(row=0, column=1)
		Label(self.encompass_frame, text='.', width=1).grid(row=0, column=2)
		self.cent_entry.grid(row=0, column=3)
		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)

		vcmd_whole = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		vcmd_cent = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'cent_entry', 2)
		self.whole_entry.config(validate="all", validatecommand=vcmd_whole)
		self.cent_entry.config(validate="all", validatecommand=vcmd_cent)

	def get_data(self):
		return self.entry.get()

	def set_data(self, data):
		self.config(entry_text=data)

	def hide_widget(self):
		self.encompass_frame.grid_forget()

	def show_widget(self, new_grid_row=False, new_grid_column=False):
		self.grid_row = new_grid_row if new_grid_row else self.grid_row
		self.grid_column = new_grid_column if new_grid_column else self.grid_column

		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)

	pass