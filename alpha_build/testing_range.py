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


a = {'a': 1}
b = {'b': 2, 'c': 3}
c = {'a': 5}

a.update(b)
c.update(b)

print(a)
print(c)
print(b)

dict(False)