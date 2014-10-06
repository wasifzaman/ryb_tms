from tkinter import RIGHT

class object_setting:
	pass

button_scheme_1 = object_setting()
button_scheme_1.label_settings = {'bg': 'purple', 'fg': 'white', 'width': 30}
button_scheme_1.hover_settings = {'bg': 'magenta', 'fg': 'black'}

coin_scheme_1 = object_setting()
coin_scheme_1.entry_settings = {'width': 10, 'justify': RIGHT}

entry_category_scheme_1 = object_setting()
entry_category_scheme_1.categories_settings = {'bg': 'orange', 'fg': 'black', 'width': 15}
entry_category_scheme_1.categories_hover_settings = {'bg': 'lightblue'}
entry_category_scheme_1.selected_category_settings = {'bg': 'pink'}