from tkinter import *
from tkinter.scrolledtext import ScrolledText
from datetime import datetime
import inspect

'''

Notes:
	- widget language attribute must be a dictionary
	- when copying widget settings, use dict(settings) to make copy
	- date widget's interactive adding of / creates new entry widgets each time / is added
	- date widget returns and sets datetime object




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
			if value: self.entry_attributes.update({attrib: value})

		
	def config(self, **kwargs):
		if 'entry_text' in kwargs:
			field_string = StringVar()
			field_string.set(kwargs['entry_text'])
			self.entry.config(textvariable=field_string)
			self.entry.config(validate="all", validatecommand=self.vcmd)

		if 'language' in kwargs:
			self.language = kwargs['language']
			self.label.config(text=self.language[self.label.get()].strip())

		return

	def OnValidate(self, d, i, P, s, S, v, V, W):
		if self.filter == 'int' and S.isdigit(): 
			return True
		if self.filter == 'all':
			return False
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

		self.vcmd = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entry.config(validate="all", validatecommand=self.vcmd)

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


class Scrolled_textbox:

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
		for attrib, value in {'width': apply_attribute('entry_width'),
			'height': apply_attribute('entry_height')
			}.items():
			if value: self.entry_attributes.update({attrib: value})

	def config(self, **kwargs):
		if 'entry_text' in kwargs:
			self.entry.insert(END, kwargs['entry_text'])

		if 'language' in kwargs:
			self.language = kwargs['language']
			self.label.config(text=self.language[self.label.get()].strip())

		return

	def create_widget(self, **kwargs):

		self.encompass_frame = Frame(kwargs['parent_obj'])

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_frame)
		self.entry = ScrolledText(self.encompass_frame)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)
		
		self.label.grid(row=0, column=0)
		self.entry.grid(row=0, column=1)
		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)

	def get_data(self):
		return self.entry.get('1.0', END + '-1c')

	def set_data(self, data):
		self.entry.delete('1.0', END)
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
			self.label.config(text=self.language[self.label.get()].strip())

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
		
		self.entry_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'entry_settings') else dict(apply_attribute('settings').entry_settings)
		for attrib, value in {'width': apply_attribute('entry_width'),
			'text': apply_attribute('entry_text')
			}.items():
			if value: self.entry_attributes.update({attrib: value})

	def config(self, **kwargs):
		if 'entry_text' in kwargs:
			field_string = StringVar()
			field_string.set(kwargs['entry_text'])
			self.entry.config(textvariable=field_string)
			self.entry.config(validate="all", validatecommand=self.vcmd)

		if 'language' in kwargs:
			self.language = kwargs['language']
			self.label.config(text=self.language[self.label.get()].strip())

		return

	def OnValidate(self, d, i, P, s, S, v, V, W, limit=False):
		if len(P) < len(s):
			return True
		if limit and s.find('.') != -1 and len(P[P.find('.'):]) > int(limit) + 1:
			return False
		if S.isdigit():
			return True
		if S == '.' and s.find('.') == -1:
			return True
		return False

	def create_widget(self, **kwargs):

		self.encompass_frame = Frame(kwargs['parent_obj'])

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_frame)
		self.entry = Entry(self.encompass_frame)

		self.vcmd = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 2)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)
			if value and attrib == 'text':
				field_string = StringVar()
				field_string.set(value)
				self.entry.config(textvariable=field_string)
				self.entry.config(validate="all", validatecommand=self.vcmd)
		
		self.label.grid(row=0, column=0)
		self.entry.grid(row=0, column=1)
		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)

		self.entry.config(validate="all", validatecommand=self.vcmd)

	def get_data(self):
		return float(self.entry.get())

	def set_data(self, data):
		self.config(entry_text=int(str(data)[:str(data).index('.')]))

	def hide_widget(self):
		self.encompass_frame.grid_forget()

	def show_widget(self, new_grid_row=False, new_grid_column=False):
		self.grid_row = new_grid_row if new_grid_row else self.grid_row
		self.grid_column = new_grid_column if new_grid_column else self.grid_column

		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)


class Date_widget(Textbox):

	def OnValidate(self, d, i, P, s, S, v, V, W):
		if len(getattr(self, 'entry').get()) == 10:
			if len(P) < len(getattr(self, 'entry').get()): return True
			return False
		if len(P) == 2 or len(P) == 5:
			if len(P) < len(getattr(self, 'entry').get()): return True
			fill_entry = P + '/'
			self.entry = Entry(self.encompass_frame)
			
			for attrib, value in self.entry_attributes.items():
				if value: self.entry.__setitem__(attrib, value)

			self.entry.grid(row=0, column=1)
			self.entry.insert(0, fill_entry)
			
			self.vcmd = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
			self.entry.config(validate="all", validatecommand=self.vcmd)

			self.entry.focus_set()
		if S.isdigit():
			return True
		return False

	def get_data(self):
		return datetime.strptime(self.entry.get(), '%m/%d/%Y')

	def set_data(self, data):
		field_string = StringVar()
		field_string.set(datetime.strftime(data, '%m/%d/%Y'))
		self.entry.config(textvariable=field_string)
		self.entry.config(validate="all", validatecommand=self.vcmd)


class Entry_category:

	def __init__(self, **kwargs):
		def apply_attribute(attrib):
			return kwargs[attrib] if attrib in kwargs else False

		self.language = apply_attribute('language')
		self.filter = apply_attribute('filter')
		self.categories = apply_attribute('categories')

		self.label_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'label_settings') else dict(apply_attribute('settings').label_settings)
		for attrib, value in {'text': self.language[apply_attribute('label_text')].strip(),
			'width': apply_attribute('label_width'),
			'anchor': apply_attribute('anchor')
			}.items():
			if value: self.label_attributes.update({attrib: value})
		
		self.entry_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'entry_settings') else dict(apply_attribute('settings').entry_settings)
		for attrib, value in {'width': apply_attribute('entry_width')
			}.items():
			if value: self.entry_attributes.update({attrib: value})

		self.categories_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'categories_settings') else dict(apply_attribute('settings').categories_settings)
		for attrib, value in {'width': apply_attribute('categories_width')
			}.items():
			if value: self.categories_attributes.update({attrib: value})

		self.categories_hover_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'categories_hover_settings') else dict(apply_attribute('settings').categories_hover_settings)
		for attrib, value in {'bg': apply_attribute('hover_bg'),
			'fg': apply_attribute('hover_fg')
			}.items():
			if value: self.categories_hover_attributes.update({attrib: value})

		self.selected_category_attributes = {} if not apply_attribute('settings') or not hasattr(apply_attribute('settings'), 'selected_category_settings') else dict(apply_attribute('settings').selected_category_settings)
		for attrib, value in {'width': apply_attribute('selected_category_width')
			}.items():
			if value: self.selected_category_attributes.update({attrib: value})

	def OnValidate(self, d, i, P, s, S, v, V, W):
		if self.filter == 'int' and S.isdigit(): 
			return True
		if self.filter == 'all':
			return False
		if not self.filter:
			return True
		return False

	def enter(self, event):
		for attrib, value in self.categories_hover_attributes.items():
			if value: event.widget.__setitem__(attrib, value)

	def leave(self, event):
		if hasattr(event.widget, 'selected') and event.widget.selected:
			for attrib, value in self.selected_category_attributes.items():
				if value and (attrib == 'fg' or attrib == 'bg'):
					event.widget.__setitem__(attrib, value)
			return

		for attrib, value in self.categories_attributes.items():
			if value and (attrib == 'fg' or attrib == 'bg'):
				event.widget.__setitem__(attrib, value)

	def click(self, event):
		for category in self.label_categories.values():
			if hasattr(category, 'selected') and category.selected:
				category.selected = False
				for attrib, value in self.categories_attributes.items():
					if value: category.__setitem__(attrib, value)
		for attrib, value in self.selected_category_attributes.items():
			if value: event.widget.__setitem__(attrib, value)
		event.widget.selected = True

		for fill_tag, category in self.label_categories.items():
			if category == event.widget:
				self.current_category = fill_tag

	def create_widget(self, **kwargs):

		self.encompass_frame = Frame(kwargs['parent_obj'])
		self.encompass_textbox = Frame(self.encompass_frame)
		self.encompass_categores = Frame(self.encompass_frame)

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_textbox)
		self.entry = Entry(self.encompass_textbox)
		self.label_categories = {}


		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)

		
		self.label.grid(row=0, column=0)
		self.entry.grid(row=0, column=1)
		column = 0
		for category in self.categories:
			for label, fill_tag in category.items():
				self.label_categories[fill_tag] = Label(self.encompass_categores, text=self.language[label])
				self.label_categories[fill_tag].grid(row=1, column=column)
				self.label_categories[fill_tag].bind('<Enter>', self.enter)
				self.label_categories[fill_tag].bind('<Leave>', self.leave)
				self.label_categories[fill_tag].bind('<Button-1>', self.click)

				if column == 0:
					self.current_category = fill_tag
					self.label_categories[fill_tag].selected = True

				column += 1

		for label in self.label_categories.values():
			for attrib, value in self.categories_attributes.items():
				if value: label.__setitem__(attrib, value)

		for attrib, value in self.selected_category_attributes.items():
			if value: self.label_categories[self.current_category].__setitem__(attrib, value)


		self.encompass_textbox.grid(row=0)
		self.encompass_categores.grid(row=1)
		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)

		self.vcmd = (self.encompass_frame.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entry.config(validate="all", validatecommand=self.vcmd)

	def get_data(self):
		return self.entry.get(), self.current_category

	def hide_widget(self):
		self.encompass_frame.grid_forget()

	def show_widget(self, new_grid_row=False, new_grid_column=False):
		self.grid_row = new_grid_row if new_grid_row else self.grid_row
		self.grid_column = new_grid_column if new_grid_column else self.grid_column

		self.encompass_frame.grid(row=self.grid_row, column=self.grid_column)


class Table:

	pass