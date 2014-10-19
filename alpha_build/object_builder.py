from alpha_ui import *
from object_settings import *
from alpha_widgets import Table, Cell_object






class Object_builder:

	def __init__(self, object_type, properties):
		self.object_type = object_type
		self.properties = properties
		self.properties.extend(['width', 'height'])
		self.need_to_convert_to_str = [list, int]

	def build(self):
		return eval(self.string_output())

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

	def move(self):

		return

	def resize(self):

		return

	pass




def select_widget(event):

	widget_build_dictionary = {'Textbox': Object_builder('Textbox', ['label_text', 'fill_tag']),
							'Scrolled_textbox': Object_builder('Scrolled_textbox', ['label_text', 'fill_tag']),
							'Button': Object_builder('Button', ['text']),
							'Coin_widget': Object_builder('Coin_widget', ['label_text', 'fill_tag']),
							'Date_widget': Object_builder('Date_widget', ['label_text', 'fill_tag']),
							'Entry_category': Object_builder('Entry_category', ['label_text', 'fill_tag', 'categories'])}

	coords = window.grid.coords(event.widget.find_closest(event.x, event.y))
	x = int(coords[0] / (window.width / window.grid_spacing))
	y = int(coords[1] / (window.height / window.grid_spacing))

	selector = Window(600, 200, 10, toplevel=True)
	widget_file = open('alpha_widgets.py', 'r')
	widget_list = []
	selector.current_widget = ''
	selector.current_widget_value = ''

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
	selector.add(value_of_property, 4, 2, 6, 3)

	style_select = Listbox(selector.window)
	style_select.place(x=420, y=100, width=180, height=100)

	add_button = Button(text='Add', fill_tag='test', settings=button_scheme_1)
	close_button = Button(text='Close', fill_tag='test', settings=button_scheme_1)
	selector.add(add_button, 3, 2, 4, 0)
	selector.add(close_button, 3, 2, 7, 0)

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
			print(cell.canvas.itemcget(cell.text, 'text'))
			selector.current_widget_value = cell.canvas.itemcget(cell.text, 'text')

			if hasattr(selector.current_widget, selector.current_widget_value):
				value_of_property.set_data(getattr(selector.current_widget, selector.current_widget_value))
			else:
				value_of_property.set_data('')
			return

		for cell in widget_value_table.cells.values():
			cell.bind('<Button-1>', set_current_value)

		value_of_property.vcmd = (value_of_property.encompass_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		value_of_property.entry.config(validate="all", validatecommand=value_of_property.vcmd)

	def set_current_widget(cell):
		selector.current_widget = widget_build_dictionary[cell.canvas.itemcget(cell.text, 'text')]
		set_value_table(cell.canvas.itemcget(cell.text, 'text'))

	for cell_coord, cell in widget_table.cells.items():
		cell.bind('<Button-1>', set_current_widget)


	def add():

		width, height = int(selector.current_widget.width), int(selector.current_widget.height)	

		window.add(selector.current_widget.build(), width, height, x, y)


	add_button.label.bind('<Button-1>', lambda event: add())
	close_button.label.bind('<Button-1>', lambda event: selector.window.destroy())


window = Window(500, 500, 10)

for grid_coords, rectangle in window.grid_rectangles.items():
	window.grid.itemconfig(rectangle, fill='lightblue')
	window.grid.tag_bind(rectangle, '<Button-1>', select_widget)



textbox = Object_builder('Date_widget', ['label_text', 'fill_tag', 'categories'])
textbox.label_text = 'abcd'
#window.add(textbox.build(), 5, 2, 0, 0)




window.window.mainloop()