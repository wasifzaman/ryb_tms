from tkinter import *


t = Tk()

b = Button(text='test', command=lambda: t.state('zoomed'))
b2 = Button(text='test2', command=lambda: t.state('normal'))
b.pack()
b2.pack()

t.mainloop()