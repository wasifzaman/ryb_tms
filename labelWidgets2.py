from tkinter import *
from widget import Widget
import inspect
from tkinter.scrolledtext import ScrolledText
from datetime import time, date, datetime

class Textbox(Widget):
	def __init__(self, **kwargs):			
		self.text = kwargs['text']
		self.repr = kwargs['repr']
		self.lang = kwargs['lang']
		self.height = 1
		self.width = 2

	def config(self, **kwargs):

		if 'text' in kwargs:
			s = StringVar()
			s.set(kwargs['text'])
			self.entry.config(textvariable=s)
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text].strip())

	def OnValidate(self, d, i, P, s, S, v, V, W):
		return True

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text].strip(), width=15, anchor=E)
		self.entry = Entry(self.parent, relief=SOLID)

		self.label.grid(row=self.row, column=self.column)
		self.entry.grid(row=self.row, column=self.column+1)

		self.bind()

	def bind(self):
		vcmd = (self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.entry.config(validate="all", validatecommand=vcmd)

	def getData(self):
		return self.entry.get()

	def setData(self, data):
		self.config(text=data)

	def hide(self):
		self.label.grid_forget()
		self.entry.grid_forget()


class IntTextbox(Textbox):

	def OnValidate(self, d, i, P, s, S, v, V, W):
		if S.isdigit():
			return True
		return False

	def getData(self):
		entry_ = self.entry.get()
		if not entry_.isdigit() or len(entry_.strip()) == 0:
			return 0
		else:
			return int(entry_)


class Datebox(IntTextbox):

	def config(self, **kwargs):

		if 'm' in kwargs and 'd' in kwargs and 'y' in kwargs:
			m, d, y = StringVar(), StringVar(), StringVar()
			m.set(kwargs['m'])
			d.set(kwargs['d'])
			y.set(kwargs['y'])
			self.mEntry.config(textvariable=m)
			self.dEntry.config(textvariable=d)
			self.yEntry.config(textvariable=y)
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.selfframe = Frame(self.parent, bg='black')
		self.mdy_frame = Frame(self.selfframe, relief=FLAT, bg='white')
		self.mdy_continaer = Frame(self.mdy_frame, relief=FLAT, bg='white')
		self.label = Label(self.parent, text=self.text, width=15, anchor=E)
		self.dLabel = Label(self.mdy_continaer, text='/', bg='white')
		self.yLable = Label(self.mdy_continaer, text='/', bg='white')

		self.mEntry = Entry(self.mdy_continaer, relief=FLAT, width=4, justify=CENTER)
		self.dEntry = Entry(self.mdy_continaer, relief=FLAT, width=4, justify=CENTER)
		self.yEntry = Entry(self.mdy_continaer, relief=FLAT, width=7, justify=CENTER)

		self.mdy_frame.pack(padx=1, pady=1, fill=X)
		self.mdy_continaer.pack()
		self.selfframe.grid(row=self.row, column=self.column+1, stick=E+W)

		self.label.grid(row=self.row, column=self.column)
		self.dLabel.grid(row=1, column=2)
		self.yLable.grid(row=1, column=4)

		self.mEntry.grid(row=1, column=1, padx=(1, 0))
		self.dEntry.grid(row=1, column=3)
		self.yEntry.grid(row=1, column=5, padx=(0, 1))

		self.bind()

	def OnValidate(self, d, i, P, s, S, v, V, W, digit_type):
		if d == '0': return True
		if not S.isdigit(): return False
		if digit_type == 'date' or digit_type == 'month':
			if len(s) == 2: return False
		elif digit_type == 'year':
			if len(s) == 4: return False
		return True

	def bind(self):
		self.mEntry.config(validate="all", validatecommand=(self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'date'))
		self.dEntry.config(validate="all", validatecommand=(self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'month'))
		self.yEntry.config(validate="all", validatecommand=(self.parent.register(self.OnValidate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W', 'year'))

	def getData(self):
		try:
			date = self.mEntry.get() + '/' + self.dEntry.get() + '/' + self.yEntry.get()
			dt = datetime.strptime(date, '%m/%d/%Y')
			return datetime.strftime(dt, '%m/%d/%Y')
		except ValueError:
			return '01/01/1900'

	def setData(self, data):
		date = data.split('/')
		m, d, y = date[0], date[1], date[2]

		self.config(m=m, d=d, y=y)


class MoneyTextbox(IntTextbox):

	#helpers
	def OnValidate(self, d, i, P, s, S, v, V, W):
		if S.isdigit():
			return True
		else:
			return S == '.' and '.' not in self.entry.get()# or False
		return False

	def getData(self):
		e = self.entry.get()
		if e == '': return 0.00
		try:
			return float("%.2f" % float(e))
		except:
			return 0.00


class Separator(Widget):

	def __init__(self, **kwargs):
		self.repr = kwargs['repr']

	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.fr = Frame(self.parent, height=2, bd=1, relief=SUNKEN)
		self.fr.grid(row=self.row, column=self.column, sticky=W+E, columnspan=100, pady=10)


class Picker(Textbox):

	def __init__(self, **kwargs):
		self.repr = kwargs['repr']
		self.text = kwargs['text']
		self.rads = kwargs['rads']

	def config(self, **kwargs):
		self.lang = kwargs['lang']
		self.label.config(text=self.lang[self.text])
		i = 0
		for rad in self.brads:
			rad.config(text=self.lang[self.rads[i][0]])
			i += 1

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.selfframe = Frame(self.parent)
		self.label = Label(self.selfframe, text=self.text)
		self.entry = Entry(self.selfframe, relief=SOLID)

		self.b, r = StringVar(), []
		self.b.set(self.rads[0][1])
		for rad in self.rads:
			r.append(Radiobutton(self.selfframe, text=rad[0], variable=self.b, \
				value=rad[1], indicatoron=10))#, offrelief=GROOVE, overrelief=SOLID))

		self.brads = r

		self.selfframe.grid()
		self.label.pack()
		self.entry.pack()
		for rad in self.brads:
			rad.pack(side=LEFT)

	def getData(self):
		return self.b.get(), self.entry.get()


class LongTextbox(Textbox):

	def config(self, **kwargs):
		if 'height' in kwargs:
			self.sentry.config(height=kwargs['height'])
		if 'width' in kwargs:
			self.sentry.config(width=kwargs['width'])
		if 'text' in kwargs:	
			self.sentry.insert(END, kwargs['text'])
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])
		
	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text])
		self.sentry = ScrolledText(self.parent, relief=SOLID)

		self.label.grid(row=self.row, column=self.column)
		self.sentry.grid(row=self.row, column=self.column+1, sticky=E)

	def getData(self):
		return self.sentry.get('1.0', END + '-1c')

	def setData(self, data):
		self.sentry.delete('1.0', END)
		self.config(text=data)
		

class Labelbox(Textbox):

	def __init__(self, **kwargs):

		Textbox.__init__(self, **kwargs)

		self.bold = False
		if 'bold' in kwargs: self.bold = kwargs['bold']

	def config(self, **kwargs):

		if 'text' in kwargs:
			self.text=kwargs['text']
			self.label.config(text=self.text)
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text])

	def getData(self):
		return self.text

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text])
		self.label.grid(row=self.row, column=self.column)

		if self.bold:
			self.label.config(font=('Verdana', 11, 'bold'))

	def hide(self):
		self.label.grid_forget()

	def show(self):
		self.label.grid()


class Buttonbox2(Textbox):

	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.repr = kwargs['repr']
		self.lang = kwargs['lang']
		self.width = 30

	def config(self, **kwargs):
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.button.config(text=self.lang[self.text])
		if 'cmd' in kwargs:
			self.cmd = kwargs['cmd']
			self.button.config(command=self.cmd)

	def setData(self, data):
		self.config(text=data)

	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.button = Button(self.parent, text=self.lang[self.text], width=self.width)
		self.button.bind('<Enter>', self.config(bg='blue'))
		self.button.grid(row=self.row, column=self.column)


class Buttonbox(Textbox):

	def __init__(self, **kwargs):
		self.text = kwargs['text']
		self.repr = kwargs['repr']
		self.lang = kwargs['lang']
		self.width = 30
		self.idlebg = '#657FCF'
		self.hoverbg = '#405DB2'
		self.idleborder = '#7D9DFF'
		self.hoverborder = '#5C7DBD'
		self.fg = 'white'
		self.hoverfg = 'white'

	def config(self, **kwargs):
		if 'lang' in kwargs:
			self.lang = kwargs['lang']
			self.button.config(text=self.lang[self.text])
		if 'cmd' in kwargs:
			self.cmd = kwargs['cmd']
			self.args = inspect.getargspec(kwargs['cmd']).args
			if len(self.args) > 0 and self.args[0] != 'self':
				self.button.bind('<ButtonRelease-1>', self.cmd)
				self.button.bind('<Button-1>', self.button.config(bg='#195CBF'))
				self.button.bind('<space>', self.cmd)
			else:
				self.button.bind('<ButtonRelease-1>', lambda e: self.cmd())
				self.button.bind('<space>', lambda e: self.cmd())
			if hasattr(self, 'timeslot_'):
				self.timeslot_.bind('<ButtonRelease-1>', self.cmd)
		if 'width' in kwargs:
			self.width = kwargs['width']
			self.button.config(width=self.width)

	def enter(self, event):
		self.button.config(bg=self.hoverbg, fg=self.hoverfg)
		self.selfframe.config(bg=self.hoverborder)

	def leave(self, event):
		self.button.config(bg=self.idlebg, fg=self.fg)
		self.selfframe.config(bg=self.idleborder)
		
	def setData(self, data):
		self.config(text=data)

	def place(self, **kwargs):
		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.selfframe = Frame(self.parent, bg=self.idleborder, bd=1)
		self.button = Label(self.selfframe, text=self.lang[self.text], width=self.width, bg=self.idlebg, fg=self.fg, \
			font=('Verdana', 11), pady=3)

		self.button.bind('<Enter>', self.enter)
		self.button.bind('<Leave>', self.leave)

		self.selfframe.grid(row=self.row, column=self.column, pady=2)
		self.button.pack()


class TextboxNoEdit(Textbox):

	def config(self, **kwargs):
		if 'text' in kwargs:
			s = StringVar()
			s.set(kwargs['text'])
			self.entry.config(state=NORMAL)
			self.entry.config(textvariable=s)
			self.entry.config(state=DISABLED)
		if 'lang' in kwargs:			
			self.lang = kwargs['lang']
			self.label.config(text=self.lang[self.text].strip())
		
	def place(self, **kwargs):

		self.parent = kwargs['parent']
		self.row = kwargs['row']
		self.column = kwargs['column']

		self.label = Label(self.parent, text=self.lang[self.text].strip(), width=15, anchor=E)
		self.entry = Entry(self.parent, relief=SOLID, state=DISABLED)

		self.label.grid(row=self.row, column=self.column)
		self.entry.grid(row=self.row, column=self.column+1)

		self.bind()