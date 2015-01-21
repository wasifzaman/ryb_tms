from tkinter import *


class Cell:

	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.pos = kwargs['pos']
		self.bgcolor = 'white'
		self.altbgcolor = 'white'
	
	def config(self, **kwargs):
		if 'width' in kwargs:
			self.label.config(width=kwargs['width'])
		if 'text' in kwargs:
			self.label.config(text=kwargs['text'])
		if 'bgcolor' in kwargs:
			self.bgcolor = kwargs['bgcolor']
			self.label.config(bg=self.bgcolor)
		if 'bind' in kwargs:
			event = kwargs['bind'][0]
			command = kwargs['bind'][1]
			self.label.bind(event, command)
		
	def getData(self):
		return self.label.cget('text')
		
	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.label = Label(self.parent, text=self.text, bg=self.bgcolor)

		self.label.grid(row=self.pos[0], column=self.pos[1], sticky=E+W)


class Table:

	def __init__(self, **kwargs):
		self.repr = kwargs['repr']
		self.editwidget = kwargs['edit']
		self.cells = {}
		self.data = {}
		self.clast = False

	def config(self, **kwargs):
		if 'lang' in kwargs:
			for cell_id, cell_val in self.cells.items():
				if cell_id[0] == 0:
					cur_text = cell_val.label.cget('text')
					if cur_text in lang:
						cell_val.label.config(text=lang[cur_text])
		if 'header_color' in kwargs:
			return

	def set_width(self, start_column, end_column, width):
		for column in range(start_column, end_column + 1):
			row = 0 if not hasattr(self, 'headers') else 1
			self.cells[(row, column)].label.config(width=width)		
		
	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.canvas = Canvas(self.parent, bg='white', confine=True)
		self.outerframe = Frame(self.canvas, bg='black')

		self.xscrollbar = Scrollbar(self.parent, orient="horizontal", command=self.canvas.xview)
		self.yscrollbar = Scrollbar(self.parent, orient="vertical", command=self.canvas.yview)
		self.canvas.create_window((0,0), window=self.outerframe, anchor=NW, tags="table_frame")
		
		for cell_id, cell in self.cells.items():
			cell.place(parent=self.outerframe, pos=cell.pos)
			if cell_id[0] == 0:
				cell.label.grid(padx=(0, 1), pady=(1, 0))
			elif cell_id[1] == 0:
				cell.label.grid(padx=1, pady=(0, 1))	

		self.canvas.grid(row=0, column=0)
		self.yscrollbar.grid(row=0, column=1, sticky=NS)
		#self.xscrollbar.grid(row=1, column=0, sticky=EW)
		
		self.parent.bind("<Configure>", self.makeScroll)

		#self.scroll_up_button = Button(self.parent, text='Up')
		#self.scroll_down_button = Button(self.parent, text='Down')
		#self.scroll_up_button.grid(row=0, column=1)
		#self.scroll_down_button.grid(row=0, column=2)
		#self.scroll_down_button.config(command=lambda: self.canvas.yview_scroll(1, UNITS))
		#self.scroll_up_button.config(command=lambda: self.canvas.yview_scroll(-1, UNITS))

		def print_coords(event):
			canvas = event.widget
			x = canvas.canvasx(event.x)
			y = canvas.canvasy(event.y)
			print(x,y)

		self.canvas.bind('<Button-1>', print_coords)

	def setData(self, **kwargs):
		olddata = self.data
		newdata = kwargs['data']

		if newdata == [[]]: return

		#delete extra cells
		last_row = len(newdata)
		for row in range(last_row, len(olddata)):
			for col in range(0, len(self.headers) + 1):
				self.cells[(row, col)].label.grid_forget()
				del self.cells[(row, col)]

		row, col = 1, 1
		for row_ in newdata:
			for text in row_:
				if (row, col) not in self.cells:
					self.cells[(row, col)] = Cell(text=text, pos=(row, col))
					self.cells[(row, col)].place(parent=self.outerframe, \
													pos=self.cells[(row, col)].pos)
					self.cells[(row, col)].label.grid(padx=(0, 1), pady=(0, 1))
				else:
					self.cells[(row, col)].label.config(text=text)
					self.cells[(row, col)].label.grid(padx=(0, 1), pady=(0, 1))
				col += 1

				#numbering
				self.cells[(row, 0)] = Cell(text=row, pos=(row, 0))
				self.cells[(row, 0)].place(parent=self.outerframe, \
													pos=self.cells[(row, 0)].pos)
				self.cells[(row, 0)].label.grid(padx=1, pady=(0, 1))
			row += 1
			col = 1

		self.data = newdata

		if 'headers' in kwargs:
			self.headers = kwargs['headers']
			row, col = 0, 1
			for data in self.headers:
				self.cells[(row, col)] = Cell(text=data, pos=(row, col))
				self.cells[(row, col)].place(parent=self.outerframe, \
													pos=self.cells[(row, col)].pos)
				self.cells[(row, col)].label.grid(padx=(0, 1), pady=1)
				col += 1

		Label(self.outerframe, text='', bg='white', width=3).\
			grid(row=0, column=0, padx=1, pady=1, sticky=E+W)

		self.canvas.coords("table_frame", (0, 0))
		self.outerframe.update_idletasks()
		self.canvas.config(scrollregion=self.canvas.bbox("all"))

	def makeScroll(self, event):
		self.canvas.config(scrollregion=self.canvas.bbox("all"))

	def getData(self):
		return self.headers, self.data

	'''
	** rewrite **
	def edit(self, pos):
		if not self.editwidget: return

		row = pos[0]
		col = pos[1]
		
		if row == 0 or col == 0: return

		def kill(event):
			self.data[row-1][col-1] = self.temp.get()
			self.update(data=self.data, headers=self.headers)
			self.temp.destroy()

		stringvar = StringVar()
		stringvar.set(self.cells[pos].getData())

		self.temp = Entry(self.innerframe,
			textvariable=stringvar,
			width=self.column_width_of[pos[1]])
		self.temp.grid(row=pos[0], column=pos[1])
		self.temp.focus_set()
		self.temp.grab_set()
		self.temp.bind("<Return>", kill)
	'''