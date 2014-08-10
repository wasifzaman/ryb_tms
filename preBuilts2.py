from labelWidgets2 import *
from tableWidget2 import *
from photoWidget2 import *
from languages import *
from mbox2 import *
from tkinter import filedialog

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


#student table
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



#photo
portr = Photo(repr='portr', path='monet_sm.jpg')


#separator
sepr = Separator(repr='sepr')


#scan
sby = Picker(repr='sby', text=language['Search By'], rads=[(language['Barcode'], 'bCode'), \
	(language['First Name'], 'firstName'), \
	(language['Last Name'], 'lastName'), \
	(language['Chinese Name'], 'chineseName'), \
	(language['Phone Number'], 'phoneNumber'), \
	(language['Date of Birth'], 'dob')])


#info titles
sinfo = Labelbox(text='Student information', lang=language, repr='sinfo')
ainfo = Labelbox(text='Address information', lang=language, repr='ainfo')
cinfo = Labelbox(text='Contact information', lang=language, repr='cinfo')
pinfo = Labelbox(text='Payment information', lang=language, repr='pinfo')
ninfo = Labelbox(text='Notes', lang=language, repr='ninfo')


#spicker
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


#spicker
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

bok.width = 10
byes.width = 10
bno.width = 10


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