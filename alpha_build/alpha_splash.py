from alpha_ui import *
from alpha_widgets import *
from object_settings import *
import languages




main_window = Window()
main_window.attributes('-fullscreen', False)
main_window.geometry('800x600+100+100')

main_app_window = AppWindow(main_window.main_frame, num_rows=3, num_columns=2)
main_app_window.language = languages.languages['english']

main_app_window.menu_frame = main_app_window.newFrame("Menu Frame", (4, 15), column=0)
main_app_window.main_image_frame = main_app_window.newFrame("Main Image Frame", (1, 1), column=1)
main_app_window.app_frame = main_app_window.newFrame("App Frame", (1, 1))
main_app_window.return_button_frame = main_app_window.newFrame("Return Button Frame", (1, 1))

button_add_teacher = Button(text='Add Teachers', language=main_app_window.language, settings=button_scheme_1)
button_check_in_teacher = Button(text='Check-in Teacher', language=main_app_window.language, settings=button_scheme_1)
button_check_out_teacher = Button(text='Check-out Teacher', language=main_app_window.language, settings=button_scheme_1)
button_teacher_database = Button(text='Teacher Database', language=main_app_window.language, settings=button_scheme_1)
button_change_language = Button(text='Change Language', language=main_app_window.language, settings=button_scheme_1)
button_print_report = Button(text='Print Report', language=main_app_window.language, settings=button_scheme_1)
button_exit = Button(text='Exit', language=main_app_window.language, settings=button_scheme_1)

text_first_name = Textbox(label_text='First Name', language=main_app_window.language)
text_first_name_filter_all = Textbox(label_text='First Name', language=main_app_window.language, filter='all')
coin_payment = Coin_widget(label_text='Last Payment', language=main_app_window.language, whole_text=10, cent_text=5, settings=coin_scheme_1)
date_of_birth = Date_widget(label_text='Date of Birth', language=main_app_window.language, entry_width=10)


main_app_window.menu_frame.addWidget(button_add_teacher, column=0)
main_app_window.menu_frame.addWidget(button_check_in_teacher, column=0)
main_app_window.menu_frame.addWidget(button_check_out_teacher, column=0)
main_app_window.menu_frame.addWidget(button_teacher_database, column=0)
main_app_window.menu_frame.addWidget(button_change_language, column=0)
main_app_window.menu_frame.addWidget(button_print_report, column=0)
main_app_window.menu_frame.addWidget(button_exit, column=0)
main_app_window.menu_frame.addWidget(text_first_name, column=0)
main_app_window.menu_frame.addWidget(text_first_name_filter_all, column=0)
main_app_window.menu_frame.addWidget(coin_payment, column=0)
main_app_window.menu_frame.addWidget(date_of_birth, column=0)

date_of_birth.set_data(datetime(1988, 10, 7))

main_window.mainloop()