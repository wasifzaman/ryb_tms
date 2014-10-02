from alpha_ui import *
from alpha_widgets import *
import languages






main_window = Window()
main_window.attributes('-fullscreen', False)
main_window.geometry('1440x900+100+100')

main_app_window = AppWindow(main_window.main_frame, num_rows=3, num_columns=2)
main_app_window.language = languages.languages['english']

main_app_window.menu_frame = main_app_window.newFrame("Menu Frame", (4, 8), column=0)
main_app_window.main_image_frame = main_app_window.newFrame("Main Image Frame", (1, 1), column=1)
main_app_window.app_frame = main_app_window.newFrame("App Frame", (1, 1))
main_app_window.return_button_frame = main_app_window.newFrame("Return Button Frame", (1, 1))

first_name = Textbox(label_text='First Name', language=main_app_window.language, fill_tag=False)
last_name = Textbox(label_text='Last Name', language=main_app_window.language, fill_tag=False)

button_add_student = Button(text='Add Students', language=main_app_window.language)

main_app_window.menu_frame.addWidget(first_name, column=0)
main_app_window.menu_frame.addWidget(last_name, column=0)
main_app_window.menu_frame.addWidget(button_add_student, column=0)




main_window.mainloop()