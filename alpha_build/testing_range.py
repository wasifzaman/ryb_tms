import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)


def show_top():
	top = Window(top=True)
	top.attributes('-fullscreen', False)
	top.geometry('300x300+100+100')

	top.grab_set()
	top.focus_set()
	top.overrideredirect(True)

	top.main_top_window = AppWindow(top.main_frame, num_rows=3, num_columns=3)
	top.main_top_window.language = languages.languages['english']

	button_kill_window = Button(text='Exit', language=top.main_top_window.language)

	top.main_top_window.menu_frame = top.main_top_window.newFrame("Menu Frame", (3, 1), column=0)
	top.main_top_window.menu_frame.addWidget(button_kill_window, column=0)

	button_kill_window.config(command=top.destroy)

def test_listbox():

	window = Tk()

	frame = Frame(window)



	listbox1 = Listbox(frame, activestyle=NONE, exportselection=0)
	listbox2 = Listbox(frame, activestyle=NONE, exportselection=0)

	listbox1.insert(END, "a list entry")
	listbox1.insert(END, "second list entry")
	listbox2.insert(END, "another entry")
	listbox2.insert(END, "another entry")


	listbox1.grid(row=0, column=0)
	listbox2.grid(row=0, column=1)

	frame.grid()


	def select_corresponding(event):
		print(listbox1.nearest(event.y))
		listbox2.selection_clear(0, 10)
		listbox2.selection_set(listbox1.nearest(event.y))
		return


	listbox1.bind('<ButtonRelease-1>', select_corresponding)





	listbox1.selection_set(0)
	listbox2.selection_set(listbox1.index(ACTIVE))

	window.mainloop()

print(float('5.'))

from tkinter import *

window = Tk()

frame = Frame(window)

canvas = Canvas(frame, width=700, height=300)

rect_1 = canvas.create_rectangle(50, 25, 150, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)
canvas.create_rectangle(150, 25, 250, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)
canvas.create_rectangle(250, 25, 350, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)

canvas.create_line(150, 25, 150, 75, width=1)
canvas.create_line(250, 25, 250, 75, width=1)
canvas.create_line(50, 25, 150, 25)
canvas.create_line(50, 75, 150, 75)
canvas.create_line(150, 75, 250, 75)
canvas.create_line(50, 25, 50, 75)

canvas.create_text(100, 50, text='text', tag='rect_0_text')

canvas.move(rect_1, 50, 50)

def select_row(event):
	for rect in canvas.find_withtag('rect_0'):
		canvas.itemconfig(rect, fill='lightblue')
	return

canvas.addtag_all('all_items')

for rect in canvas.find_withtag('all_items'):
	if 'rect_0' in canvas.gettags(rect):
		canvas.itemconfig(rect, fill='red')


canvas.tag_bind('rect_0', '<Button-1>', select_row)
canvas.tag_bind('rect_0_text', '<Button-1>', select_row)


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

	pass

frame.grid()
'''
	cell = Cell_object(canvas, 350, 25, 450, 75, 0, 0)
	canvas.create_text(cell.center, text='text', tag='rect_0_text')

	#canvas.create_line(cell.left_line)
	#canvas.create_line(cell.top_line)
	#canvas.create_line(cell.bottom_line)
	#canvas.create_line(cell.right_line)

	canvas.itemconfig(cell.object_id, fill='lightgreen')

	string = "0;50,25;150,75"

	print(string.split(';'))

	

	canvas.grid()
'''

class Table:

	def __init__(self, parent, num_rows, num_columns):

		self.num_rows = num_rows
		self.num_columns = num_columns
		self.canvas = Canvas(parent, width=num_columns * 100 + 5, height=num_rows * 25 + 5)
		self.canvas.grid()
		self.cells = {}

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

		if after >= self.num_rows:
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

					self.cells[(column, row + 1)] = self.cells[(column, row)]
					moved_cell = self.cells[(column, row + 1)]
					moved_cell.p1y = moved_cell.p1y + 25
					moved_cell.p2y = moved_cell.p2y + 25

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

		if after >= self.num_columns:
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

					self.cells[(column + 1, row)] = self.cells[(column, row)]
					moved_cell = self.cells[(column + 1, row)]
					moved_cell.p1x = moved_cell.p1x + 100
					moved_cell.p2x = moved_cell.p2x + 100

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
			



	pass


table = Table(frame, 5, 5)

#table.erase_line((0, 2), 'left')
#table.draw_line((0, 0), 'left')
#table.add_row(2)
#table.add_column(2)

window.mainloop()

