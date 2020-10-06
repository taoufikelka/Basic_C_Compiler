#!/usr/bin/python

from tkinter import *
from tkinter import filedialog
import os

home = os.getenv("HOME")
mainpath = home+"/.cache/C"
path1 = home+"/.cache/C/projects"
path2 = home+"/.cache/C/project"
path3 = home+"/.cache/C/bugs"

if os.path.exists(mainpath) == False :
	os.system('mkdir '+mainpath+"; touch "+path1+" "+path2+" "+path3)
else :
	None

def creat():
	projectpath = filedialog.asksaveasfilename(parent=win, defaultextension=".c")   			#file=user choice
	if projectpath is None :			  		      			#if no choice , go back
		return
	procache = open(path1,'a')
	curcache = open(path2,'w')
	curcache.write(projectpath)
	curcache.close()
	procache.write(projectpath+'\n')
	procache.close()
	win.quit
	os.system('python C.py')

def copen():
	filename = filedialog.askopenfilename(parent=win, defaultextension=".c")   #file=user choice
	if filename is None :						#if no choice , go back
		return
	procache = open(path1,'a')
	curcache = open(path2,'w')
	curcache.write(filename)
	curcache.close()
	procache.write(filename+'\n')
	procache.close()
	os.system('python C.py -f '+filename)

win = Tk()
win.title('Ccompilator')
win.geometry('300x250')

imgopen = PhotoImage(file='icons/openf.png')
imgcreate = PhotoImage(file='icons/create.png')

butcreat = Button(win,compound=LEFT, text='Create new project', image=imgcreate, command=creat)
butcreat.pack()
butopen = Button(win,compound=LEFT, text=' Open old project  ', image=imgopen, command=copen)
butopen.pack()

win.mainloop()
