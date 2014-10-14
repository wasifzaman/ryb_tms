from tkinter import *
from alpha_widgets import *
from object_settings import *
import languages

'''

Notes:
	-


'''


class Window:

	def __init__(self, width, height, grid_spacing, **kwargs):
		def apply_attribute(attrib):
			return kwargs[attrib] if attrib in kwargs else False

		self.width = width
		self.height = height
		self.grid_spacing = grid_spacing
		self.grid_occupied = {}
		self.grid_rectangles = {}

		self.window = Toplevel() if apply_attribute('toplevel') else Tk()
		self.window.geometry(str(width) + 'x' + str(height))
		self.grid = Canvas(self.window, width=width, height=height)
		self.grid.place(x=0, y=0)

		x, y = 0, 0
		while x < width:
			while y < height:
				self.grid_rectangles[(int(x / (width / grid_spacing)), int(y / (height / grid_spacing)))] = self.grid.create_rectangle(x, y, x + width / self.grid_spacing, y + height / self.grid_spacing)
				self.grid.create_text(x + width / self.grid_spacing / 2, y + height / self.grid_spacing / 2, text='(' + str(int(x / (width / grid_spacing))) + ',' + str(int(y / (height / grid_spacing))) + ')')

				y += height / self.grid_spacing

			x += width / self.grid_spacing
			y = 0

	def add(self, item, width, height, column, row):

		x, y = column, row

		while y < row + height:
			while x < column + width:
				if (x, y) in self.grid_occupied:
					return

				x += 1

			y += 1
			x = column

		item.width = width * self.width / self.grid_spacing
		item.height = height * self.height / self.grid_spacing

		x, y = column * self.width / self.grid_spacing, row * self.height / self.grid_spacing
		item.create_widget(parent_obj=self.window, grid_row=y, grid_column=x)

		x, y = column, row

		while row < y + height:
			while column < x + width:
				self.grid_occupied[(column, row)] = True

				column += 1

			row += 1
			column = 0

		return

	pass


window = Window(500, 500, 10)

def select_widget(event):

	coords = window.grid.coords(event.widget.find_closest(event.x, event.y))
	x = int(coords[0] / (window.width / window.grid_spacing))
	y = int(coords[1] / (window.height / window.grid_spacing))

	selector = Window(600, 200, 10, toplevel=True)
	widget_file = open('alpha_widgets.py', 'r')
	widget_list = {}
	for line in widget_file:
		if line[:5] == 'class':
			widget_list[line[6:line.index(':')]] = True
	scrollbar = Scrollbar(selector.window, orient=VERTICAL)
	widget_list_widget = Listbox(selector.window, yscrollcommand=scrollbar.set)
	widget_list_widget.place(x=0, y=0, width=180, height=200)
	scrollbar.config(command=widget_list_widget.yview)
	scrollbar.place(x=180, y=0, height=200)


	def set_value(event):

		selector.widget_value_list = {}
		selector.widget_value_list_widget = Listbox(selector.window)
		selector.widget_value_list_widget.place(x=240, y=60, width=120, height=140)

		selector.value = Textbox(label_text='Value:', language={'Value:': 'Value:'}, fill_tag='value')
		selector.add(selector.value, 4, 2, 6, 3)

		def OnValidate(d, i, P, s, S, v, V, W):
			selector.widget_value_list[selector.widget_value_list_widget.get(ACTIVE)] = selector.value.get_data()
			return True

		selector.value.vcmd = (selector.value.encompass_frame.register(OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		selector.value.entry.config(validate="all", validatecommand=selector.value.vcmd)

		for attr in widget_build_dictionary[widget_list_widget.get(ACTIVE)]:
			selector.widget_value_list_widget.insert(END, attr)

		selector.widget_value_list_widget.bind('<Button-1>', lambda event: selector.value.set_data(''))

		return

	widget_list_widget.bind('<Button-1>', set_value)

	add_button = Button(text='Add', language={'Add': 'Add'}, fill_tag='test', settings=button_scheme_1)
	selector.add(add_button, 3, 2, 5, 0)

	widget_build_dictionary = {'Textbox': {'label_text': False, 'language': False, 'fill_tag':False, 'width': False, 'height': False, \
								'build': lambda self:Textbox(label_text=self['label_text'], language=self['language'], fill_tag=self['fill_tag'])},
								'Scrolled_textbox': {'label_text': False, 'language': False, 'fill_tag': False, 'width': False, 'height': False, \
								'build': lambda self:Scrolled_textbox(label_text=self['label_text'], language=self['language'], fill_tag=self['fill_tag'])},
								'Button': {'label_text': False, 'language': False, 'width': False, 'height': False, \
								'build': lambda self:Button(text=self['label_text'], language=self['language'])},
								'Coin_widget': {'label_text': False, 'language': False, 'fill_tag':False, 'width': False, 'height': False, \
								'build': lambda self: Coin_widget(label_text=self['label_text'], language=self['language'], fill_tag=self['fill_tag'])},
								'Date_widget': {'label_text': False, 'language': False, 'fill_tag':False, 'width': False, 'height': False, \
								'build': lambda self: Date_widget(label_text=self['label_text'], language=self['language'], fill_tag=self['fill_tag'])},
								'Entry_category': {'label_text': False, 'language': False, 'fill_tag':False, 'width': False, 'height': False, \
								'build': lambda self: Entry_category(label_text=self['label_text'], language=self['language'], fill_tag=self['fill_tag'])}}

	#selector.grid.place_forget()

	for widget in widget_list:
		if widget == 'Cell_object' or widget == 'Table': continue
		widget_list_widget.insert(END, widget)

	def add():

		widget = dict(widget_build_dictionary[widget_list_widget.get(ACTIVE)])

		for attr, value in selector.widget_value_list.items():
			if attr == 'build': continue
			widget[attr] = value

		print(selector.widget_value_list)

		widget['language'] = {'abcd': 'abcd'}
		width, height = int(widget['width']), int(widget['height'])	



		window.add(widget['build'](widget), width, height, x, y)


	add_button.label.bind('<Button-1>', lambda event: add())


def add_textbox(event, text, fill_tag, width, height):
	coords = window.grid.coords(event.widget.find_closest(event.x, event.y))
	x = int(coords[0] / (window.width / window.grid_spacing))
	y = int(coords[1] / (window.height / window.grid_spacing))
	window.add(Textbox(label_text=text, language=languages.languages['english'], fill_tag=fill_tag), width, height, x, y)



for grid_coords, rectangle in window.grid_rectangles.items():
	window.grid.itemconfig(rectangle, fill='lightblue')
	window.grid.tag_bind(rectangle, '<Button-1>', select_widget)






#window.add(Textbox(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 4, 0, 0)
#window.add(Scrolled_textbox(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 2, 0, 2)
#window.add(Button(text='First Name', language=languages.languages['english'], fill_tag='test', settings=button_scheme_1), 5, 1, 0, 2)
#window.add(Coin_widget(label_text='First Name', language=languages.languages['english'], whole_text=10, cent_text=5, settings=coin_scheme_1, fill_tag='test'), 5, 1, 0, 2)
#window.add(Date_widget(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 2, 0, 0)
#window.add(Entry_category(label_text='Search', language=languages.languages['english'], categories=[{'First Name': 'First Name'}, {'Last Name': 'Last Name'}, {'Chinese Name': 'Chinese Name'}], settings=entry_category_scheme_1), 7, 3, 0, 0)


window.window.mainloop()