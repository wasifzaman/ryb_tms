import sys, os
sys.path.append(os.path.abspath(os.pardir))
sys.path.append(os.path.abspath(os.pardir) + '\widgets')
images = os.path.abspath(os.pardir) + '\images\\'

from tkinter import *

from mbox2 import Mbox
from button import Buttonbox
from simple_label import Labelbox
from photoWidget2 import Photo
from languages import languages

language = languages["english"]

ws = Photo(repr='ws', path=os.path.abspath(os.pardir) + '\images\\' + 'ws_sm.png')
bok = Buttonbox(text='ok', lang=language, repr='bok')