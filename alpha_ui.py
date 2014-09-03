from tkinter import *
from PIL import Image, ImageTk



class AppFrame(Frame):

	def __init__(self, parent, num_rows=1, num_columns=1, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid_max_rows = num_rows
		self.grid_max_columns = num_columns
		self.grid_items = {}
		self.widgets = {}

		#self.config(bg='grey') #debugger

	def float(self, state=True):
		if state:
			self.grab_set()
			self.focus_set()
			self.state = 'float'
		else:
			self.grab_release()
			self.state = 'normal'

	def addWidget(self, widget, row=False, column=False):
		self.widgets[widget.repr] = widget
		is_empty = False

		if type(row) != bool and type(column) != bool and (row, column) not in self.grid_items:
			is_empty = (row, column)
		elif type(row) != bool:
			is_empty = self.grid_search(row=row)
		elif type(column) != bool:
			is_empty = self.grid_search(column=column)
		else:
			is_empty = self.grid_search()

		if not is_empty:
			print("grid slot taken")
			return

		self.grid_items[is_empty] = widget.repr
		self.widgets[widget.repr].place(parent=self, column=is_empty[1], row=is_empty[0])

	def grid_search(self, row=False, column=False):
		found = False
		if type(row) != bool:
			for x in range(0, self.grid_max_columns):
				if (row, x) not in self.grid_items:
					found = (row, x)
					break
		elif type(column) != bool:
			for y in range(0, self.grid_max_rows):
				if (y, column) not in self.grid_items:
					found = (y, column)
					break
		else:
			for x in range(0, self.grid_max_rows):
				if found: break
				for y in range(0, self.grid_max_columns):
					if (x, y) not in self.grid_items:
						found = (x, y)

		return found

class AppWindow(Frame):

	def __init__(self, parent, num_rows=1, num_columns=1, *args, **kwargs):		
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent
		self.grid_max_rows = num_rows
		self.grid_max_columns = num_columns
		self.grid_items = {}
		self.option_add("*Font", "Verdana 11")

		self.outer_frame = Frame(self)
		self.main_frame = Frame(self.outer_frame, bd=10)
		self.outer_frame.pack(fill="both", expand=True)
		self.main_frame.place(in_=self.outer_frame, anchor="c", relx=.5, rely=.5)

		#self.option_add("*Background", "lightgrey") #debugger

		#frames
		self.frames = {}
		self.frame_padding_x = 10
		self.frame_padding_y = 1

		self.pack()
		self.outer_frame.grid()
		self.main_frame.grid()

	def newFrame(self, frame_name, frame_size=(1, 1), row=False, column=False):
		rows = frame_size[1]
		columns = frame_size[0]

		is_empty = False

		if type(row) != bool and type(column) != bool and (row, column) not in self.grid_items:
			is_empty = (row, column)
		elif type(row) != bool:
			is_empty = self.grid_search(row=row)
		elif type(column) != bool:
			is_empty = self.grid_search(column=column)
		else:
			is_empty = self.grid_search()

		if not is_empty:
			print("grid slot taken")
			return

		self.grid_items[is_empty] = frame_name

		self.frames[frame_name] = AppFrame(self.main_frame, num_rows=rows, num_columns=columns)
		self.frames[frame_name].grid(
			row=is_empty[0], column=is_empty[1],
			padx=self.frame_padding_x, pady=self.frame_padding_y, sticky=N)

		return self.frames[frame_name]

	def grid_search(self, row=False, column=False):
		found = False
		if type(row) != bool:
			for x in range(0, self.grid_max_columns):
				if (row, x) not in self.grid_items:
					found = (row, x)
					break
		elif type(column) != bool:
			for y in range(0, self.grid_max_rows):
				if (y, column) not in self.grid_items:
					found = (y, column)
					break
		else:
			for x in range(0, self.grid_max_rows):
				if found: break
				for y in range(0, self.grid_max_columns):
					if (x, y) not in self.grid_items:
						found = (x, y)

		return found

	def collect(self, relevant):
		crossed = {}

		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.repr in relevant:
					crossed[widget.repr] = widget.getData()

		return crossed

	def populate(self, info):
		for frame in self.frames.values():
			for widget in frame.widgets.values():
				if widget.repr in info:
					try:
						widget.setData(info[widget.repr])
					except:
						continue

	def dw(self):
		self.destroy()
		

class Window(Tk):

	def __init__(self, top=False, *args, **kwargs):
		if top: Toplevel.__init__(self, *args, **kwargs)
		else: Tk.__init__(self, *args, **kwargs)

		self.attributes('-fullscreen', True)

		self.pic = Image.open('bigbl.jpg')
		self.img = ImageTk.PhotoImage(self.pic)


		self.outer_frame = Frame(self)

		#background label
		Label(self.outer_frame, image=self.img).place(x=-2, y=-5, in_=self.outer_frame)

		self.main_frame = Frame(self.outer_frame)

		#title frame and x button START
		self.titleFrame = Frame(self.main_frame, bg="#4D4D4D", height=60)
		self.titleFrame.pack(fill=X)

		self.wintitle = Label(self.titleFrame, bg='#4D4D4D', fg='white', font=('Jumbo', 15, 'bold'))
		self.wintitle.place(in_=self.titleFrame, anchor="c", relx=.5, rely=.5)

		self.outer_frame.pack(fill="both", expand=True)
		self.main_frame.place(in_=self.outer_frame, anchor="c", relx=.5, rely=.5)

		self.outer_frame.config(bg="#FFF5EE")

		#center items?
		self.update_idletasks()
		self.after_idle(lambda: self.minsize(self.winfo_width(), self.winfo_height()))	

		
	

		
		
if __name__ == "__main__":

	w = Window()

	w.mainloop()