#!/usr/bin/python

from Tkinter import *
from tkFileDialog import *
import optparse
import os

home = os.getenv("HOME")

def proname():
	projcache = open(home+'/.cache/C/project','r')
	a=0
	b=0
	c=[]
	d=projcache.read()
	e=len(d)
	while a<e:
		f=d[a:a+1]
		if f != '/':
			c[b:b+1]=f
			b +=1
		else :
			c=[]
		a +=1
	g=0
	h=len(c)-2
	i=[]
	while g<h:
		i[g:g+1]=c[g:g+1]
		g +=1
	j=0
	k=[]
	while j<e-2:
		k[j:j+1]=d[j:j+1]
		j +=1
	l=0
	m=len(c)
	n=[]
	while l<e-m:
		n[l:l+1]=d[l:l+1]
		l +=1

	return "".join(i),"".join(c),"".join(k),"".join(n),d

def build():
	
	builcm = 'gcc '+names[4]+' -o '+names[2]
	bugs = 'gnome-terminal -- bash echo {[ C compilator ]} ;echo [+] Project : '+names[0]+';echo  ;cd '+names[3]+'; '+builcm+';echo   ;echo   ;echo building done;echo  press any key to exit;read;exit'
	os.system(bugs)


def run():
	w = 'gnome-terminal -- bash echo {[ C compilator ]} ;echo [+] Project : '+names[0]+';echo  ;cd '+names[3]+';./'+names[0]+';echo   ;echo   ;echo  press any key to exit;read;exit'
	os.system(w)	

def save(arg=0):
	projcache = open(home+'/.cache/C/project','r') 
	projectfile = open(projcache.read(),'w')
	projectfile.write(ent.get("1.0",END))					      			# Write the code in the file
	projectfile.close()

def openC(path):
	cfile = open(path,'r')
	ent.insert(INSERT,cfile.read())

def openf():
	filename = askopenfilename(parent=fen, defaultextension=".c")   #file=user choice
	if filename is None :						#if no choice , go back
		return
	fileload = open(filename, 'r')				        # Open the file
	ent.insert(INSERT,fileload.read())			        # Write the car in the text wid 

names = proname()
fen = Tk()						                # The window
fen.title(names[0])
fen.geometry('700x650')
menubar = Menu(fen)

# icons
imgrun = PhotoImage(file='icons/run.png')
imgopen = PhotoImage(file='icons/open.png')
imgnew = PhotoImage(file='icons/new.png')
imgsave = PhotoImage(file='icons/save.png')
imgbuild = PhotoImage(file='icons/build.png')
imgclose = PhotoImage(file='icons/close.png')

#menu bar
#menubar.add_command(image=imgnew)
menubar.add_command(image=imgopen , command=openf)
menubar.add_command(image=imgsave , command=save)
menubar.add_command(image=imgbuild, command=build)
menubar.add_command(image=imgrun  , command=run)
menubar.add_command(image=imgclose, command=fen.quit)

fen.config(menu=menubar)

frm = Frame(fen)
frm.pack(fill="both", expand=True)
frm.grid_propagate(False)
frm.grid_rowconfigure(0, weight=1)
frm.grid_columnconfigure(0, weight=1)

ent = Text(frm, borderwidth=3, relief="sunken")
ent.config(font=("consolas", 12), undo=True, wrap='word')
ent.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
ent.bind("<Control-Key-s>", save)					#ctrl+s/S -> save/creat a file
ent.bind("<Control-Key-S>", save)				        # just in case caps lock is on

scrollb = Scrollbar(frm, command=ent.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
ent['yscrollcommand'] = scrollb.set

bugcache = open('/home/agentt/.cache/C/bugs','r+')
cnsl = Label(frm, bg="black", fg="white")
cnsl.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)

parser = optparse.OptionParser("usage %prog " + "-f <.c> ")
parser.add_option('-f', dest = 'filepath', type='string', help='the .c path')
(options, arg) = parser.parse_args()
if (options.filepath != None):
	openC(options.filepath)

fen.mainloop()
