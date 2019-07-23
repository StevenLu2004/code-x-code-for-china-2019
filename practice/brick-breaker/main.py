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
	wn.resizable(0, 0)
	return wn

__gameStarted = False
keyDowns = []

def movePaddlesToCursorX(x):
	global paddle_top, paddle_bottom, keyDowns
	if not "Shift_L" in keyDowns:
		return
	paddle_top.setp(geo.Point(x, paddle_top.particle.pos.y))
	paddle_bottom.setp(geo.Point(x, paddle_bottom.particle.pos.y))

def exitGame():
	global wnd, interval
	global bgBlock, blocks, ball, paddle_top, paddle_bottom, border_top, border_bottom, border_left, border_right
	if interval.running:
		interval.cancel()
	del bgBlock, blocks, ball, paddle_top, paddle_bottom, border_top, border_bottom, border_left, border_right
	wnd.destroy()

def exitOnEscapeKey(event):
	if event.keysym == "Escape":
		exitGame()

def startGame(event):
	global interval, wnd, canv
	global ball
	ball.setv((geo.Point(event.x, event.y) - ball.particle.pos).unit() * ballSpeed)
	# print(ball.particle.vel)
	interval.start()
	pass

def keyDownHandler(event):
	global keyDowns
	if event.keysym and not event.keysym in keyDowns:
		keyDowns.append(event.keysym)
def keyUpHandler(event):
	exitOnEscapeKey(event)
	global keyDowns
	if event.keysym and event.keysym in keyDowns:
		keyDowns.remove(event.keysym)
	# print(event.keysym)

def leftMouseReleaseHandler(event):
	global __gameStarted
	if not __gameStarted:
		startGame(event)
		__gameStarted = True
	pass

def cursorMotionHandler(event):
	global __gameStarted
	if __gameStarted:
		movePaddlesToCursorX(event.x)
	pass

def updateCanvas():
	global canv
	global blocks, ball, paddle_top, paddle_bottom
	global ballActive, blockHealth, blockHealthDownList
	ball.updateDrawing()
	paddle_top.updateDrawing()
	paddle_bottom.updateDrawing()
	if 2 <= ballActive < 4:
		ballActive -= 2
		canv.itemconfig(ball.circle, ballCanvOptions[ballActive])
	bhdlTmp = blockHealthDownList
	blockHealthDownList = []
	for i in bhdlTmp:
		canv.itemconfig(blocks[i].rect, blockCanvOptions[blockHealth[i]])
	# print(ball.filledCircle.center)

def intervalContent():
	backupIntervalContent()
	updateCanvas()
	pass

def backupIntervalContent():
	global blocks, ball, paddle_top, paddle_bottom, border_top, border_bottom, border_left, border_right
	global keyDowns, ballActive, blockHealth, blockHealthDownList
	# Paddle move on keys
	if not "Shift_L" in keyDowns:
		v = geo.Vector(0, 0)
		if "a" in keyDowns or "Left" in keyDowns:
			v -= geo.Vector(paddleSpeedOnKey, 0)
		if "d" in keyDowns or "Right" in keyDowns:
			v += geo.Vector(paddleSpeedOnKey, 0)
		paddle_top.setv(v)
		paddle_bottom.setv(v)
		paddle_top.move()
		paddle_bottom.move()
		if paddle_top.particle.pos.x < windowDm[0] / 2 - borderOffsetLeftRight:
			paddle_top.setp(geo.Point(windowDm[0] / 2 - borderOffsetLeftRight, paddle_top.particle.pos.y))
		if paddle_top.particle.pos.x > windowDm[0] / 2 + borderOffsetLeftRight:
			paddle_top.setp(geo.Point(windowDm[0] / 2 + borderOffsetLeftRight, paddle_top.particle.pos.y))
		if paddle_bottom.particle.pos.x < windowDm[0] / 2 - borderOffsetLeftRight:
			paddle_bottom.setp(geo.Point(windowDm[0] / 2 - borderOffsetLeftRight, paddle_bottom.particle.pos.y))
		if paddle_bottom.particle.pos.x > windowDm[0] / 2 + borderOffsetLeftRight:
			paddle_bottom.setp(geo.Point(windowDm[0] / 2 + borderOffsetLeftRight, paddle_bottom.particle.pos.y))
	else:
		paddle_top.stop()
		paddle_bottom.stop()
	# Ball collisions
	f_pt = paddle_top.helpColli(ball)
	f_pb = paddle_bottom.helpColli(ball)
	f_bt = border_top.helpColli(ball)
	f_bb = border_bottom.helpColli(ball)
	border_left.helpColli(ball)
	border_right.helpColli(ball)
	for i in range(len(blocks)):
		if blockHealth[i] == 0:
			continue
		f_tmp = blocks[i].helpColli(ball)
		if ballActive and f_tmp:
			blockHealth[i] -= 1
			if not i in blockHealthDownList:
				blockHealthDownList.append(i)
	ball.resolveColli()
	ball.move()
	if f_bt or f_bb:
		ballActive = 2
	if f_pt or f_pb:
		ballActive = 3
	pass

def main():
	global canv, wnd, interval
	global bgBlock, blocks, ball, paddle_top, paddle_bottom, border_top, border_bottom, border_left, border_right
	global screenDm, paddleRadius, ballActive, blockHealth, blockHealthDownList
	wnd = newwindow(title = "{{BREAKOUT}}", size = windowDm)
	screenDm = (wnd.winfo_screenwidth(), wnd.winfo_screenheight())
	wnd.geometry(sizetostr(windowDm, ((screenDm[0] - windowDm[0]) // 2, (screenDm[1] - windowDm[1]) // 2)))
	wnd.bind("<KeyPress>", keyDownHandler)
	wnd.bind("<KeyRelease>", keyUpHandler)
	wnd.bind("<ButtonRelease-1>", leftMouseReleaseHandler)
	wnd.bind("<Motion>", cursorMotionHandler)
	canv = TK.Canvas(wnd, width = windowDm[0], height = windowDm[1])
	canv.pack()
	# Background color block
	bgBlock = ele.StaticRectangle(canv, windowDm[0] / 2, windowDm[1] / 2, windowDm[0], windowDm[1])
	canv.itemconfig(bgBlock.rect, **bgBlockCanvOptions)
	# Blocks
	blocks = []
	blockHealth = []
	blockHealthDownList = []
	blockgridw = blockGridSize[0] * blockSize[0] + (blockGridSize[0] - 1) * blockMargin[0]
	blockgridh = blockGridSize[1] * blockSize[1] + (blockGridSize[1] - 1) * blockMargin[1]
	blockgridx = (windowDm[0] - blockgridw + blockSize[0]) / 2
	blockgridy = (windowDm[1] - blockgridh + blockSize[1]) / 2
	for i in range(blockGridSize[0]):
		for j in range(blockGridSize[1]):
			x = blockgridx + i * (blockSize[0] + blockMargin[0])
			y = blockgridy + j * (blockSize[1] + blockMargin[1])
			block = ele.StaticRectangle(canv, x, y, *blockSize)
			blocks.append(block)
			blockHealth.append(defaultBlockHealth)
			canv.itemconfig(block.rect, blockCanvOptions[defaultBlockHealth])
	# Paddles
	paddleRadius = (paddleHeight + (paddleWidth / 2) ** 2 / paddleHeight) / 2
	paddle_top = ele.Circle(canv, windowDm[0] / 2, borderHeightTopBottom - paddleRadius + paddleHeight, paddleRadius)
	paddle_bottom = ele.Circle(canv, windowDm[0] / 2, windowDm[1] - borderHeightTopBottom + paddleRadius - paddleHeight, paddleRadius)
	canv.itemconfig(paddle_top.circle, **paddleCommonCanvOptions)
	canv.itemconfig(paddle_bottom.circle, **paddleCommonCanvOptions)
	# Ball
	ballActive = 1
	ball = ele.Circle(canv, windowDm[0] / 2, windowDm[1] - borderHeightTopBottom - ballStartOffset, ballRadius)
	canv.itemconfig(ball.circle, **ballCanvOptions[ballActive])
	# Borders
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
