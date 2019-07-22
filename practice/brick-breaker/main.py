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
	global ball, border_top, border_bottom, border_left, border_right
	if event.char and event.char.encode("UTF-8")[0] == 27:
		if interval.running:
			interval.cancel()
		del ball, border_top, border_bottom, border_left, border_right
		wnd.destroy()

__gameStarted = False
def startGame(event):
	global interval, wnd, canv
	global ball
	ball.setv((geo.Point(event.x, event.y) - ball.particle.pos).unit() * ballSpeed)
	# print(ball.particle.vel)
	interval.start()
	pass

def keyEventHandler(event):
	# print(event.char.encode("UTF-8")[0])
	exitOnEscapeKey(event)

def leftReleaseHandler(event):
	global __gameStarted
	if not __gameStarted:
		startGame(event)
		__gameStarted = True
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
	global ball, border_top, border_bottom, border_left, border_right
	border_top.helpColli(ball)
	border_bottom.helpColli(ball)
	border_left.helpColli(ball)
	border_right.helpColli(ball)
	ball.resolveColli()
	ball.move()
	pass

def main():
	global canv, wnd, interval
	global ball, border_top, border_bottom, border_left, border_right
	global screenDm
	wnd = newwindow(title = "{{BREAKOUT}}", size = windowDm)
	screenDm = (wnd.winfo_screenwidth(), wnd.winfo_screenheight())
	wnd.geometry(sizetostr(windowDm, ((screenDm[0] - windowDm[0]) // 2, (screenDm[1] - windowDm[1]) // 2)))
	wnd.bind("<Key>", keyEventHandler)
	wnd.bind("<ButtonRelease-1>", leftReleaseHandler)
	wnd.bind("<Motion>", cursorMotionHandler)
	canv = TK.Canvas(wnd, width = windowDm[0], height = windowDm[1])
	canv.pack()
	ball = ele.Circle(canv, windowDm[0] / 2, windowDm[1] / 2 + 180, 10)
	canv.itemconfig(ball.circle, **ballCanvOptions)
	border_top = ele.StaticRectangle(canv, windowDm[0] / 2, borderHeightTopBottom / 2, windowDm[0], borderHeightTopBottom)
	border_bottom = ele.StaticRectangle(canv, windowDm[0] / 2, windowDm[1]  - borderHeightTopBottom / 2, windowDm[0], borderHeightTopBottom)
	border_left = ele.Circle(canv, windowDm[0] / 2 - borderOffsetLeftRight - math.sqrt(borderRadiusLeftRight ** 2 - (windowDm[1] / 2 - borderHeightTopBottom) ** 2), windowDm[1] / 2, borderRadiusLeftRight)
	border_right = ele.Circle(canv, windowDm[0] / 2 + borderOffsetLeftRight + math.sqrt(borderRadiusLeftRight ** 2 - (windowDm[1] / 2 - borderHeightTopBottom) ** 2), windowDm[1] / 2, borderRadiusLeftRight)
	canv.itemconfig(border_top.rect, **borderCommonCanvOptions)
	canv.itemconfig(border_bottom.rect, **borderCommonCanvOptions)
	canv.itemconfig(border_left.circle, **borderCommonCanvOptions)
	canv.itemconfig(border_right.circle, **borderCommonCanvOptions)
	interval = itv4.Interval(intervalContent, 1 / targetRate, fixed = True, xsafe = True, xsafeFun = backupIntervalContent)
	return 0

if __name__ == "__main__":
	main()
	wnd.mainloop()
