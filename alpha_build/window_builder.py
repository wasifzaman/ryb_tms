from alpha_ui_separate_grid import *
from object_settings import *
from object_builder import *
from alpha_widgets import Table, Cell_object
from tkinter import Label
from PIL import Image, ImageTk
<<<<<<< HEAD
=======

>>>>>>> origin/master

'''
Notes:
	- de_select in select_widget method is a helper method to Cell_object




'''




class Window_builder:

	def __init__(self, window_width, window_height, grid_spacing):
		self.window = Window(window_width, window_height, grid_spacing)
		self.tools = Window(200, 100, 10, toplevel=True)
		self.object_builder_set = set()

		self.tools.toggle_grid()

		add_widget_selector = Button(text='Add', settings=button_scheme_1)
		toggle_grid = Button(text='Toggle Grid', settings=button_scheme_1)
		self.tools.add(add_widget_selector, 140, 40, 20, 20)
		self.tools.add(toggle_grid, 140, 40, 20, 61)
		add_widget_selector.label.bind('<Button-1>', self.select_widget)
		toggle_grid.label.bind('<Button-1>', lambda event: self.window.toggle_grid())


	def select_widget(self, event):

		widget_build_dictionary = {'Textbox': Object_builder('Textbox', ['label_text', 'fill_tag']),
								'Scrolled_textbox': Object_builder('Scrolled_textbox', ['label_text', 'fill_tag']),
								'Button': Object_builder('Button', ['text']),
								'Coin_widget': Object_builder('Coin_widget', ['label_text', 'fill_tag']),
								'Date_widget': Object_builder('Date_widget', ['label_text', 'fill_tag']),
								'Entry_category': Object_builder('Entry_category', ['label_text', 'fill_tag', 'categories'])}

		selector = Window(600, 200, 10, toplevel=True)
		widget_file = open('alpha_widgets.py', 'r')
		widget_list = []
		selector.current_widget = False
		selector.current_widget_value = False
		selector.objects_to_track = {}

		def de_select(self):
			self.canvas.itemconfig(self.object_id, fill='')

		Cell_object.de_select = de_select

		widget_table = Table(selector.window, 1, 1)
		widget_value_table = Table(selector.window, 1, 1)

		widget_value_table.canvas.place(x=240, y=60)

		for line in widget_file:
			widget = False
			if line[:5] == 'class':
				if line.find('(') != -1:
					widget = line[6:line.index('(')]
				else:
					widget = line[6:line.index(':')]
			if widget == 'Table' or widget == 'Cell_object': continue
			if widget:
				widget_list.append(widget)

		scrollbar = Scrollbar(selector.window, orient=VERTICAL)
		widget_table.canvas.config(yscrollcommand=scrollbar.set)
		scrollbar.config(command=widget_table.canvas.yview)
		scrollbar.place(x=180, y=0, height=200)

		value_of_property = Textbox(label_text='Value:', language={'Value:': 'Value:'}, fill_tag='value')
		selector.add(value_of_property, 180, 20, 420, 70)

		style_select = Listbox(selector.window)
		style_select.place(x=420, y=100, width=180, height=100)

		add_button = Button(text='Add', fill_tag='test', settings=button_scheme_1)
		close_button = Button(text='Close', fill_tag='test', settings=button_scheme_1)
		selector.add(add_button, 140, 40, 390, 10)
		selector.add(close_button, 140, 40, 245, 10)

		selector.grid.place_forget()

		row = 0
		while row < len(widget_list):
			widget_table.cells[(0, row)].insert_text(widget_list[row])
			row += 1
			if row != len(widget_list):
				widget_table.add_row(row)

		def set_value_table(widget):

			row = widget_value_table.num_rows
			while row > 1:
				widget_value_table.delete_row(row)
				row -= 1
				if row == 1:
					column = widget_value_table.num_columns
					while column > 1:
						cell = widget_value_table.cells[(column, row)]
						if hasattr(cell, 'text'):
							cell.canvas.delete(cell.text)
						column -= 1
					last_cell = widget_value_table.cells[(0, 0)]
					if hasattr(last_cell, 'text'):
						last_cell.canvas.delete(last_cell.text)

			widget_values = widget_build_dictionary[widget].properties
			row = 0
			while row < len(widget_values):
				widget_value_table.cells[(0, row)].insert_text(widget_values[row])
				row += 1
				if row != len(widget_values):
					widget_value_table.add_row(row)

			def OnValidate(d, i, P, s, S, v, V, W):
				
				setattr(selector.current_widget, selector.current_widget_value, P)
				return True

			def set_current_value(cell):
				if selector.current_widget_value in selector.objects_to_track:
					selector.objects_to_track[selector.current_widget_value].de_select()

				print(cell.canvas.itemcget(cell.text, 'text'))
				selector.current_widget_value = cell.canvas.itemcget(cell.text, 'text')

				if hasattr(selector.current_widget, selector.current_widget_value):
					value_of_property.set_data(getattr(selector.current_widget, selector.current_widget_value))
				else:
					value_of_property.set_data('')

				selector.objects_to_track[selector.current_widget_value] = cell
				cell.canvas.itemconfig(cell.object_id, fill='lightblue')
				return

			for cell in widget_value_table.cells.values():
				cell.bind('<Button-1>', set_current_value)

			value_of_property.vcmd = (value_of_property.encompass_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
			value_of_property.entry.config(validate="all", validatecommand=value_of_property.vcmd)

		def set_current_widget(cell):
			if selector.current_widget in selector.objects_to_track:
				selector.objects_to_track[selector.current_widget].de_select()
			selector.current_widget = widget_build_dictionary[cell.canvas.itemcget(cell.text, 'text')]
			set_value_table(cell.canvas.itemcget(cell.text, 'text'))

			selector.objects_to_track[selector.current_widget] = cell
			cell.canvas.itemconfig(cell.object_id, fill='pink')

		for cell_coord, cell in widget_table.cells.items():
			cell.bind('<Button-1>', set_current_widget)


		def add():

			width, height = int(selector.current_widget.width), int(selector.current_widget.height)	

			self.window.add(selector.current_widget.build(), width, height, 20, 20)

			selector.current_widget.make_resizable()
			selector.current_widget.make_movable()
			selector.current_widget.make_snappable(self.window.grid_spacing)
			selector.current_widget.make_removable(self)

			self.object_builder_set.add(selector.current_widget)

		add_button.label.bind('<Button-1>', lambda event: add())
		close_button.label.bind('<Button-1>', lambda event: selector.window.destroy())


test_window = Window_builder(426, 500, 10)
test_window.window.window.mainloop()