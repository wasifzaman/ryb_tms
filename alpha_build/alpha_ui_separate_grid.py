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
		self.grid_status = 'on'
		self.vertical_lines = {}
		self.horizontal_lines = {}

		self.window = Toplevel() if apply_attribute('toplevel') else Tk()
		self.window.geometry(str(width) + 'x' + str(height))
		self.grid = Canvas(self.window, width=width, height=height)
		self.grid.place(x=0, y=0)

		self.widget_set = set()

		x = 0
		while x < width:
			self.vertical_lines[x] = self.grid.create_line(x, 0, x, self.height)

			x += self.grid_spacing

		y = 0
		while y < height:
			self.horizontal_lines[y] = self.grid.create_line(0, y, self.width, y)

			y+= self.grid_spacing

		def create_and_modify_grid_lines(event):

			if self.width == self.window.winfo_width() and self.height == self.window.winfo_height():
				return

			for line in self.vertical_lines.values():
				cur_coords = self.grid.coords(line)
				cur_coords[3] = self.window.winfo_height()
				self.grid.coords(line, cur_coords[0], cur_coords[1], cur_coords[2], cur_coords[3])

			for line in self.horizontal_lines.values():
				cur_coords = self.grid.coords(line)
				cur_coords[2] = self.window.winfo_width()
				self.grid.coords(line, cur_coords[0], cur_coords[1], cur_coords[2], cur_coords[3])

			x = self.width

			while x < self.window.winfo_width():
				p1x = x - x % self.grid_spacing
				if p1x in self.vertical_lines:
					self.grid.delete(self.vertical_lines[p1x])
				self.vertical_lines[p1x] = self.grid.create_line(p1x, 0, p1x, self.height)

				x += self.grid_spacing

			y = self.height

			while y < self.window.winfo_height():
				p1y = y - y % self.grid_spacing
				if p1y in self.horizontal_lines:
					self.grid.delete(self.horizontal_lines[p1y])
				self.horizontal_lines[p1y] = self.grid.create_line(0, p1y, self.width, p1y)

				y += self.grid_spacing

			self.width, self.height = self.window.winfo_width(), self.window.winfo_height()

			self.grid.config(width=self.width, height=self.height)

		self.window.bind('<Configure>', create_and_modify_grid_lines)

	def add(self, item, width, height, column, row):

		item.width = width
		item.height = height

		item.create_widget(parent_obj=self.window, grid_row=row, grid_column=column)
		self.widget_set.add(item)

		return

	def remove(self, item):
		item.delete_widget()

		self.widget_set.remove(item)

		return		

	def toggle_grid(self):
		if self.grid_status == 'on':
			self.grid_status = 'off'
			self.grid.place_forget()
		elif self.grid_status == 'off':
			self.grid_status = 'on'
			self.grid.place(x=0, y=0)

	pass



def add_textbox(event, text, fill_tag, width, height):
	coords = window.grid.coords(event.widget.find_closest(event.x, event.y))
	x = int(coords[0] / (window.width / window.self.grid_spacing))
	y = int(coords[1] / (window.height / window.self.grid_spacing))
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