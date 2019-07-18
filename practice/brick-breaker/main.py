#!/usr/bin/python3
import turtle
import random
import tkinter as TK
import math
import intervals3 as itv3
from globalVars import *

def sizetostr(size,pos):
	return str(int(size[0]))+"x"+str(int(size[1]))+"+"+str(int(pos[0]))+"+"+str(int(pos[1]))

randerlib="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#*"
def rander(a=3,b=4,confirm=False):
	res=""
	for i in range(a):
		if i!=0:
			res+="-"
		cur=""
		num=0
		for j in range(b):
			i=random.randint(0,len(randerlib)-1)
			cur+=randerlib[i]
			num=num^i
		if confirm:
			cur+=randerlib[num]
		res+=cur
	return res

def newwindow(title=None,size=(200,200),pos=(100,100)):
	wn=TK.Tk()
	wn.geometry(sizetostr(size,pos))
	if title==None:
		title=rander()
	wn.title(title)
	return wn

def exitOnEscapeKey(event):
	global wnd
	if event.char and event.char.encode("UTF-8")[0] == 27:
		wnd.destroy()

def keyEventHandler(event):
	print(event.char.encode("UTF-8")[0])
	exitOnEscapeKey(event)

def leftClickHandler(event):
	pass

def cursorMotionHandler(event):
	pass

def main():
	global canv, wnd
	global ball, bricks, board, box
	wnd = newwindow(title = "Practice", size = windowDm)
	wnd.bind("<Key>", keyEventHandler)
	wnd.bind("<ButtonRelease-1>", leftClickHandler)
	wnd.bind("<Motion>", cursorMotionHandler)
	canv = TK.Canvas(wnd, width = windowDm[0], height = windowDm[1])
	canv.pack()

	return 0

if __name__ == "__main__":
	main()
	wnd.mainloop()
