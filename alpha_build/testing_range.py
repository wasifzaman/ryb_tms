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

canvas.create_rectangle(50, 25, 150, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)
canvas.create_rectangle(150, 25, 250, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)
canvas.create_rectangle(250, 25, 350, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)

canvas.create_line(150, 25, 150, 75, width=1)
canvas.create_line(250, 25, 250, 75, width=1)
canvas.create_line(50, 25, 150, 25)
canvas.create_line(50, 75, 150, 75)
canvas.create_line(150, 75, 250, 75)
canvas.create_line(50, 25, 50, 75)

canvas.create_text(100, 50, text='text', tag='rect_0_text')


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

	def __init__(self, p1x, p1y, p2x, p2y, grid_row, grid_column):
		self.row = grid_row
		self.column = grid_column
		self.p1x = p1x
		self.p1y = p1y
		self.p2x = p2x
		self.p2y = p2y
		self.center = ((p1x + p2x) / 2, (p1y + p2y) / 2)
		self.left_line = (self.p1x, self.p1y, self.p1x, self.p2y)
		self.right_line = (self.p2x, self.p1y, self.p2x, self.p2y)
		self.top_line = (self.p1x, self.p1y, self.p2x, self.p1y)
		self.bottom_line = (self.p1x, self.p2y, self.p2x, self.p2y)
		self.object_id = canvas.create_rectangle(self.p1x, self.p1y, self.p2x, self.p2y, width=0)
		#self.tag = str(self.row) + ',' + str(self.column)
		#canvas.itemconfig(self.object_id, tags=(self.tag))

	pass

cell = Cell_object(350, 25, 450, 75, 0, 0)
canvas.create_text(cell.center, text='text', tag='rect_0_text')

canvas.create_line(cell.left_line)
canvas.create_line(cell.top_line)
canvas.create_line(cell.bottom_line)
canvas.create_line(cell.right_line)

canvas.itemconfig(cell.object_id, fill='lightgreen')

string = "0;50,25;150,75"

print(string.split(';'))

frame.grid()

#canvas.grid()


class Table:

	def __init__(self, parent, num_rows, num_columns):

		self.num_rows = num_rows
		self.num_columns = num_columns
		self.canvas = Canvas(parent, width=num_columns * 100, height=num_rows * 25)
		self.canvas.grid()
		self.cells = {}

		x, y, row, column = 0, 0, 0, 0
		while column < num_columns:
			while row < num_rows:
				self.cells[(column, row)] = Cell_object(x, y, x + 100, y + 25, row, column)
				x += 100
				y += 25
				row += 1
				print(column, row)
				#self.canvas.create_line(self.cells[(column, row)].top_line)
			column += 1
			row = 0


		self.canvas.create_line(self.cells[(1, 3)].left_line)
	pass


table = Table(frame, 5, 5)


window.mainloop()

