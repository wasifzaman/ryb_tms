from tkinter import *
from widget import Widget
import copy

class Cell(Widget):

	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.pos = kwargs['pos']
		self.bgcolor = 'white'
		self.altbgcolor = 'white'
		self.bd = 1
		self.relief = SOLID
	
	def config(self, **kwargs):
		if 'width' in kwargs:
			self.label.config(width=kwargs['width'])
		if 'text' in kwargs:
			self.label.config(text=kwargs['text'])
		if 'bgcolor' in kwargs:
			self.bgcolor = kwargs['bgcolor']
			self.label.config(bg=self.bgcolor)
		if 'bind' in kwargs:
			btn = kwargs['bind'][0]
			cmd = kwargs['bind'][1]
			self.label.bind(btn, cmd)
		
	def getData(self):
		return self.label.cget('text')
		
	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.label = Label(self.parent, text=self.text, relief=self.relief,\
			bd=self.bd, bg=self.bgcolor, height=0)

		self.label.grid(row=self.pos[0], column=self.pos[1])

	def delete(self, **kwargs):
		self.label.grid_remove()


class Table(Widget):

	def __init__(self, **kwargs):
		self.repr = kwargs['repr']
		self.editwidget = kwargs['edit']
		self.clast = False
		self.editable = 'all'

	def config(self, lang):
		for cell_id, cell_val in self.cells.items():
			if cell_id[0] == 0:
				cur_text = cell_val.label.cget('text')
				if cur_text in lang:
					cell_val.label.config(text=lang[cur_text])

	def edit(self, pos):

		if not self.editwidget: return
		if pos[0] == 0 or pos[1] == 0: return

		def kill(event):
			self.data[pos[0]-1][pos[1]-1] = self.temp.get()
			self.update(data=self.data, headers=self.headers)
			self.temp.destroy()

		t = StringVar()
		t.set(self.cells[pos].getData())

		self.temp = Entry(self.innerframe, textvariable=t, width=self.cwids[pos[1]])
		self.temp.grid(row=pos[0], column=pos[1])
		self.temp.focus_set()
		self.temp.grab_set()
		self.temp.bind("<Return>", kill)

	def build(self, **kwargs):

		self.headers = kwargs['headers']
		self.data = kwargs['data']
		self.cells = {}

		r, l = 1, 0
		for row in self.data:
			c = 1
			for data in row:
				self.cells[(r, c)] = Cell(text=data, pos=(r, c))
				c += 1
			r += 1
			l = max(l, len(row))

		self.headers = self.headers[:l]

		tr, r, c = r, 1, 0
		for n in range(1, tr):
			self.cells[(r, c)] = Cell(text=str(n), pos=(r, c))
			r += 1

		r, c = 0, 1
		for data in self.headers:
			self.cells[(r, c)] = Cell(text=data, pos=(r, c))
			c += 1

	def intersect(self, newdata, olddata):
		cross = {}
		deprecated = {}

		new = {}
		old = {}

		r = 0
		for row in newdata:
			c = 0
			for data in row:
				new[(r + 1, c + 1)] = data
				c += 1
			r += 1

		r = 0
		for row in olddata:
			c = 0
			for data in row:
				old[(r + 1, c + 1)] = data
				c += 1
			r += 1

		for key, val in old.items():
			if key in new and new[key] != val:
				cross[key] = new[key]
			elif key not in new:
				deprecated[key] = val

		return cross, deprecated

	def update(self, **kwargs):
		self.previous = list(self.data)
		self.previouscells = dict(self.cells)

		self.build(**kwargs)

		cross, deprecated = self.intersect(self.data, self.previous)

		for cell in deprecated:
			self.previouscells[cell].delete()
			del self.previouscells[cell]

		for key, value in cross.items():
			self.previouscells[key].config(text=self.data[key[0]-1][key[1]-1])

		for n in range(len(self.data), len(self.previous)):
			self.previouscells[(n+1, 0)].delete()

		for pos, cell in self.cells.items():
			if pos in cross:
				self.cells[pos] = self.previouscells[pos]
		
		for pos, cell in self.cells.items():
			if pos not in cross:
				cell.place(parent=self.innerframe, pos=cell.pos)
	
		for pos, cell in self.cells.items():
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: self.edit(pos)))

		if self.clast:
			for cell in self.cells:
				if cell[0] == len(self.data):
					self.cells[cell].config(bgcolor=self.clast)

		self.resize()

		self.canvas.config(scrollregion=self.canvas.bbox("all"))

	def resize(self):
		self.cwids = {}
		for cell in self.cells:
			self.cwids[cell[1]] = 0
		
		self.cwids[0] = 4
		for key, value in self.cells.items():
			self.cwids[key[1]] = max(self.cwids[key[1]], len(value.getData()))
		
		for key, value in self.cells.items():
			value.config(width=self.cwids[key[1]] + 2)

	def makeScroll(self, event):
		self.canvas.config(scrollregion=self.canvas.bbox("all"))
		self.xscrollbar.pack(side=BOTTOM, fill=X)
		self.canvas.pack(side=LEFT)			
		self.yscrollbar.pack(side=RIGHT, fill=Y)

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.container = Frame(self.parent)
		self.canvas = Canvas(self.container)
		self.outerframe = Frame(self.canvas)
		self.innerframe = Frame(self.outerframe)		

		self.xscrollbar = Scrollbar(self.container, orient="horizontal", command=self.canvas.xview, relief=FLAT)
		self.yscrollbar = Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
		self.canvas.config(xscrollcommand=self.xscrollbar.set)
		self.canvas.config(yscrollcommand=self.yscrollbar.set)
		
		for cell in self.cells.values():
			cell.place(parent=self.innerframe, pos=cell.pos)
	
		self.container.grid()
		self.innerframe.grid(row=0, column=0, pady=30)
		self.canvas.create_window((0,0), window=self.outerframe, anchor=NW)
		self.parent.bind("<Configure>", self.makeScroll)
		self.resize()

		if len(self.cells) == 1 and (1, 0) in self.cells:
			self.cells[(1, 0)].label.grid_forget()

	def deleteAll(self):
		for cell in self.cells.values():
			cell.delete()

		self.cells = {}

	def getData(self):
		return self.headers, self.data

	def setData(self, data):
		headers = data[0]
		information = data[1]

		self.update(headers=data[0], data=data[1])