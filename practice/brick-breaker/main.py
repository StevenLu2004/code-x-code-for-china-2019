#!/usr/bin/python3
import random
import tkinter as TK
import math
import intervals4 as itv4
from globalVars import *
import gameElements as ele
import gameGeometry as geo
import gamePhysics as phys

def sizetostr(size, pos = None):
	if pos == None:
		return "{}x{}".format(size[0], size[1])
	return "{}x{}+{}+{}".format(size[0], size[1], pos[0], pos[1])

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
	global wnd, interval
	global ball, border_top, border_bottom
	del ball, border_top, border_bottom
	if event.char and event.char.encode("UTF-8")[0] == 27:
		if interval.running:
			interval.cancel()
		wnd.destroy()

__gameStarted = False
def startGame(event):
	global interval, wnd, canv
	global ball
	ball.setv((geo.Point(event.x, event.y) - ball.particle.pos).unit() * ballSpeed)
	print(ball.particle.vel)
	canv.itemconfig(ball.circle, fill = "#33ff99", state = "normal")
	interval.start()
	pass

def keyEventHandler(event):
	# print(event.char.encode("UTF-8")[0])
	exitOnEscapeKey(event)

def leftReleaseHandler(event):
	if not __gameStarted:
		startGame(event)
	pass

def cursorMotionHandler(event):
	pass

def updateCanvas():
	global ball
	ball.updateDrawing()
	# print(ball.filledCircle.center)

def intervalContent():
	backupIntervalContent()
	updateCanvas()
	pass

def backupIntervalContent():
	global ball, border_top, border_bottom
	if border_top.helpColli(ball) or border_bottom.helpColli(ball):
		print("Collide!")
	ball.resolveColli()
	ball.move()
	pass

def main():
	global canv, wnd, interval
	global ball, border_top, border_bottom
	wnd = newwindow(title = "Practice", size = windowDm)
	wnd.bind("<Key>", keyEventHandler)
	wnd.bind("<ButtonRelease-1>", leftReleaseHandler)
	wnd.bind("<Motion>", cursorMotionHandler)
	canv = TK.Canvas(wnd, width = windowDm[0], height = windowDm[1])
	canv.pack()
	ball = ele.Circle(canv, windowDm[0] / 2, windowDm[1] / 2 + 180, 10)
	border_top = ele.StaticRectangle(canv, windowDm[0] / 2, -5, windowDm[0], 10)
	border_bottom = ele.StaticRectangle(canv, windowDm[0] / 2, -5, windowDm[0], 10)
	interval = itv4.Interval(intervalContent, 1 / targetRate, fixed = True, xsafe = True, xsafeFun = backupIntervalContent)
	return 0

if __name__ == "__main__":
	main()
	wnd.mainloop()
