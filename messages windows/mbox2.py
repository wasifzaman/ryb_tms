import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\windows')

from uiHandler22 import *

class Mbox(AppWindow):

	def __init__(self, title=''):
		self.root = Toplevel()
		self.root.resizable(0, 0)
		self.root.grab_set()
		self.root.focus_set()
		self.root.protocol('WM_DELETE_WINDOW', self.dw)
		self.root.overrideredirect(1)

		w = self.root.winfo_screenwidth()
		h = self.root.winfo_screenheight()

		w, h = w//2, h//2

		self.root.title(title)
		self.root.geometry('+' + str(w) + '+' + str(h))
		self.root.config(bg="#000066")

		self.title_ = Label(self.root, bg='#000066', fg='white')
		self.mainFrame = Frame(self.root)
		self.title_.pack(padx=1, pady=1, fill=X)
		self.mainFrame.pack(padx=1, pady=1)

		self.frames = {}
		self.framePadding = (10, 15)

		def start_move(event):
			self.drag_x = event.x
			self.drag_y = event.y

		def in_motion(event):
			delta_x = event.x - self.drag_x
			delta_y = event.y - self.drag_y
			x = self.root.winfo_x() + delta_x
			y = self.root.winfo_y() + delta_y
			self.root.geometry("+%s+%s" % (x, y))

		self.title_.bind('<ButtonPress-1>', start_move)
		self.title_.bind('<B1-Motion>', in_motion)

	def config(self, **kwargs):
		if 'bg' in kwargs:
			self.bgc = kwargs['bg']
			for frame in self.frames.values():
				frame.config(bg=self.bgc)

				for widget in frame.widgets.values():
					widget.config(bg=kwargs['bg'])

	def dw(self):
		self.root.destroy()