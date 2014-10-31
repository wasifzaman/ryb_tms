from alpha_ui_separate_grid import *
from object_settings import *
from alpha_widgets import Table, Cell_object
from tkinter import Label
from PIL import Image, ImageTk






class Object_builder:

	def __init__(self, object_type, properties):
		self.object_type = object_type
		self.properties = properties
		self.properties.extend(['width', 'height'])
		self.need_to_convert_to_str = [list, int]

	def build(self):
		self.widget = eval(self.string_output())
		return self.widget

	def string_output(self):
		output = self.object_type + '('
		for attr in self.properties:
			output += attr + '='
			if not hasattr(self, attr):
				output += repr(False)
			else:
				try:
					if type(eval(getattr(self, attr))) in self.need_to_convert_to_str:
						output += str(getattr(self, attr))
				except (TypeError, NameError) as error:
					output += repr(getattr(self, attr))
			output += ', '

		return output[:-2] + ')'

	def make_movable(self):

		def onclick(event):
			self.drag_x = event.x
			self.drag_y = event.y

		def onmotion(event):
			delta_x = event.x - self.drag_x
			delta_y = event.y - self.drag_y

			self.widget.grid_row = self.widget.grid_row + delta_y
			self.widget.grid_column = self.widget.grid_column + delta_x

			self.widget.encompass_frame.place(x=self.widget.grid_column, y=self.widget.grid_row)

		self.move_drag_point = Label(self.widget.encompass_frame, text=' ', cursor='fleur')
		self.move_drag_point.place(x=1, y=1)

		self.move_drag_point.bind('<ButtonPress-1>', onclick)
		self.move_drag_point.bind('<B1-Motion>', onmotion)

	def make_resizable(self):

		def onclick(event):
			self.drag_x = event.x
			self.drag_y = event.y

		def onmotion(event, corner_id):
			delta_x = event.x - self.drag_x
			delta_y = event.y - self.drag_y
			
			if corner_id == 'bottom_left':
				self.widget.width = self.widget.width + (delta_x * -1)
				self.widget.height = self.widget.height + delta_y
				self.widget.grid_column = self.widget.grid_column + delta_x
				self.widget.encompass_frame.place(x=self.widget.grid_column)
			elif corner_id == 'top_right':
				self.widget.width = self.widget.width + delta_x
				self.widget.height = self.widget.height + (delta_y * -1)
				self.widget.grid_row = self.widget.grid_row + delta_y
				self.widget.encompass_frame.place(y=self.widget.grid_row)
			elif corner_id == 'bottom_right':
				self.widget.width = (self.widget.width + delta_x) 
				self.widget.height = (self.widget.height + delta_y) 

			self.widget.encompass_frame.config(width=self.widget.width, height=self.widget.height)

			self.resize_point_bottom_right.place(x=self.widget.width - 10, y=self.widget.height - 15)
			self.resize_point_bottom_left.place(x=-3, y=self.widget.height - 15)
			self.resize_point_top_right.place(x=self.widget.width - 10, y=-7)		

		self.resize_point_bottom_right = Label(self.widget.encompass_frame, text=' ', cursor='bottom_right_corner')
		self.resize_point_bottom_left = Label(self.widget.encompass_frame, text=' ', cursor='bottom_left_corner')
		self.resize_point_top_right = Label(self.widget.encompass_frame, text=' ', cursor='top_right_corner')
		self.resize_point_bottom_right.place(x=self.widget.width - 10, y=self.widget.height - 15)
		self.resize_point_bottom_left.place(x=-3, y=self.widget.height - 15)
		self.resize_point_top_right.place(x=self.widget.width - 10, y=-7)

		self.resize_point_bottom_right.bind('<ButtonPress-1>', onclick)
		self.resize_point_bottom_right.bind('<B1-Motion>', lambda event: onmotion(event, 'bottom_right'))
		self.resize_point_bottom_left.bind('<ButtonPress-1>', onclick)
		self.resize_point_bottom_left.bind('<B1-Motion>', lambda event: onmotion(event, 'bottom_left'))
		self.resize_point_top_right.bind('<ButtonPress-1>', onclick)
		self.resize_point_top_right.bind('<B1-Motion>', lambda event: onmotion(event, 'top_right'))


		return

	def make_snappable(self, grid_spacing):

		def onrelease(event, corner_id):

			if corner_id == 'bottom_left':
				self.widget.width = self.widget.width // grid_spacing * grid_spacing + grid_spacing
				self.widget.height = self.widget.height // grid_spacing * grid_spacing + grid_spacing
				self.widget.grid_column = self.widget.grid_column // grid_spacing * grid_spacing
				self.widget.encompass_frame.place(x=self.widget.grid_column)
			elif corner_id == 'top_right':
				self.widget.width = self.widget.width // grid_spacing * grid_spacing + grid_spacing
				self.widget.height = self.widget.height // grid_spacing * grid_spacing + grid_spacing
				self.widget.grid_row = self.widget.grid_row // grid_spacing * grid_spacing + grid_spacing
				self.widget.encompass_frame.place(y=self.widget.grid_row)
			elif corner_id == 'bottom_right':
				self.widget.width = self.widget.width // grid_spacing * grid_spacing
				self.widget.height = self.widget.height // grid_spacing * grid_spacing

			self.widget.encompass_frame.config(width=self.widget.width, height=self.widget.height)

			self.resize_point_bottom_right.place(x=self.widget.width - 10, y=self.widget.height - 15)
			self.resize_point_bottom_left.place(x=-3, y=self.widget.height - 15)
			self.resize_point_top_right.place(x=self.widget.width - 10, y=-7)
			

			return

		def drag_onrelease(event):

			self.widget.grid_row = self.widget.grid_row // grid_spacing * grid_spacing
			self.widget.grid_column = self.widget.grid_column // grid_spacing * grid_spacing

			self.widget.encompass_frame.place(x=self.widget.grid_column, y=self.widget.grid_row)

			self.move_drag_point.place(x=1, y=1)

		if grid_spacing:
			self.resize_point_bottom_right.bind('<ButtonRelease-1>', lambda event: onrelease(event, 'bottom_right'))
			self.resize_point_bottom_left.bind('<ButtonRelease-1>', lambda event: onrelease(event, 'bottom_left'))
			self.resize_point_top_right.bind('<ButtonRelease-1>', lambda event: onrelease(event, 'top_right'))

			self.move_drag_point.bind('<ButtonRelease-1>', drag_onrelease)

		else:
			return

		return

	def make_removable(self, window_builder):

		def remove(event):
			window_builder.window.remove(self.widget)
			window_builder.object_builder_set.remove(self)

		self.delete_point = Label(self.widget.encompass_frame, text='×', font=('Helvetica',20))
		self.delete_point.place(relx=0.5, y=3)

		self.delete_point.bind('<Button-1>', remove)

		print(window_builder.object_builder_set)

		return

	pass



'''
def select_widget(event, grid_spacing):

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

		window.add(selector.current_widget.build(), width, height, 20, 20)

		selector.current_widget.make_resizable()
		selector.current_widget.make_movable()
		selector.current_widget.make_snappable(grid_spacing)
		selector.current_widget.make_removable(window)

		object_builder_set.add(selector.current_widget)


	add_button.label.bind('<Button-1>', lambda event: add())
	close_button.label.bind('<Button-1>', lambda event: selector.window.destroy())



window = Window(426, 500, 10)
tools = Window(200, 100, 10, toplevel=True)
object_builder_set = set()

tools.toggle_grid()

add_widget_selector = Button(text='Add', settings=button_scheme_1)
toggle_grid = Button(text='Toggle Grid', settings=button_scheme_1)
tools.add(add_widget_selector, 140, 40, 20, 20)
tools.add(toggle_grid, 140, 40, 20, 61)
add_widget_selector.label.bind('<Button-1>', lambda event: select_widget(event, window.grid_spacing))
toggle_grid.label.bind('<Button-1>', lambda event: window.toggle_grid())


textbox = Object_builder('Date_widget', ['label_text', 'fill_tag', 'categories'])
textbox.label_text = 'abcd'
window.add(textbox.build(), 300, 245, 0, 0)

textbox.make_movable()
textbox.make_resizable()
textbox.make_snappable(window.grid_spacing)
textbox.make_removable(window)


def onclick(event):
	textbox.drag_x = event.x
	textbox.drag_y = event.y

def callback(event):
	delta_x = event.x - textbox.drag_x
	delta_y = event.y - textbox.drag_y
	textbox.widget.grid_row = textbox.widget.grid_row + delta_y
	textbox.widget.grid_column = textbox.widget.grid_column + delta_x
	textbox.widget.encompass_frame.place(y=textbox.widget.grid_row, x=textbox.widget.grid_column)
	return


#window.window.mainloop()'''