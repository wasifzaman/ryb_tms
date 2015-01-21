from tkinter import *


t = Tk()

b = Button(text='test', command=lambda: t.state('zoomed'))
b2 = Button(text='test2', command=lambda: t.state('normal'))
b.pack()
<<<<<<< HEAD
=======
'''

tup = (0, 0, 5, 5)
f = Frame(t)
c = Canvas(f, bg='red', width=30, height=300)
c.config(scrollregion=(0, 0, 0, 0))
f2 = Frame(c)
yscroll = Scrollbar(f, orient="vertical", command=c.yview)
b1 = Button(f, text='Up')
b2 = Button(f, text='Down')

b1.pack()
>>>>>>> parent of 2e98c4e... Revert "upgr"
b2.pack()


<<<<<<< HEAD
x = [1, 2, 3, 4]
print(x[:3])
=======


for i in range(1, 4):
	print(i)
>>>>>>> parent of 2e98c4e... Revert "upgr"

#t.mainloop()
