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

canvas = Canvas(frame, width=500, height=300)

canvas.create_rectangle(50, 25, 150, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)
canvas.create_rectangle(150, 25, 250, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)
canvas.create_rectangle(250, 25, 350, 75, fill="lightblue", outline="lightblue", tag='rect_0', width=0)

canvas.create_line(150, 25, 150, 75, width=1)
canvas.create_line(250, 25, 250, 75, width=1)

canvas.create_text(100, 50, text='text')


def select_row(event):
	for rect in canvas.find_withtag('rect_0'):
		canvas.itemconfig(rect, fill='blue')
	return

for rect in canvas.find_withtag('rect_0'):
	canvas.itemconfig(rect, fill='red')


canvas.tag_bind('rect_0', '<Button-1>', select_row)



frame.grid()

canvas.grid()

window.mainloop()

