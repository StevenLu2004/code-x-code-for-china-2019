#!/usr/bin/python3
import turtle
import intervals3 as itv3
import random
import math
from turtle import TK

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
	cv=TK.Canvas(wn,width=size[0],height=size[1])
	cv.pack()
	sc=turtle.TurtleScreen(cv)
	sc.tracer(0)
	return (wn,cv,sc)

def delwindow(wnd):
	wnd[0].destroy()

ship_coord = [0, 0]
ship_speed = [0, 0]
ship_heading = 90
ship_accel = 1
ship_flexibility = 6
f_shipcrash = False

def updateShipPos():
	global ship_coord, ship_speed
	ship_coord[0] += ship_speed[0]
	ship_coord[1] += ship_speed[1]

def turnShip_left():
	global ship_heading, ship_flexibility
	ship_heading += ship_flexibility
	if ship_heading >= 180:
		ship_heading -= 360
	if ship_heading < -180:
		ship_heading += 360
def turnShip_right():
	global ship_heading, ship_flexibility
	ship_heading -= ship_flexibility
	if ship_heading >= 180:
		ship_heading -= 360
	if ship_heading < -180:
		ship_heading += 360

def accelerateShip():
	global ship_heading, ship_speed
	sh = ship_heading / 180 * math.pi
	ship_speed[0] += ship_accel * math.cos(sh)
	ship_speed[1] += ship_accel * math.sin(sh)

def checkCrash():
	global f_shipcrash
	f_shipcrash = not ((universe_bounaries[0][0] < ship_coord[0] < universe_bounaries[0][1]) and (universe_bounaries[1][0] < ship_coord[1] < universe_bounaries[1][1]))

def showShip():
	global ship, ship_coord, ship_heading
	ship.goto(ship_coord[0], ship_coord[1])
	ship.setheading(ship_heading)

universe_bounaries = ((-390, 390), (-290, 290))

def drawUniverseBoundaries():
	global boundPen
	boundPen.penup()
	boundPen.goto(universe_bounaries[0][0], universe_bounaries[1][0])
	boundPen.pendown()
	boundPen.goto(universe_bounaries[0][1], universe_bounaries[1][0])
	boundPen.goto(universe_bounaries[0][1], universe_bounaries[1][1])
	boundPen.goto(universe_bounaries[0][0], universe_bounaries[1][1])
	boundPen.goto(universe_bounaries[0][0], universe_bounaries[1][0])
	boundPen.penup()

keys = []
f_gameover = False

def updateData():
	global keys, f_shipcrash
	if f_shipcrash:
		return
	if "left" in keys:
		turnShip_left()
	if "right" in keys:
		turnShip_right()
	if "up" in keys:
		accelerateShip()
	updateShipPos()
	checkCrash()

def draw():
	global wnd, f_shipcrash, f_gameover
	if f_gameover:
		return
	# wnd[2].clear()
	showShip()
	if f_shipcrash:
		ship.color("red"); ship.shape("circle")
	# drawUniverseBoundaries()
	wnd[2].update()

def aftermath():
	global f_gameover
	if f_gameover:
		return
	f_gameover = f_shipcrash

def intervalContent():
	updateData()
	draw()
	aftermath()

def pressLeftKey():
	global keys
	if not ("left" in keys):
		keys.append("left")
def pressRightKey():
	global keys
	if not ("right" in keys):
		keys.append("right")
def pressUpKey():
	global keys
	if not ("up" in keys):
		keys.append("up")

def releaseLeftKey():
	global keys
	while ("left" in keys):
		keys.remove("left")
def releaseRightKey():
	global keys
	while ("right" in keys):
		keys.remove("right")
def releaseUpKey():
	global keys
	while ("up" in keys):
		keys.remove("up")

def main():
	global wnd, ship, boundPen, interval1
	def destroy_wrapper():
		interval1.cancel()
		delwindow(wnd)
	wnd = newwindow(title = "Stay Inbounds [$teven edit]", size = (800, 600))
	wnd[2].onkey(destroy_wrapper, "Escape")
	ship = turtle.RawTurtle(wnd[2])
	ship.speed(0)
	ship.penup()
	boundPen = turtle.RawTurtle(wnd[2])
	boundPen.speed(0)
	boundPen.penup()
	boundPen.hideturtle()
	boundPen.color("red")
	drawUniverseBoundaries()
	interval1 = itv3.Interval(intervalContent, .05)
	wnd[2].onkeypress(pressLeftKey, "Left")
	wnd[2].onkeypress(pressRightKey, "Right")
	wnd[2].onkeypress(pressUpKey, "Up")
	wnd[2].onkeyrelease(releaseLeftKey, "Left")
	wnd[2].onkeyrelease(releaseRightKey, "Right")
	wnd[2].onkeyrelease(releaseUpKey, "Up")
	wnd[2].listen()
	interval1.start()
	return 0

if __name__ == "__main__":
	main()
	wnd[2].mainloop()
