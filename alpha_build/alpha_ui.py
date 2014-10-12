from tkinter import *
from alpha_widgets import *
import languages

class Window:

	def __init__(self, width, height, grid_spacing):

		self.width = width
		self.height = height
		self.grid_spacing = grid_spacing
		self.grid_occupied = {}

		self.window = Tk()
		self.window.geometry(str(width) + 'x' + str(height))
		self.grid = Canvas(self.window, width=width, height=height)
		self.grid.place(x=0, y=0)

		x, y = 0, 0
		while x < width:
			while y < height:
				self.grid.create_rectangle(x, y, x + width / self.grid_spacing, y + height / self.grid_spacing)
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


#window.add(Textbox(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 2, 0, 0)
#window.add(Textbox(label_text='First Name', language=languages.languages['english'], fill_tag='test'), 5, 2, 0, 2)




window.window.mainloop()