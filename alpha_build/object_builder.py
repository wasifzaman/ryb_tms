from alpha_ui import *
from object_settings import *






class Object_builder:

	def __init__(self, object_type, properties):
		self.object_type = object_type
		self.properties = properties
		self.properties.update({'width': False, 'height': False})
		self.need_to_convert_to_str = [list, int]

	def build(self):
		return eval(self.string_output())

	def string_output(self):
		output = self.object_type + '('
		for attr, value in self.properties.items():
			output += attr + '='
			try:
				if type(eval(value)) in self.need_to_convert_to_str:
					output += str(value)
			except (TypeError, NameError) as error:
				output += repr(value)
			output += ', '

		return output[:-2] + ')'

	def move(self):

		return

	def resize(self):

		return

	pass


widget_build_dictionary = {'Textbox': Object_builder('Textbox', {'label_text': False, 'fill_tag': False}),
							'Scrolled_textbox': Object_builder('Scrolled_textbox', {'label_text': False, 'fill_tag': False}),
							'Button': Object_builder('Button', {'text': False}),
							'Coin_widget': Object_builder('Coin_widget', {'label_text': False, 'fill_tag':False}),
							'Date_widget': Object_builder('Date_widget', {'label_text': False, 'fill_tag':False}),
							'Entry_category': Object_builder('Entry_category', {'label_text': False, 'fill_tag':False, 'categories': False})}


def select_widget(event):

	coords = window.grid.coords(event.widget.find_closest(event.x, event.y))
	x = int(coords[0] / (window.width / window.grid_spacing))
	y = int(coords[1] / (window.height / window.grid_spacing))

	selector = Window(600, 200, 10, toplevel=True)
	widget_file = open('alpha_widgets.py', 'r')
	widget_list = []
	widget_map = {}
	widget_index = 0
	for line in widget_file:
		widget = False
		if line[:5] == 'class':
			if line.find('(') != -1:
				widget = line[6:line.index('(')]
			else:
				widget = line[6:line.index(':')]
		if widget:
			widget_map[widget_index] = widget
			widget_list.append(widget)
			widget_index += 1
	scrollbar = Scrollbar(selector.window, orient=VERTICAL)
	widget_list_widget = Listbox(selector.window, yscrollcommand=scrollbar.set)
	widget_list_widget.place(x=0, y=0, width=180, height=200)
	scrollbar.config(command=widget_list_widget.yview)
	scrollbar.place(x=180, y=0, height=200)

	value_of_property = Textbox(label_text='Value:', language={'Value:': 'Value:'}, fill_tag='value')
	selector.add(value_of_property, 4, 2, 6, 3)

	widget_value_list_widget = Listbox(selector.window)
	widget_value_list_widget.place(x=240, y=60, width=120, height=140)

	style_select = Listbox(selector.window)
	style_select.place(x=420, y=100, width=180, height=100)


	def set_value(event):

		widget_value_list_widget.delete(0, END)

		def OnValidate(d, i, P, s, S, v, V, W):
			#setattr(current_active, widget_value_list_widget.get(ACTIVE), P)
			widget_value_list[widget_value_list_widget.get(ACTIVE)] = P
			return True

		value_of_property.vcmd = (value_of_property.encompass_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		value_of_property.entry.config(validate="all", validatecommand=value_of_property.vcmd)

		current_active = widget_build_dictionary[widget_map[widget_list_widget.curselection()[0]]]
		print(setattr(current_active, 'abcd', 5))
		for attr in widget_build_dictionary[widget_map[widget_list_widget.curselection()[0]]].properties:
			widget_value_list[attr] = False
			widget_value_list_widget.insert(END, attr)

		return

	widget_value_list = {}

	widget_list_widget.bind('<<ListboxSelect>>', set_value)
	#widget_value_list_widget.bind('<Button-1>', lambda event: selector.value.set_data(''))

	add_button = Button(text='Add', fill_tag='test', settings=button_scheme_1)
	close_button = Button(text='Close', fill_tag='test', settings=button_scheme_1)
	selector.add(add_button, 3, 2, 4, 0)
	selector.add(close_button, 3, 2, 7, 0)

	selector.grid.place_forget()

	for widget in widget_list:
		if widget == 'Cell_object' or widget == 'Table': continue
		widget_list_widget.insert(END, widget)

	def add():

		widget = widget_build_dictionary[widget_list_widget.get(ACTIVE)]

		for attr, value in widget_value_list.items():
			if attr == 'build': continue
			widget.properties[attr] = value

		print(widget_value_list)

		width, height = int(widget.properties['width']), int(widget.properties['height'])	

		window.add(widget.build(), width, height, x, y)


	add_button.label.bind('<Button-1>', lambda event: add())
	close_button.label.bind('<Button-1>', lambda event: selector.window.destroy())


window = Window(500, 500, 10)

for grid_coords, rectangle in window.grid_rectangles.items():
	window.grid.itemconfig(rectangle, fill='lightblue')
	window.grid.tag_bind(rectangle, '<Button-1>', select_widget)



textbox = Object_builder('Date_widget', {'label_text': False, 'fill_tag': False, 'categories': "[{'abcd': 'abcd'}]"})
textbox.properties['label_text'] = 'abcd'
window.add(textbox.build(), 5, 2, 0, 0)

print(int(str('2')))


window.window.mainloop()