from labelWidgets2 import *
from tableWidget2 import *
from photoWidget2 import *
from languages import *
from mbox2 import *
from tkinter import filedialog
from Crypto.Cipher import AES
import pickle
from datetime import datetime
import tkinter.ttk as ttk

language = languages["english"]

#duplicates of these widgets cannot exist if duplicates are desired, they have to be created by user

#strings
firstName = Textbox(text="First Name", lang=language, repr='firstName')
lastName = Textbox(text="Last Name", lang=language, repr='lastName')
chineseName = Textbox(text="Chinese Name", lang=language, repr='chineseName')
schoolLoc = Textbox(text="School Location", lang=language, repr='schoolLoc')
bCode = Textbox(text="Barcode", lang=language, repr='bCode')
bCodeNE = TextboxNoEdit(text="Barcode", lang=language, repr='bCode')
gender = Textbox(text="Gender", lang=language, repr='gender')
parentName = Textbox(text="Parent Name", lang=language, repr='parentName')
pup = Textbox(text="Pick up Person", lang=language, repr='pup')
addr = Textbox(text="Address", lang=language, repr='addr')
state = Textbox(text="State", lang=language, repr='state')
city = Textbox(text="City", lang=language, repr='city')
wkdwknd = Textbox(text="Weekday/Weekend", lang=language, repr='wkdwknd')
ctime = Textbox(text="Class time", lang=language, repr='ctime')
email = Textbox(text="E-mail", lang=language, repr='email')
sType = Textbox(text="Service Type", lang=language, repr='sType')
hPhone = Textbox(text="Home Phone", lang=language, repr='hPhone')
cPhone = Textbox(text="Cell Phone", lang=language, repr='cPhone')
cPhone2 = Textbox(text="Cell Phone 2", lang=language, repr='cPhone2')
cp = Textbox(text="Card Printed", lang=language, repr='cp')

#integers
age = IntTextbox(text="Age", lang=language, repr='age')
sid = IntTextbox(text="Old Student ID", lang=language, repr='sid')
zip = IntTextbox(text="Zipcode", lang=language, repr='zip')
cAwarded = IntTextbox(text="Classes Awarded", lang=language, repr='cAwarded')
cRemaining = IntTextbox(text="Classes Remaining", lang=language, repr='cRemaining')

#date
dob = Datebox(text="Date of Birth", lang=language, repr='dob')
tpd = Datebox(text="Tuition Paid Day", lang=language, repr='tpd')

#money
tpa = MoneyTextbox(text="Tuition Pay Amount", lang=language, repr='tpa')
tpo = MoneyTextbox(text="Amount Owed", lang=language, repr='tpo')
tp = MoneyTextbox(text="Already Paid", lang=language, repr='tp')

#attendance table
attinfo = Table(repr='attinfo', edit=True)
attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
attinfo.build(headers=attinfoh, data=[[]])
attinfo.clast = '#FF99FF'

stable = Table(repr='stable', edit=False)
stableh = [language['Barcode'], language['First Name'], \
	language['Last Name'], language['Chinese Name'], language['Date of Birth']]
stable.build(headers=stableh, data=[[]])
def sbind(f):
	def fsb(p):
		i = stable.data[p[0]-1][0]
		try:
			f(i)
		except:
			print(stable.data[p[0]-1][0])

	try:
		for pos, cell in stable.cells.items():
			cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))
	except:
		print("cells could not be bound")


portr = Photo(repr='portr', path='monet_sm.jpg')

sepr = Separator(repr='sepr')
sby = Picker(repr='sby', text=language['Search By'], rads=[(language['Barcode'], 'bCode'), \
	(language['First Name'], 'firstName'), \
	(language['Last Name'], 'lastName'), \
	(language['Chinese Name'], 'chineseName'), \
	(language['Phone Number'], 'phoneNumber')])

#info titles
sinfo = Labelbox(text='Student information', lang=language, repr='sinfo')
ainfo = Labelbox(text='Address information', lang=language, repr='ainfo')
cinfo = Labelbox(text='Contact information', lang=language, repr='cinfo')
pinfo = Labelbox(text='Payment information', lang=language, repr='pinfo')
ninfo = Labelbox(text='Notes', lang=language, repr='ninfo')

#early checkin
checkin25 = TextboxNoEdit(text='25s', lang=language, repr='25s')
checkin50 = TextboxNoEdit(text='50s', lang=language, repr='50s')
checkin100 = TextboxNoEdit(text='100s', lang=language, repr='100s')
early_checkin = TextboxNoEdit(text='Early Check-in', lang=language, repr='inrow')




def spicker(d):

	def sets(i):
		stable.s = i
		t.destroy()

	def destroy():
		stable.s = False
		t.destroy()

	t = Toplevel()
	frame = Frame(t, padx=10, pady=10)
	frame.pack()
	t.grab_set()
	t.focus_set()
	t.protocol('WM_DELETE_WINDOW', destroy)
	t.geometry('570x440')


	stable.build(headers=stableh, data=d)
	stable.place(parent=frame, row=0, column=0)
	stable.canvas.config(widt=530, height=400)

	sbind(lambda i: sets(i=i))

	t.resizable(0, 0)

	t.wait_window()

	#return s
	return stable.s

def cward(lang):

	def sel(c):
		t.c = c
		t.destroy()
		t.cancel = False

	
	t = Window(top=True)
	t.attributes('-fullscreen', False)
	t.geometry('420x200')
	t.resizable(0, 0)
	t.grab_set()
	t.focus_set()
	t.cancel = True
	t.c = 0


	w = AppWindow(t.mainFrame)

	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')

	w.newFrame("First Frame", (0, 0))

	w.frames["First Frame"].addWidget(bgold, (0, 0))
	w.frames["First Frame"].addWidget(bbasic, (1, 0))

	bgold.config(cmd=lambda: sel(60))
	bbasic.config(cmd=lambda: sel(15))


	#t = Toplevel()
	#t.grab_set()
	#t.focus_set()
	#t.cancel = True

	t.protocol('WM_DELETE_WINDOW', t.destroy)

	#frame = Frame(t)
	#frame.grid()

	#rads = [('Gold', 60, 'This awards the student 60 classes.'),\
	#('Basic', 15, 'This awrards the student 15 classes.')]
	#b, r = StringVar(), []
	#b.set(rads[0][1])

	#info = Label(frame, text=rads[0][2])
	#info.grid()


	#for rad in rads:
	#	rb = Radiobutton(frame, text=rad[0], variable=b, value=rad[1], indicatoron=0, width=20)
	#	rb.bind('<Button-1>', lambda event, r=rad[2]: info.config(text=r))
	#	r.append(rb)

	#rads = r

	


	#for rad in rads:
	#	rad.grid()

	#bac = Buttonbox(text='awardclass', lang=language, repr='bac')
	#bac.place(parent=frame, row=4, column=0)
	#bac.config(cmd=sel)

	t.wait_window()

	return t.c

def sstype():
	if cAwarded.getData() >= 60:
		sType.setData('Gold')
	else:
		sType.setData('Basic')

def cpicker(lang):
	cAwarded.setData(cward(lang))
	cRemaining.setData(cAwarded.getData())
	sstype()

def cadd(lang):
	new = cward(lang)
	cAwarded.setData(cAwarded.getData() + new)
	cRemaining.setData(cRemaining.getData() + new)
	sstype()

def caddone():
	cAwarded.setData(cAwarded.getData() + 1)
	cRemaining.setData(cRemaining.getData() + 1)
	sstype()

def caddx(x):
	cAwarded.setData(x)
	cRemaining.setData(x)
	sstype()

def caddmorex(x):
	cAwarded.setData(cAwarded.getData() + x)
	cRemaining.setData(cRemaining.getData() + x)
	sstype()


#longtexts
#findSchool = LongTextbox(text="How did you hear about the school?", lang=language, repr='findSchool')
notes = LongTextbox(text="Notes", lang=language, repr='notes')


#ppicker
def ppicker():
	try:
		p = filedialog.askopenfile().name
		portr.config(path=p)
	except:
		return


#title bg
titlePic = Image.open('smallblu.jpg')
#titleImg = ImageTk.PhotoImage(titlePic)


#signs
ws = Photo(repr='ws', path='ws_sm.png')
hs = Photo(repr='hs', path='halt_sm.png')
cm = Photo(repr='cm', path='check_mark_sm.png')






bok = Buttonbox(text='ok', lang=language, repr='bok')
byes = Buttonbox(text='yes', lang=language, repr='byes')
bno = Buttonbox(text='no', lang=language, repr='bno')
bcancel = Buttonbox(text='Cancel', lang=language, repr='bcancel')

bok.width = 10
byes.width = 10
bno.width = 10
bcancel.width = 10


#importexp
imp = Labelbox(text='impdb', lang=language, repr='imp', bold=True)
impt = Labelbox(text='impt', lang=language, repr='impt', bold=True)
exp = Labelbox(text='expdb', lang=language, repr='exp', bold=True)
curfile = Labelbox(text='curfile', lang=language, repr='curfile', bold=True)
curdbs = Labelbox(text='', lang=language, repr='curdb')
saveto = Labelbox(text='saveto', lang=language, repr='saveto')

bimp = Buttonbox(text='impxls', lang=language, repr='bimp')
bimpt = Buttonbox(text='imptxls', lang=language, repr='bimpt')
bexp = Buttonbox(text='expxls', lang=language, repr='bexp')
bsav = Buttonbox(text='Save', lang=language, repr='bsav')
bcdb = Buttonbox(text='choosedb', lang=language, repr='bcdb')
bsalrep = Buttonbox(text='salrep', lang=language, repr='bsrep')

bk = Buttonbox(text='Back', lang=language, repr='bk')
nxt = Buttonbox(text='Next', lang=language, repr='bimp')


#browsebtn
brw = Buttonbox(text='browse', lang=language, repr='brw')
fpath = Textbox(text='filepath', lang=language, repr='fpath')
brw2 = Buttonbox(text='browse', lang=language, repr='brw2')
fpath2 = Textbox(text='filepath', lang=language, repr='fpath2')
brwp = Buttonbox(text='browsephoto', lang=language, repr='brwp')


#ebox
def nos(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='No student', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def noc(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	noctext = Labelbox(text='No classes', lang=lang, repr='noctext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(noctext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def con(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	context = Labelbox(text='Con student', lang=lang, repr='context')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(context, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bno.button.focus_set()

	t.root.wait_window()

	return t.z

def conS(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	constext = Labelbox(text='Con S student', lang=lang, repr='constext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(constext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)

	t.root.wait_window()

	return t.z

def ase(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	asetext = Labelbox(text='Ase student', lang=lang, repr='asetext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(asetext, (2, 0))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bno.button.focus_set()

	t.root.wait_window()

	return t.z

def sa(s, lang):


	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	t.frames["First Frame"].addWidget(cm, (0, 0))
	t.frames["Second Frame"].addWidget(bok, (4, 0))

	satext = Labelbox(text='Sa student', lang=lang, repr='satext')
	
	t.frames["First Frame"].addWidget(satext, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def cs(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Cs student', lang=lang, repr='cstext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def csout(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='cstext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def no_checkin_today(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	fimport = Labelbox(text='No Check-in today', lang=lang, repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(fimport, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def date_error(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Invalid Date', lang=lang, repr='invaliddate')
	breturn = Buttonbox(text='Return', lang=lang, repr='ok_')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(breturn, (2, 0))
	
	breturn.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

def invalid_path(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Invalid Path', lang={'Invalid Path': 'Invalid Path'}, repr='invaliddate')
	breturn = Buttonbox(text='Return', lang=lang, repr='ok_')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(breturn, (2, 0))
	
	breturn.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

def checkout_earlier_checkin(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	checkout_earlier_checkin_ = Labelbox(text='Check-Out Cannot be earlier than Check-In',
		lang=lang, 
		repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(checkout_earlier_checkin_, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def entry_not_found(lang, date):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	entry_not_found_ = Labelbox(text='No Check-In on that Date',
		lang=lang, 
		repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(entry_not_found_, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	entry_not_found_.label.config(text=entry_not_found_.label.cget('text') + ' ' + date)

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def deny_checkout_future(lang, date):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	entry_not_found_ = Labelbox(text='Cannot Check-In a future time',
		lang=lang, 
		repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(entry_not_found_, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	entry_not_found_.label.config(text=entry_not_found_.label.cget('text') + ' ' + date)

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def confirm_check_in_time(lang, database):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')

	timeslot = database.findTimeSlot(datetime.now())

	byes_current_time = Buttonbox(text='Check-in', lang=lang, repr='bok')
	byes_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='bnok')

	byes_current_time.width = 20
	byes_enter_time.width = 20

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes_current_time, (0, 0))
	t.frames["Second Frame"].addWidget(byes_enter_time, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes_current_time.selfframe.grid(sticky=E+W, padx=5)
	byes_enter_time.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes_current_time.config(cmd=lambda: return_(True))
	byes_enter_time.config(cmd=lambda: return_('manual'))
	bcancel.config(cmd=lambda: return_(False))
	byes_current_time_text = byes_current_time.button.cget('text')
	byes_current_time.button.config(
		text=byes_current_time_text + ' ' + timeslot)
	
	t.root.wait_window()

	return t.value

def time_entry(lang):

	def return_():
		time_input = hour_input_stringvar.get() + ':' + minute_input_stringvar.get() + ' ' + am_pm_stringvar.get()
		dt = datetime.strftime(datetime.strptime(time_input, '%I:%M %p'), '%I:%M %p')
		confirm_time.time_input_confirmed = dt
		confirm_time.destroy()

	confirm_time = Window(top=True)
	confirm_time.attributes('-fullscreen', False)
	confirm_time.resizable(0, 0)
	confirm_time.geometry('400x200+200+200')
	confirm_time.grab_set()
	confirm_time.focus_set()
	confirm_time.titleFrame.pack_forget()
	confirm_time.time_input_confirmed = False

	confirm_window = AppWindow(confirm_time.mainFrame)

	hour_input_stringvar = StringVar()
	minute_input_stringvar = StringVar()
	am_pm_stringvar = StringVar()
	hour_input_stringvar.set(datetime.strftime(datetime.now(), '%I'))
	minute_input_stringvar.set('00')
	am_pm_stringvar.set(datetime.strftime(datetime.now(), '%p'))
	return_button = Buttonbox(text='Confirm', lang=lang, repr='rbutton')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancelbutton')

	confirm_window.newFrame("First Frame", (0, 0))

	Label(confirm_window.frames["First Frame"], text=lang['Time']).grid(row=0, column=0, sticky=E)
	hour_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=hour_input_stringvar, width=3, state='readonly')
	hour_input.grid(row=0, column=1)
	minute_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=minute_input_stringvar, width=3, state='readonly')
	minute_input.grid(row=0, column=2)
	am_pm_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=am_pm_stringvar, width=3, state='readonly')
	am_pm_input.grid(row=0, column=3)
	confirm_window.frames["First Frame"].addWidget(return_button, (1, 0))
	confirm_window.frames["First Frame"].addWidget(cancel_button, (2, 0))

	hour_input['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	minute_input['values'] = ('00', '30')
	am_pm_input['values'] = ('AM', 'PM')

	return_button.selfframe.grid(columnspan=6, pady=(20, 0))
	cancel_button.selfframe.grid(columnspan=6)

	return_button.config(cmd=return_)
	cancel_button.config(cmd=confirm_time.destroy)

	confirm_time.wait_window()

	return confirm_time.time_input_confirmed

def confirm_overwrite_checkout(lang):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Checkout', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: return_(True), lang=lang)
	bno.config(cmd=lambda: return_(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.value

def confirm_overwrite_checkin(lang):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Overwrite Check-In', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: return_(True), lang=lang)
	bno.config(cmd=lambda: return_(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.value

def confirm_check_out_time(lang, database):

	def return_(value):
		t.value = value
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Check out prompt', lang=lang, repr='creset')
	
	timeslot = database.findTimeSlot(datetime.now())

	byes_current_time = Buttonbox(text='Check-out', lang=lang, repr='bok')
	byes_enter_time = Buttonbox(text='Yes, enter time', lang=lang, repr='bnok')

	byes_current_time.width = 20
	byes_enter_time.width = 20

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes_current_time, (0, 0))
	t.frames["Second Frame"].addWidget(byes_enter_time, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes_current_time.selfframe.grid(sticky=E+W, padx=5)
	byes_enter_time.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes_current_time.config(cmd=lambda: return_(True), lang=lang)
	byes_enter_time.config(cmd=lambda: return_('manual'), lang=lang)
	bcancel.config(cmd=lambda: return_(False), lang=lang)
	byes_current_time_text = byes_current_time.button.cget('text')
	byes_current_time.button.config(
		text=byes_current_time_text + ' ' + timeslot)

	t.root.wait_window()

	return t.value

def date_time_entry(lang):

	def return_():
		if date_input.getData() == '01/01/1900':
			date_error(lang)
			return
		time_input = hour_input_stringvar.get() + ':' + minute_input_stringvar.get() + ' ' + am_pm_stringvar.get()
		dt = datetime.strftime(datetime.strptime(time_input, '%I:%M %p'), '%I:%M %p')
		confirm_time.time_input_confirmed = dt
		confirm_time.date_input = date_input.getData()
		confirm_time.destroy()

	confirm_time = Window(top=True)
	confirm_time.attributes('-fullscreen', False)
	confirm_time.resizable(0, 0)
	confirm_time.geometry('400x200+200+200')
	confirm_time.grab_set()
	confirm_time.focus_set()
	confirm_time.titleFrame.pack_forget()
	confirm_time.date_input = False
	confirm_time.time_input_confirmed = False

	confirm_window = AppWindow(confirm_time.mainFrame)

	date_input = Datebox(text='Date', lang=lang, repr='dateinput')
	hour_input_stringvar = StringVar()
	minute_input_stringvar = StringVar()
	am_pm_stringvar = StringVar()
	hour_input_stringvar.set(datetime.strftime(datetime.now(), '%I'))
	minute_input_stringvar.set('00')
	am_pm_stringvar.set(datetime.strftime(datetime.now(), '%p'))
	return_button = Buttonbox(text='Confirm', lang=lang, repr='rbutton')
	cancel_button = Buttonbox(text='Cancel', lang=lang, repr='cancelbutton')

	confirm_window.newFrame("First Frame", (0, 0))

	confirm_window.frames["First Frame"].addWidget(date_input, (0, 0))
	Label(confirm_window.frames["First Frame"], text=lang['Time']).grid(row=1, column=0, sticky=E)
	hour_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=hour_input_stringvar, width=2, state='readonly')
	hour_input.grid(row=1, column=1)
	minute_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=minute_input_stringvar, width=2, state='readonly')
	minute_input.grid(row=1, column=2)
	am_pm_input = ttk.Combobox(
		confirm_window.frames["First Frame"],
		textvariable=am_pm_stringvar, width=3, state='readonly')
	am_pm_input.grid(row=1, column=3, padx=(2, 0))
	confirm_window.frames["First Frame"].addWidget(return_button, (2, 0))
	confirm_window.frames["First Frame"].addWidget(cancel_button, (3, 0))

	hour_input['values'] = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
	minute_input['values'] = ('00', '30')
	am_pm_input['values'] = ('AM', 'PM')

	return_button.selfframe.grid(columnspan=6, pady=(20, 0))
	cancel_button.selfframe.grid(columnspan=6)
	date_input.label.config(width=11)
	date_input.selfframe.grid(columnspan=7, pady=15)

	return_button.config(cmd=return_)
	cancel_button.config(cmd=confirm_time.destroy)

	confirm_time.titleFrame.pack_forget()

	confirm_time.wait_window()

	return confirm_time.date_input, confirm_time.time_input_confirmed

	'''
	try:
		cdt = datetime.now()
		time = '{:%I:%M %p}'.format(cdt)
		date = window_.date_input
		data = [date, time, window_.time_input_confirmed, '', '', database.school]
		#print(data)

		s = database.studentList[bCodeNE.getData()].datapoints
		
		slot = []
		for slot_ in s['attinfo'][1]:
			if slot_[0] == date:
				slot.append(slot_)
				break

		print(slot)
		if len(slot) == 0: return

		s['attinfo'] = list(s['attinfo'])
		s['attinfo'][0] = ['Date', 'Check-In Time', 'Start Time', 'Check-Out Time', 'Confirm Time']
		slot[0][3] = time
		slot[0][4] = window_.time_input_confirmed
	except AttributeError:
		return
	print('out', window_.time_input_confirmed)
	database.saveData()

	att_info = database.studentList[window_.student_id].datapoints['attinfo']
	headers = att_info[0]
	last_check_in = [att_info[1][-1]]
	print(last_check_in)
	data_points = database.studentList[window_.student_id].datapoints
	window_.attinfo.setData([data_points['attinfo'][0], [data_points['attinfo'][1][-1]]])

	sby.b.set(sby.rads[0][1]) #reset Scan By to Barcode
	window_.attinfo.canvas.yview_moveto(1.0) #scroll to bottom
	'''

def confirm_print(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Con print', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def print_succesful(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Print Successful', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

	return t.z

def teacher_report_print_successful(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Teacher Print Successful', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

	return t.z

def confirm_check_in(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Confirm late check-in', lang=lang, repr='cprint')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	byes.button.focus_set()

	t.root.wait_window()

	return t.z

def confirm_reset(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	cstext = Labelbox(text='Confirm Reset', lang=lang, repr='creset')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(cstext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))
	t.frames["Second Frame"].addWidget(bcancel, (0, 2))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	bcancel.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bcancel.config(cmd=lambda: d('cancel'), lang=lang)

	t.root.wait_window()

	return t.z

def reset_confirmation(lang, value):

	if value != True: return

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	dbupdate = Labelbox(text='Early Check-ins have been reset', lang=lang, repr='dbupdate')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(dbupdate, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def choose_school(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	t.root.overrideredirect(0)
	t.root.protocol('WM_DELETE_WINDOW', lambda: False)

	t.newFrame("First Frame", (0, 0))

	cstext = Labelbox(text='Choose School', lang=lang, repr='creset')


	button_brooklyn = Buttonbox(text='Brooklyn', lang=lang, repr='bk')
	button_elmhurst = Buttonbox(text='Elmhurst', lang=lang, repr='el')
	button_flushing = Buttonbox(text='Flushing', lang=lang, repr='flu')
	button_chinatown = Buttonbox(text='Chinatown', lang=lang, repr='ct')


	t.frames["First Frame"].addWidget(button_flushing, (0, 0))
	t.frames["First Frame"].addWidget(button_chinatown, (1, 0))
	t.frames["First Frame"].addWidget(button_elmhurst, (2, 0))
	t.frames["First Frame"].addWidget(button_brooklyn, (3, 0))
	t.frames["First Frame"].addWidget(bcancel, (4, 0))

	button_brooklyn.config(cmd=lambda: d('Brooklyn'), lang=lang)
	button_elmhurst.config(cmd=lambda: d('Elmhurst'), lang=lang)
	button_flushing.config(cmd=lambda: d('Flushing'), lang=lang)
	button_chinatown.config(cmd=lambda: d('Chinatown'), lang=lang)
	bcancel.config(cmd=lambda: d('cancel'), lang=lang)

	t.root.wait_window()

	print(t.z)
	return t.z

def create_new_db(lang, d):

	def get_return(z):
		t.z = z
		t.db_file = db_file_textbox.getData()
		t.pw_file = pw_file_textbox.getData()
		t.pw = pw_textbox.getData()
		t.dw()

	def set_file(file_):
		f_path = filedialog.askdirectory()
		print(f_path + '/' + db_file_textbox.getData())
		if file_ == 'db_file':
			db_file_textbox.setData(f_path + '/' + db_file_textbox.getData() + '.rybdb')
		elif file_ == 'pw_file':
			pw_file_textbox.setData(f_path + '/' + pw_file_textbox.getData() + '.rybdb')
		
		return


	t = Mbox()
	#t.root.overrideredirect(0)
	#t.root.attributes(toolwindow=1)

	t.newFrame("First Frame", (0, 0))


	db_file_textbox = Textbox(text='Database File', lang={'Database File': 'Database File'}, repr='db_file')
	pw_file_textbox = Textbox(text='Password File', lang={'Password File': 'Password File'}, repr='pw_file')
	pw_textbox = Textbox(text='Password', lang={'Password': 'Password'}, repr='pw')

	brw1 = Buttonbox(text='browse', lang=language, repr='brw1')
	brw2 = Buttonbox(text='browse', lang=language, repr='brw2')
	
	t.frames["First Frame"].addWidget(db_file_textbox,(0, 0))
	t.frames["First Frame"].addWidget(pw_file_textbox,(1, 0))
	t.frames["First Frame"].addWidget(brw1, (0, 2))
	t.frames["First Frame"].addWidget(brw2, (1, 2))
	t.frames["First Frame"].addWidget(pw_textbox, (3, 0))
	t.frames["First Frame"].addWidget(bsav, (4, 1))
	t.frames["First Frame"].addWidget(bcancel, (5, 1))


	db_file_textbox.label.config(width=12)
	pw_file_textbox.label.config(width=12)
	pw_textbox.label.config(width=12)
	brw1.button.config(width=7)
	brw2.button.config(width=7)
	bsav.button.config(width=22)

	brw1.config(cmd=lambda: set_file('db_file'))
	brw2.config(cmd=lambda: set_file('pw_file'))
	bsav.config(cmd=lambda: get_return('success'))
	bcancel.config(cmd=lambda: get_return('cancel'), lang=lang)



	t.root.wait_window()

	if t.z == 'cancel':
		return

	if len(t.pw.strip()) == 0 or len(t.db_file.strip()) == 0 or len(t.pw_file.strip()) == 0:
		return

	if not (os.path.exists(os.path.dirname(t.pw_file)) and os.path.exists(os.path.dirname(t.db_file))):
		print('invalid paths')
		return

	key = str.encode(t.pw)

	if len(key) != 16 and len(key) != 24 and len(key) != 32:
		print('failed')
		return

	studentList = {}
	cipher = AES.new(key, AES.MODE_CFB, d.iv)
	binary_string = pickle.dumps(studentList)
	encrypted = cipher.encrypt(binary_string)

	f = open(t.db_file, 'wb')
	f.write(bytearray(encrypted))
	f.close()

	f = open(t.pw_file, 'wb')
	f.write(bytearray(str.encode(t.pw)))
	f.close()

	print(t.z)

def convert_to_encrypted(lang, d):

	def get_return(z):
		t.z = z
		t.to_encrypt_file = to_encrypt_file_textbox.getData()
		t.db_file = db_file_textbox.getData()
		t.pw_file = pw_file_textbox.getData()
		t.pw = pw_textbox.getData()
		t.dw()

	def set_file(file_):
		if file_ == 'db_file':
			f_path = filedialog.askdirectory()
			db_file_textbox.setData(f_path + '/' + db_file_textbox.getData() + '.rybdb')
		elif file_ == 'pw_file':
			f_path = filedialog.askdirectory()
			pw_file_textbox.setData(f_path + '/' + pw_file_textbox.getData() + '.rybdb')
		elif file_ == 'to_enc_file':
			f_path = filedialog.askopenfile()
			if f_path == None: return
			to_encrypt_file_textbox.setData(f_path.name)

		return


	t = Mbox()
	#t.root.overrideredirect(0)
	#t.root.bind("<Destroy>", lambda event: None)

	t.newFrame("First Frame", (0, 0))


	to_encrypt_file_textbox = Textbox(text='Unencrypted File', lang={'Unencrypted File': 'Unencrypted File'}, repr='unc_db_file')
	db_file_textbox = Textbox(text='Encrypt File To', lang={'Encrypt File To': 'Encrypt File To'}, repr='db_file')
	pw_file_textbox = Textbox(text='Password File', lang={'Password File': 'Password File'}, repr='pw_file')
	pw_textbox = Textbox(text='Password', lang={'Password': 'Password'}, repr='pw')

	brw1 = Buttonbox(text='browse', lang=language, repr='brw1')
	brw2 = Buttonbox(text='browse', lang=language, repr='brw2')
	brw3 = Buttonbox(text='browse', lang=language, repr='brw3')

	t.frames["First Frame"].addWidget(to_encrypt_file_textbox, (0, 0))
	t.frames["First Frame"].addWidget(db_file_textbox,(1, 0))
	t.frames["First Frame"].addWidget(pw_file_textbox,(2, 0))
	t.frames["First Frame"].addWidget(brw3, (0, 2))
	t.frames["First Frame"].addWidget(brw1, (1, 2))
	t.frames["First Frame"].addWidget(brw2, (2, 2))
	t.frames["First Frame"].addWidget(pw_textbox, (3, 0))
	t.frames["First Frame"].addWidget(bsav, (4, 1))
	t.frames["First Frame"].addWidget(bcancel, (5, 1))


	db_file_textbox.label.config(width=12)
	pw_file_textbox.label.config(width=12)
	to_encrypt_file_textbox.config(width=12)
	pw_textbox.label.config(width=12)
	brw1.button.config(width=7)
	brw2.button.config(width=7)
	brw3.button.config(width=7)
	bsav.button.config(width=22)

	brw1.config(cmd=lambda: set_file('db_file'))
	brw2.config(cmd=lambda: set_file('pw_file'))
	brw3.config(cmd=lambda: set_file('to_enc_file'))
	bsav.config(cmd=lambda: get_return('success'))
	bcancel.config(cmd=lambda: get_return('cancel'), lang=lang)



	t.root.wait_window()

	if t.z == 'cancel':
		return

	key = str.encode(t.pw)
	studentList = pickle.load(open(t.to_encrypt_file, 'rb'))
	cipher = AES.new(key, AES.MODE_CFB, d.iv)
	binary_string = pickle.dumps(studentList)
	encrypted = cipher.encrypt(binary_string)

	f = open(t.db_file, 'wb')
	f.write(bytearray(encrypted))
	f.close()

	f = open(t.pw_file, 'wb')
	f.write(bytearray(str.encode(t.pw)))
	f.close()

	print(t.z)

def password_prompt(lang, reset_pw):

	def get_return(z):
		if z == 'pw_mismatch':
			return
		t.z = z
		t.dw()

	t = Mbox()
	#t.root.overrideredirect(0)

	t.newFrame("Top Frame", (0, 0))
	t.newFrame("First Frame", (1, 0))
	t.newFrame("Second Frame", (2, 0))

	no_pw_detected = Labelbox(text="no_pw_set_pw", lang=lang, repr='nopwsetpw')
	old_pw_textbox = Textbox(text="Old Password", lang={"Old Password": "Old Password"}, repr='oldpwtextbox')
	new_pw_textbox = Textbox(text="New Password", lang={"New Password": "New Password"}, repr='newpwtextbox')
	retype_new_pw_textbox = Textbox(text="Retype New Password", lang={"Retype New Password": "Retype New Password"}, repr='retypenewpwtextbox')
	pw_textbox = Textbox(text="Password", lang={"Password": "Password"}, repr='oldpwtextbox')

	if reset_pw:
		t.frames["Top Frame"].addWidget(no_pw_detected, (0, 0))
		t.frames["First Frame"].addWidget(old_pw_textbox, (1, 0))
		t.frames["First Frame"].addWidget(new_pw_textbox, (2, 0))
		t.frames["First Frame"].addWidget(retype_new_pw_textbox, (3, 0))
		t.frames["Second Frame"].addWidget(bsav, (0, 1))
		bsav.config(cmd=lambda: get_return((old_pw_textbox.getData(), new_pw_textbox.getData())) if new_pw_textbox.getData() == retype_new_pw_textbox.getData() else get_return('pw_mismatch'))
		bsav.button.config(width=10)
		old_pw_textbox.label.config(width=19)
		new_pw_textbox.label.config(width=19)
		retype_new_pw_textbox.label.config(width=19)
	else:
		t.frames["First Frame"].addWidget(pw_textbox, (0, 0))
		t.frames["Second Frame"].addWidget(bok, (0, 1))
		bok.config(cmd=lambda: get_return(pw_textbox.getData()))
		bok.button.config(width=10)

	t.frames["Second Frame"].addWidget(bcancel, (0, 0))

	bcancel.button.config(width=10)
	
	bcancel.config(cmd=lambda: get_return('cancel'))


	t.root.wait_window()

	return t.z

def pw_reset_confirm(lang):

	t = Mbox()
	t.root.overrideredirect(0)
	
	t.newFrame("First Frame", (0, 0))

	t.frames["First Frame"].addWidget(bok, (1, 0))

	confirmed_reset = Labelbox(text='confirmed reset', lang=lang, repr='confirmedreset')

	t.frames["First Frame"].addWidget(confirmed_reset, (0, 0))
	t.frames["First Frame"].addWidget(bok, (1, 0))

	bok.config(cmd=t.dw)

	t.root.wait_window()

	return

def wrong_password(lang):

	t = Mbox()
	t.root.overrideredirect(0)
	
	t.newFrame("First Frame", (0, 0))

	wrong_pw_label = Labelbox(text='wrong password try again', lang=lang, repr='wrongpwtryagain')

	t.frames["First Frame"].addWidget(wrong_pw_label, (0, 0))
	t.frames["First Frame"].addWidget(bok, (1, 0))

	bok.config(cmd=t.dw)

	t.root.wait_window()

	return

def create_new_markerfile(lang):

	def get_return(z):
		t.z = z
		t.marker_file = marker_file_textbox.getData()
		t.dw()

	def set_file(file_):
		f_path = filedialog.askdirectory()
		if file_ == 'marker_file':
			marker_file_textbox.setData(f_path + '/' + marker_file_textbox.getData() + '.rybdb')

		return


	t = Mbox()
	#t.root.overrideredirect(0)
	#t.root.bind("<Destroy>", lambda event: None)

	t.newFrame("First Frame", (0, 0))


	marker_file_textbox = Textbox(text='Marker File', lang={'Marker File': 'Marker File'}, repr='marker_file')
	
	brw3 = Buttonbox(text='browse', lang=language, repr='brw3')

	t.frames["First Frame"].addWidget(marker_file_textbox,(2, 0))
	t.frames["First Frame"].addWidget(brw3,(2, 2))
	t.frames["First Frame"].addWidget(bsav, (4, 1))
	t.frames["First Frame"].addWidget(bcancel, (5, 1))


	marker_file_textbox.label.config(width=12)
	brw3.button.config(width=7)
	bsav.button.config(width=22)

	brw3.config(cmd=lambda: set_file('marker_file'))
	bsav.config(cmd=lambda: get_return('success'))
	bcancel.config(cmd=lambda: get_return('cancel'), lang=lang)



	t.root.wait_window()

	if t.z == 'cancel':
		return

	if t.marker_file.strip() != "":
		pickle.dump({}, open(t.marker_file, "wb"))

	print(t.z)

def ret(s, lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()

	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	rettext = Labelbox(text='Ret to Main', lang=lang, repr='rettext')

	t.frames["First Frame"].addWidget(hs, (1, 0))
	t.frames["First Frame"].addWidget(rettext, (2, 0))
	t.frames["Second Frame"].addWidget(byes, (0, 0))
	t.frames["Second Frame"].addWidget(bno, (0, 1))

	byes.selfframe.grid(sticky=E+W, padx=5)
	bno.selfframe.grid(sticky=E+W, padx=5)
	byes.config(cmd=lambda: d(True), lang=lang)
	bno.config(cmd=lambda: d(False), lang=lang)
	bno.button.focus_set()

	t.root.wait_window()

	return t.z

def dbs(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	dbupdate = Labelbox(text='Database succesfully updated!', lang=lang, repr='dbupdate')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(dbupdate, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def noimp(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	fimport = Labelbox(text='File could not be imported', lang=lang, repr='fimport')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(fimport, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def pchoosefile(lang):

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	pchoosefiletext = Labelbox(text='Please choose a file', lang=lang, repr='pchoosefiletext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(pchoosefiletext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))

	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

def ctimp(lang, simp, timp):

	t = Mbox()
	
	t.newFrame("Im Frame", (0, 0))
	t.newFrame("First Frame", (1, 0))
	t.newFrame("Second Frame", (2, 0))

	fimport = Labelbox(text='Import succesful', lang=lang, repr='fimport')
	simport = Labelbox(text='Students imported: ', lang=lang, repr='simport')
	timport = Labelbox(text='Attendance data imported: ', lang=lang, repr='timport')

	Label(t.frames["First Frame"], text=simp, anchor=E).grid(row=2, column=3)
	Label(t.frames["First Frame"], text=timp, anchor=E).grid(row=3, column=3)

	t.frames["Im Frame"].addWidget(cm, (0, 0))
	t.frames["First Frame"].addWidget(fimport, (1, 0))
	t.frames["First Frame"].addWidget(simport, (2, 0))
	t.frames["First Frame"].addWidget(timport, (3, 0))
	t.frames["Second Frame"].addWidget(bok, (4, 0))
	
	cm.label.grid(columnspan=2)
	fimport.label.grid(columnspan=2)
	simport.label.grid(columnspan=2, sticky=W)
	timport.label.grid(columnspan=2, sticky=W)
	bok.button.grid(columnspan=2)
	bok.config(cmd=t.dw, lang=lang)

	t.root.wait_window()

#renew classes button
def renew(lang):
	def retC():
		w.ret = w.renClass.getData()
		t.destroy()

	t = Window(top=True)
	t.attributes('-fullscreen', False)
	t.geometry('400x300')

	w = AppWindow(t.mainFrame)

	w.lang = lang

	w.ret = 0

	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))

	w.renClass = IntTextbox(text="Number of classes", lang=w.lang, repr='renClass')
	w.bok = Buttonbox(text='ok', lang=w.lang, repr='bok')
	w.bcan = Buttonbox(text='Cancel', lang=w.lang, repr='bcan')
	w.bok.width = 10
	w.bcan.width = 10

	w.frames["First Frame"].addWidget(w.renClass, (0, 0))
	w.frames["Second Frame"].addWidget(w.bok, (0, 0))
	w.frames["Second Frame"].addWidget(w.bcan, (0, 1))

	w.bok.config(cmd=retC)
	w.bcan.config(cmd=t.destroy)

	w.bok.selfframe.grid(sticky=E+W, padx=5)
	w.bcan.selfframe.grid(sticky=E+W, padx=5)
	t.bind('<Return>', lambda e: retC())
	t.bind('<Escape>', lambda e: t.destroy())


	t.grab_set()
	t.focus_set()

	t.wait_window()

	return w.ret

def database_backup_successful(lang):

	def d(z):
		t.z = z
		t.dw()

	t = Mbox()
	
	t.newFrame("First Frame", (0, 0))
	t.newFrame("Second Frame", (1, 0))

	nostext = Labelbox(text='Database Backup Successful', lang=lang, repr='nostext')

	t.frames["First Frame"].addWidget(ws, (0, 0))
	t.frames["First Frame"].addWidget(nostext, (1, 0))
	t.frames["Second Frame"].addWidget(bok, (2, 0))
	
	bok.config(cmd=lambda: d(True), lang=lang)

	t.root.wait_window()

	return t.z

#clang
def clang():
		if w.lang['self'] == 'english':
			w.lang = languages['chinese']
		else:
			w.lang = languages['english']
		for frame in w.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=w.lang)


#bclang
bclang = Buttonbox(text='changelanguage', lang=language, repr='bclang')


#Search
bsearch = Buttonbox(text='Search', lang=language, repr='bsearch')