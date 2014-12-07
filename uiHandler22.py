from tkinter import *
import os.path
from PIL import Image, ImageTk



class AppFrame(Frame):

	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.curRow = 0
		self.curColumn = 0
		#self.config(bg='grey') #debugger

		#widgets
		self.widgets = {}

	def addWidget(self, widget, pos):
		self.widgets[widget.repr] = widget
		self.widgets[widget.repr].place(parent=self, row=pos[0], column=pos[1])

class AppWindow(Frame):

	def __init__(self, parent, *args, **kwargs):
		
		Frame.__init__(self, parent, *args, **kwargs)
		self.parent = parent

		self.oframe = Frame(self)
		self.mainFrame = Frame(self.oframe, bd=10)
		self.oframe.pack(fill="both", expand=True)
		self.mainFrame.place(in_=self.oframe, anchor="c", relx=.5, rely=.5)

		#troubleshooter
		#self.option_add("*Background", "lightgrey")

		#font-size
		self.option_add("*Font", "Verdana 11")

		#frames
		self.frames = {}
		self.framePadding = (10, 1)

		#
		#self.update_idletasks()
		#self.after_idle(lambda: self.minsize(self.winfo_width(), self.winfo_height()))	

		self.pack()
		self.oframe.grid()
		self.mainFrame.grid()


	def newFrame(self, frameName, gridpos=(0,0)):
		gridRow = gridpos[0]
		gridColumn = gridpos[1]

		self.frames[frameName] = AppFrame(self.mainFrame)

		self.frames[frameName].grid(
			row=gridRow, column=gridColumn,
			padx=self.framePadding[0], pady=self.framePadding[1], sticky=N)


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
		#if top, Toplevel
		#else: Tk
		if top: Toplevel.__init__(self, *args, **kwargs)
		else: Tk.__init__(self, *args, **kwargs)

		self.attributes('-fullscreen', True)

		self.pic = Image.open('bigbl.jpg')
		self.img = ImageTk.PhotoImage(self.pic)


		self.oframe = Frame(self)

		#bg
		Label(self.oframe, image=self.img).place(x=-2, y=-5, in_=self.oframe)

		self.mainFrame = Frame(self.oframe)#, bd=1, bg='lightgrey')

#title frame and x button START
		self.titleFrame = Frame(self.mainFrame, bg="#000000", height=60)
		self.titleFrame.pack(fill=X)

		self.wintitle = Label(self.titleFrame, bg='#000000', fg='white', font=('Jumbo', 15, 'bold'))
		self.wintitle.place(in_=self.titleFrame, anchor="c", relx=.5, rely=.5)

		#self.exit = Label(self.titleFrame, bg='#B20000', fg='white', text='  ×  ', font=('Arial', 12, 'bold'))
		#self.exit.place(in_=self.titleFrame, anchor='c', relx=.987, rely=.48)

		#self.exit.bind('<Enter>', lambda e: self.exit.config(bg='red'))
		#self.exit.bind('<Leave>', lambda e: self.exit.config(bg='#B20000'))
#title frame and x button END

		self.oframe.pack(fill="both", expand=True)#, padx=20, pady=20)
		self.mainFrame.place(in_=self.oframe, anchor="c", relx=.5, rely=.5)

		self.oframe.config(bg="#FFF5EE")

		#
		self.update_idletasks()
		self.after_idle(lambda: self.minsize(self.winfo_width(), self.winfo_height()))	

		
	

		
		
if __name__ == "__main__":

	w = Window()

	w.mainloop()