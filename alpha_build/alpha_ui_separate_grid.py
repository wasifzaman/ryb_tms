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

		'''
		x, y = column, row

		while y < row + height:
			while x < column + width:
				if (x, y) in self.grid_occupied:
					return

				x += 1

			y += 1
			x = column
		'''

		#item.width = width * self.width / self.grid_spacing
		#item.height = height * self.height / self.grid_spacing

		item.width = width
		item.height = height

		#x, y = column * self.width / self.grid_spacing, row * self.height / self.grid_spacing
		#item.create_widget(parent_obj=self.window, grid_row=y, grid_column=x)

		item.create_widget(parent_obj=self.window, grid_row=row, grid_column=column)

		'''
		x, y = column, row

		while row < y + height:
			while column < x + width:
				self.grid_occupied[(column, row)] = True

				column += 1

			row += 1
			column = 0
		'''

		return

	pass



def add_textbox(event, text, fill_tag, width, height):
	coords = window.grid.coords(event.widget.find_closest(event.x, event.y))
	x = int(coords[0] / (window.width / window.grid_spacing))
	y = int(coords[1] / (window.height / window.grid_spacing))
	window.add(Textbox(label_text=text, language=languages.languages['english'], fill_tag=fill_tag), width, height, x, y)





#window = Window(500, 500, 10)


#window.add(Textbox(label_text='First Name'), 200, 300, 0, 0)


#window.add(Textbox(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 4, 0, 0)
#window.add(Scrolled_textbox(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 2, 0, 2)
#window.add(Button(text='First Name', language=languages.languages['english'], fill_tag='test', settings=button_scheme_1), 5, 1, 0, 2)
#window.add(Coin_widget(label_text='First Name', language=languages.languages['english'], whole_text=10, cent_text=5, settings=coin_scheme_1, fill_tag='test'), 5, 1, 0, 2)
#window.add(Date_widget(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 2, 0, 0)
#window.add(Entry_category(label_text='Search', language=languages.languages['english'], categories=[{'First Name': 'First Name'}, {'Last Name': 'Last Name'}, {'Chinese Name': 'Chinese Name'}], settings=entry_category_scheme_1), 7, 3, 0, 0)

#window.window.mainloop()