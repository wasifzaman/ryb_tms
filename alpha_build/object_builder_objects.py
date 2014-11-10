'''
Notes:
	- key: Object_builder object name, value: Object_builder object properties

'''

object_builder_object_properties = {
	
	'Textbox': ['label_text', 'fill_tag'],
	'Scrolled_textbox': ['label_text', 'fill_tag'],
	'Button': ['text'],
	'Coin_widget': ['label_text', 'fill_tag'],
	'Date_widget': ['label_text', 'fill_tag'],
	'Entry_category': ['label_text', 'fill_tag', 'categories']



}

''' Compiler '''

from object_builder import Object_builder

object_builder_objects = {}

for obj, properties, in object_builder_object_properties.items():
	object_builder_objects[obj] = Object_builder(obj, properties)