import sys, os
sys.path.append(os.path.abspath(os.pardir) + '\windows')

from uiHandler22 import *

class Mbox(AppWindow):

	def __init__(self, title=''):
		self.root = Toplevel(bd=2)
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
		self.root.config(bg="#9FB6CD")

		self.mainFrame = Frame(self.root)#, bg='grey', bd=10)
		self.mainFrame.pack(fill=Y, expand=1, anchor=S)

		self.frames = {}
		self.framePadding = (0, 0)

	def config(self, **kwargs):
		if 'bg' in kwargs:
			self.bgc = kwargs['bg']
			for frame in self.frames.values():
				frame.config(bg=self.bgc)

				for widget in frame.widgets.values():
					widget.config(bg=kwargs['bg'])

	def dw(self):
		self.root.destroy()