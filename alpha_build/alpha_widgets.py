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
		self.height = apply_attribute('height')
		self.width = apply_attribute('width')

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

		self.encompass_frame = Frame(kwargs['parent_obj'], width=self.width, height=self.height)
		self.encompass_label = Frame(self.encompass_frame, width=int(self.width / 4), height=self.height)
		self.encompass_entry = Frame(self.encompass_frame, width=int(3 * self.width / 4), height=self.height)

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_label, height=int(self.height))
		self.entry = Entry(self.encompass_entry)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)


		self.label.pack(fill=X)
		self.entry.place(anchor="c", relwidth=1.0, relx=.5, rely=.5)
		self.encompass_frame.pack_propagate(0)
		self.encompass_label.pack_propagate(0)
		self.encompass_entry.pack_propagate(0)

		self.encompass_label.pack(side=LEFT)
		self.encompass_entry.pack(side=LEFT)
		self.encompass_frame.place(y=self.grid_row, x=self.grid_column)

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

		self.encompass_frame = Frame(kwargs['parent_obj'], width=self.width, height=self.height)
		self.encompass_label = Frame(self.encompass_frame, width=int(self.width / 4), height=int(self.height / 2))
		self.encompass_entry = Frame(self.encompass_frame, width=int(3 * self.width / 4), height=int(self.height / 2))

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_label, height=int(self.height))
		self.entry = ScrolledText(self.encompass_entry)

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)
		
		self.label.pack(fill=X)
		self.entry.pack(fill=X)
		self.encompass_frame.pack_propagate(0)
		self.encompass_label.pack_propagate(0)
		self.encompass_entry.pack_propagate(0)

		self.encompass_label.pack(side=LEFT)
		self.encompass_entry.pack(side=LEFT)
		self.encompass_frame.place(y=self.grid_row, x=self.grid_column)

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

		self.encompass_frame = Frame(kwargs['parent_obj'], width=self.width, height=self.height)
		self.encompass_label = Frame(self.encompass_frame, width=self.width, height=self.height)

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_label, height=int(self.height))

		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		self.label.bind('<Enter>', self.enter)
		self.label.bind('<Leave>', self.leave)

		self.label.pack(fill=X)
		self.encompass_frame.pack_propagate(0)
		self.encompass_label.pack_propagate(0)

		self.encompass_label.pack(side=LEFT)
		self.encompass_frame.place(y=self.grid_row, x=self.grid_column)


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

		self.encompass_frame = Frame(kwargs['parent_obj'], width=self.width, height=self.height)
		self.encompass_label = Frame(self.encompass_frame, width=int(self.width / 4), height=int(self.height / 2))
		self.encompass_entry = Frame(self.encompass_frame, width=int(3 * self.width / 4), height=int(self.height / 2))

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_label)
		self.entry = Entry(self.encompass_entry)

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
		
		self.label.pack(fill=X)
		self.entry.pack(fill=X)
		self.encompass_frame.pack_propagate(0)
		self.encompass_label.pack_propagate(0)
		self.encompass_entry.pack_propagate(0)

		self.encompass_label.pack(side=LEFT)
		self.encompass_entry.pack(side=LEFT)
		self.encompass_frame.place(y=self.grid_row, x=self.grid_column)

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
			self.entry.pack_forget()
			self.entry = Entry(self.encompass_entry)
			
			for attrib, value in self.entry_attributes.items():
				if value: self.entry.__setitem__(attrib, value)

			self.entry.place(anchor="c", relwidth=1.0, relx=.5, rely=.5)
			self.encompass_entry.pack_propagate(0)
			self.entry.insert(0, fill_entry)
			
			self.vcmd = (self.encompass_entry.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
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

		self.encompass_frame = Frame(kwargs['parent_obj'], width=self.width, height=self.height)
		self.encompass_label_entry = Frame(self.encompass_frame, width=self.width, height=int(self.height / 2))
		self.encompass_label = Frame(self.encompass_label_entry, width=int(self.width / 4), height=int(self.height / 2))
		self.encompass_entry = Frame(self.encompass_label_entry, width=int(3 * self.width / 4), height=int(self.height / 2))
		self.encompass_categores = Frame(self.encompass_frame, width=int(self.width), height=int(self.height / 2))

		self.grid_row = kwargs['grid_row']
		self.grid_column = kwargs['grid_column']

		self.label = Label(self.encompass_label, height=int(self.height / 2))
		self.entry = Entry(self.encompass_entry)
		self.label_categories = {}


		for attrib, value in self.label_attributes.items():
			if value: self.label.__setitem__(attrib, value)

		for attrib, value in self.entry_attributes.items():
			if value: self.entry.__setitem__(attrib, value)


		self.label.pack(fill=X)
		self.entry.place(anchor="c", relwidth=1.0, relx=.5, rely=.5)
		self.encompass_frame.pack_propagate(0)
		self.encompass_label.pack_propagate(0)
		self.encompass_label_entry.pack_propagate(0)
		self.encompass_categores.pack_propagate(0)
		self.encompass_entry.pack_propagate(0)

		column = 0
		for category in self.categories:
			for label, fill_tag in category.items():
				self.label_categories[fill_tag] = Label(self.encompass_categores, text=self.language[label])
				self.label_categories[fill_tag].grid(row=0, column=column)
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


		self.encompass_label.pack(side=LEFT)
		self.encompass_entry.pack(side=LEFT)
		self.encompass_label_entry.pack()
		self.encompass_categores.pack()
		self.encompass_frame.place(y=self.grid_row, x=self.grid_column)

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


class Cell_object:

	def __init__(self, canvas, p1x, p1y, p2x, p2y, grid_row, grid_column):
		self.row = grid_row
		self.column = grid_column
		self.canvas = canvas
		self.p1x = p1x
		self.p1y = p1y
		self.p2x = p2x
		self.p2y = p2y
		self.center = ((p1x + p2x) / 2, (p1y + p2y) / 2)
		self.left_line = self.canvas.create_line(self.p1x, self.p1y, self.p1x, self.p2y)
		self.right_line = self.canvas.create_line(self.p2x, self.p1y, self.p2x, self.p2y)
		self.top_line = self.canvas.create_line(self.p1x, self.p1y, self.p2x, self.p1y)
		self.bottom_line = self.canvas.create_line(self.p1x, self.p2y, self.p2x, self.p2y)
		self.object_id = self.canvas.create_rectangle(self.p1x, self.p1y, self.p2x, self.p2y, width=0)
		self.canvas.tag_raise(self.left_line)
		self.canvas.tag_raise(self.right_line)
		self.canvas.tag_raise(self.top_line)
		self.canvas.tag_raise(self.bottom_line)
		#self.tag = str(self.row) + ',' + str(self.column)
		#canvas.itemconfig(self.object_id, tags=(self.tag))

	def erase_line(self, line):
		if line == 'left':
			self.canvas.itemconfig(self.left_line, state=HIDDEN)
		elif line == 'right':
			self.canvas.itemconfig(self.right_line, state=HIDDEN)
		elif line == 'top':
			self.canvas.itemconfig(self.top_line, state=HIDDEN)
		elif line == 'bottom':
			self.canvas.itemconfig(self.bottom_line, state=HIDDEN)
		else:
			return

	def draw_line(self, line):
		if line == 'left':
			self.canvas.itemconfig(self.left_line, state=NORMAL)
		elif line == 'right':
			self.canvas.itemconfig(self.right_line, state=NORMAL)
		elif line == 'top':
			self.canvas.itemconfig(self.top_line, state=NORMAL)
		elif line == 'bottom':
			self.canvas.itemconfig(self.bottom_line, state=NORMAL)
		else:
			return

	def insert_text(self, text):
		self.text = self.canvas.create_text(self.center, text=text)

	def delete_cell(self):
		self.canvas.delete(self.left_line)
		self.canvas.delete(self.right_line)
		self.canvas.delete(self.top_line)
		self.canvas.delete(self.bottom_line)
		self.canvas.delete(self.object_id)

		if hasattr(self, 'text'):
			self.canvas.delete(self.text)

	pass


class Table:

	def __init__(self, parent, num_rows, num_columns):

		self.num_rows = num_rows
		self.num_columns = num_columns
		self.canvas = Canvas(parent, width=num_columns * 100 + 5, height=num_rows * 25 + 5)
		self.canvas.grid()
		self.cells = {}
		self.merged_cells = {}

		x, y, row, column = 5, 5, 0, 0
		while column < num_columns:
			while row < num_rows:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				y += 25
				
				row += 1
			
			x += 100
			y = 5	


			column += 1
			row = 0
	
	def erase_line(self, cell, line):

		def erase_single_line(line):

			if cell not in self.cells: return

			if line == 'left':
				cell_left = (cell[0] - 1, cell[1])
				if cell_left in self.cells:
					self.cells[cell_left].erase_line('right')
				self.cells[cell].erase_line('left')
			elif line == 'right':
				cell_right = (cell[0] + 1, cell[1])
				if cell_right in self.cells:
					self.cells[cell_right].erase_line('left')
				self.cells[cell].erase_line('right')
			elif line == 'top':
				cell_right = (cell[0], cell[1] - 1)
				if cell_right in self.cells:
					self.cells[cell_right].erase_line('bottom')
				self.cells[cell].erase_line('top')
			elif line == 'bottom':
				cell_right = (cell[0], cell[1] + 1)
				if cell_right in self.cells:
					self.cells[cell_right].erase_line('top')
				self.cells[cell].erase_line('bottom')
			else:
				return

		if type(line) == list:

			for single_line in line:
				erase_single_line(single_line)
		else:
			erase_single_line(line)

	def draw_line(self, cell, line):

		def draw_single_line(line):

			if cell not in self.cells: return

			if line == 'left':
				cell_left = (cell[0] - 1, cell[1])
				if cell_left in self.cells:
					self.cells[cell_left].draw_line('right')
				self.cells[cell].draw_line('left')
			elif line == 'right':
				cell_right = (cell[0] + 1, cell[1])
				if cell_right in self.cells:
					self.cells[cell_right].draw_line('left')
				self.cells[cell].draw_line('right')
			elif line == 'top':
				cell_right = (cell[0], cell[1] - 1)
				if cell_right in self.cells:
					self.cells[cell_right].draw_line('bottom')
				self.cells[cell].draw_line('top')
			elif line == 'bottom':
				cell_right = (cell[0], cell[1] + 1)
				if cell_right in self.cells:
					self.cells[cell_right].draw_line('top')
				self.cells[cell].draw_line('bottom')
			else:
				return

		if type(line) == list:

			for single_line in line:
				draw_single_line(single_line)
		else:
			draw_single_line(line)

	def add_row(self, after):

		if after != 0:

			x = 0

			while x < self.num_columns:
				if hasattr(self.cells[(x, after)], 'state') and self.cells[(x, after)].state == 'MERGED':
					return
				x += 1

		if after == 0:

			x, y, row, column = 5, self.cells[(0, after)].p1y, self.num_rows - 1, 0

			while row > after - 1:
				while column < self.num_columns:

					self.canvas.move(self.cells[(column, row)].object_id, 0, 25)
					self.canvas.move(self.cells[(column, row)].left_line, 0, 25)
					self.canvas.move(self.cells[(column, row)].right_line, 0, 25)
					self.canvas.move(self.cells[(column, row)].top_line, 0, 25)
					self.canvas.move(self.cells[(column, row)].bottom_line, 0, 25)

					if hasattr(self.cells[(column, row)], 'text'):
						self.canvas.move(self.cells[(column, row)].text, 0, 25)

					self.cells[(column, row + 1)] = self.cells[(column, row)]
					moved_cell = self.cells[(column, row + 1)]
					moved_cell.p1y = moved_cell.p1y + 25
					moved_cell.p2y = moved_cell.p2y + 25
					moved_cell.center = ((moved_cell.p1x + moved_cell.p2x) / 2, (moved_cell.p1y + moved_cell.p2y) / 2)

					column += 1

				column = 0
				row -= 1

			x, y, row, column = 5, self.cells[(0, 0)].p1y - 25, after, 0

			while column < self.num_columns:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				column += 1

				x += 100

		elif after >= self.num_rows:
			after = self.num_rows

			x, y, row, column = 5, self.cells[(0, self.num_rows - 1)].p2y, after, 0

			while column < self.num_columns:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				column += 1

				x += 100

		else:

			x, y, row, column = 5, self.cells[(0, after)].p2y, self.num_rows - 1, 0

			while row > after - 1:
				while column < self.num_columns:

					self.canvas.move(self.cells[(column, row)].object_id, 0, 25)
					self.canvas.move(self.cells[(column, row)].left_line, 0, 25)
					self.canvas.move(self.cells[(column, row)].right_line, 0, 25)
					self.canvas.move(self.cells[(column, row)].top_line, 0, 25)
					self.canvas.move(self.cells[(column, row)].bottom_line, 0, 25)

					if hasattr(self.cells[(column, row)], 'text'):
						self.canvas.move(self.cells[(column, row)].text, 0, 25)

					self.cells[(column, row + 1)] = self.cells[(column, row)]
					moved_cell = self.cells[(column, row + 1)]
					moved_cell.p1y = moved_cell.p1y + 25
					moved_cell.p2y = moved_cell.p2y + 25
					moved_cell.center = ((moved_cell.p1x + moved_cell.p2x) / 2, (moved_cell.p1y + moved_cell.p2y) / 2)

					column += 1

				column = 0
				row -= 1

			x, y, row, column = 5, self.cells[(0, after - 1)].p2y, after, 0

			while column < self.num_columns:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				column += 1

				x += 100
	
		self.num_rows += 1
	
		self.canvas.config(height=self.num_rows * 25 + 5)

	def add_column(self, after):

		if after != 0:

			y = 0

			while y < self.num_rows:
				if hasattr(self.cells[(after, y)], 'state') and self.cells[(after, y)].state == 'MERGED':
					return
				y += 1

		if after == 0:

			x, y, row, column = self.cells[(after, 0)].p1x, 5, 0, self.num_columns - 1

			while column > after - 1:
				while row < self.num_rows:

					self.canvas.move(self.cells[(column, row)].object_id, 100, 0)
					self.canvas.move(self.cells[(column, row)].left_line, 100, 0)
					self.canvas.move(self.cells[(column, row)].right_line, 100, 0)
					self.canvas.move(self.cells[(column, row)].top_line, 100, 0)
					self.canvas.move(self.cells[(column, row)].bottom_line, 100, 0)

					if hasattr(self.cells[(column, row)], 'text'):
						self.canvas.move(self.cells[(column, row)].text, 100, 0)

					self.cells[(column + 1, row)] = self.cells[(column, row)]
					moved_cell = self.cells[(column + 1, row)]
					moved_cell.p1x = moved_cell.p1x + 100
					moved_cell.p2x = moved_cell.p2x + 100
					moved_cell.center = ((moved_cell.p1x + moved_cell.p2x) / 2, (moved_cell.p1y + moved_cell.p2y) / 2)


					row += 1

				column -= 1
				row = 0

			x, y, row, column = self.cells[(after, 0)].p1x - 100, 5, 0, after

			while row < self.num_rows:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				row += 1

				y += 25

		elif after >= self.num_columns:
			after = self.num_columns

			x, y, row, column = self.cells[(self.num_columns - 1, 0)].p2x, 5, 0, after

			while row < self.num_rows:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				row += 1

				y += 25

		else:

			x, y, row, column = self.cells[(after, 0)].p2x, 5, 0, self.num_columns - 1

			while column > after - 1:
				while row < self.num_rows:

					self.canvas.move(self.cells[(column, row)].object_id, 100, 0)
					self.canvas.move(self.cells[(column, row)].left_line, 100, 0)
					self.canvas.move(self.cells[(column, row)].right_line, 100, 0)
					self.canvas.move(self.cells[(column, row)].top_line, 100, 0)
					self.canvas.move(self.cells[(column, row)].bottom_line, 100, 0)

					if hasattr(self.cells[(column, row)], 'text'):
						self.canvas.move(self.cells[(column, row)].text, 100, 0)

					self.cells[(column + 1, row)] = self.cells[(column, row)]
					moved_cell = self.cells[(column + 1, row)]
					moved_cell.p1x = moved_cell.p1x + 100
					moved_cell.p2x = moved_cell.p2x + 100
					moved_cell.center = ((moved_cell.p1x + moved_cell.p2x) / 2, (moved_cell.p1y + moved_cell.p2y) / 2)


					row += 1

				column -= 1
				row = 0

			x, y, row, column = self.cells[(after - 1, 0)].p2x, 5, 0, after

			while row < self.num_rows:
				self.cells[(column, row)] = Cell_object(self.canvas, x, y, x + 100, y + 25, row, column)

				row += 1

				y += 25
	
		self.num_columns += 1
	
		self.canvas.config(width=self.num_columns * 100 + 5)

	def color_row(self, row, color):

		row = row - 1

		for cell_coord, cell in self.cells.items():
			if hasattr(cell, 'state') and cell.state == 'MERGED':
				continue
			if cell_coord[1] == row:
				self.canvas.itemconfig(cell.object_id, fill=color)
		return

	def color_column(self, column, color):

		column = column - 1

		for cell_coord, cell in self.cells.items():
			if hasattr(cell, 'state') and cell.state == 'MERGED':
				continue
			if cell_coord[0] == column:
				self.canvas.itemconfig(cell.object_id, fill=color)
		return

	def merge_cells(self, from_cell, to_cell):

		x, y = from_cell[0], from_cell[1]

		while x <= to_cell[0]:
			while y <= to_cell[1]:
				if x != to_cell[0]:
					self.erase_line((x, y), 'right')

				if y != to_cell[1]:
					self.erase_line((x, y), 'bottom')

				if hasattr(self.cells[(x, y)], 'text'):
					self.canvas.delete(self.cells[(x, y)].text)

				self.cells[(x, y)].state = 'MERGED'
				self.canvas.itemconfig(self.cells[(x, y)].object_id, fill=self.canvas.itemcget(self.cells[from_cell].object_id, 'fill'))

				self.merged_cells[(x, y)] = from_cell

				y += 1

			x += 1
			y = from_cell[1]

		self.cells[from_cell].state = 'NORMAL'
		merged_cell = self.cells[from_cell]
		merged_cell.p2x, merged_cell.p2y = self.cells[to_cell].p2x, self.cells[to_cell].p2y
		merged_cell.center = ((merged_cell.p1x + merged_cell.p2x) / 2, (merged_cell.p1y + merged_cell.p2y) / 2)
		self.canvas.coords(merged_cell.object_id, merged_cell.p1x, merged_cell.p1y, merged_cell.p2x, merged_cell.p2y)

		return

	def restore_merged_cells(self, from_cell):

		delete_from_merged = []

		for cell_coord, cell in self.merged_cells.items():
			if cell == from_cell:
				self.draw_line(cell_coord, 'left')
				self.draw_line(cell_coord, 'top')

				self.cells[cell_coord].state = 'NORMAL'

				delete_from_merged.append(cell_coord)

		for cell_coord in delete_from_merged:
			del self.merged_cells[cell_coord]

		if hasattr(self.cells[from_cell], 'text'):
			self.canvas.delete(self.cells[from_cell].text)

		self.cells[from_cell].p2x = self.cells[from_cell].p1x + 100
		self.cells[from_cell].p2y = self.cells[from_cell].p1y + 25
		self.cells[from_cell].center = ((self.cells[from_cell].p1x + self.cells[from_cell].p2x) / 2, (self.cells[from_cell].p1y + self.cells[from_cell].p2y) / 2)
		self.canvas.coords(self.cells[from_cell].object_id, self.cells[from_cell].p1x, self.cells[from_cell].p1y, self.cells[from_cell].p2x, self.cells[from_cell].p2y)

		return

	def delete_row(self, table_row):

		column, row = 0, table_row - 1

		while column < self.num_columns:
			print(column, row)
			if (column, row) in self.merged_cells:
				self.restore_merged_cells(self.merged_cells[(column, row)])

			column += 1

		if table_row >= self.num_rows:
			table_row = self.num_rows - 1

			column, row = 0, table_row

			while column < self.num_columns:
				self.cells[(column, row)].delete_cell()

				column += 1
		
		else:

			column, row = 0, table_row - 1

			while column < self.num_columns:
				self.cells[(column, row)].delete_cell()
				del self.cells[(column, row)]

				column += 1

			column, row = 0, table_row

			
			while row < self.num_rows:
				while column < self.num_columns:
					self.cells[(column, row - 1)] = self.cells.pop((column, row), None)

					moved_cell = self.cells[(column, row - 1)]
					self.canvas.move(moved_cell.object_id, 0, -25)
					self.canvas.move(moved_cell.left_line, 0, -25)
					self.canvas.move(moved_cell.right_line, 0, -25)
					self.canvas.move(moved_cell.top_line, 0, -25)
					self.canvas.move(moved_cell.bottom_line, 0, -25)

					if hasattr(moved_cell, 'text'):
						self.canvas.move(moved_cell.text, 0, -25)

					moved_cell.p1y = moved_cell.p1y - 25
					moved_cell.p2y = moved_cell.p2y - 25
					moved_cell.center = ((moved_cell.p1x + moved_cell.p2x) / 2, (moved_cell.p1y + moved_cell.p2y) / 2)

					column += 1

				row += 1
				column = 0


		self.num_rows -= 1

		self.canvas.config(height=self.num_rows * 25 + 5)

		return

	def delete_column(self, table_column):

		column, row = table_column - 1, 0

		while row < self.num_rows:
			if (column, row) in self.merged_cells:
				self.restore_merged_cells(self.merged_cells[(column, row)])

			row += 1

		if table_column >= self.num_columns:
			table_column = self.num_columns - 1

			column, row = table_column, 0

			while row < self.num_rows:
				self.cells[(column, row)].delete_cell()

				row += 1
		
		else:

			column, row = table_column - 1, 0

			while row < self.num_rows:
				self.cells[(column, row)].delete_cell()
				del self.cells[(column, row)]

				row += 1

			column, row = table_column, 0

			
			while column < self.num_columns:
				while row < self.num_rows:
					self.cells[(column - 1, row)] = self.cells.pop((column, row), None)

					moved_cell = self.cells[(column - 1, row)]
					self.canvas.move(moved_cell.object_id, -100, 0)
					self.canvas.move(moved_cell.left_line, -100, 0)
					self.canvas.move(moved_cell.right_line, -100, 0)
					self.canvas.move(moved_cell.top_line, -100, 0)
					self.canvas.move(moved_cell.bottom_line, -100, 0)

					if hasattr(moved_cell, 'text'):
						self.canvas.move(moved_cell.text, -100, 0)

					moved_cell.p1x = moved_cell.p1x - 100
					moved_cell.p2x = moved_cell.p2x - 100
					moved_cell.center = ((moved_cell.p1x + moved_cell.p2x) / 2, (moved_cell.p1y + moved_cell.p2y) / 2)

					row += 1

				column += 1
				row = 0


		self.num_columns -= 1

		self.canvas.config(width=self.num_columns * 100 + 5)

		return

	pass
