from tkinter import *

def find_all(root, output):
	if len(root.winfo_children()) == 0:
		return
	else:
		for child in root.winfo_children():
			#_list.append(root)
			find_all(child, output)
			if type(child) == Label:
				output.append(child)

def translate(root, translation_lib):
	label_lib = []
	find_all(root, label_lib)

	for label in label_lib:
		if label.cget('text') in translation_lib:
			label.config(text=translation_lib[label.cget('text')])