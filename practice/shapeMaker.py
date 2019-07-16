#!/usr/bin/python3.5
import turtle
import math
import random

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def ri(l, r):
	return random.randint(l, r)

def rc():
	return random.randint(0, 255)

def setRandColor(turt):
	turt.color(rc(), rc(), rc())

def drawSpiral(x, y, L, l, w, cnt, fRefresh = False):
	global t, screen
	t.penup()
	t.goto(x, y)
	t.pensize(w)
	t.pendown()
	for _ in range(cnt):
		t.forward(L)
		t.forward(-L)
		t.left(360 / cnt)
		L *= l
	t.penup()
	if fRefresh:
		screen.update()

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def drawStar(x, y, n, m, d, r, fRefresh = False):
	t.penup()
	t.goto(x, y)
	t.left(d)
	g = gcd(n, m)
	n //= g; m //= g
	theta = m / n
	sideL = 2 * r * math.cos((.5 - theta) * math.pi)
	for _ in range(g):
		t.penup()
		t.forward(r)
		t.pendown()
		t.begin_fill()
		t.left(90 + 180 * theta)
		for _ in range(n):
			t.forward(sideL)
			t.left(360 * theta)
		t.right(90 + 180 * theta)
		t.end_fill()
		t.penup()
		t.forward(-r)
		t.left(360 / n / g)
	t.right(360 / n)
	t.right(d)
	if fRefresh:
		screen.update()

def drawSquare(x = None, y = None, r = None, d = None):
	setRandColor(t)
	if x == None:
		x = ri(-300, 300)
	if y == None:
		y = ri(-300, 300)
	if r == None:
		r = ri(30, 60)
	if d == None:
		d = ri(0, 359)
	drawStar(x, y, 4, 1, d, r, fRefresh = True)

def drawCircle(x = None, y = None, r = None):
	setRandColor(t)
	if x == None:
		x = ri(-300, 300)
	if y == None:
		y = ri(-300, 300)
	if r == None:
		r = ri(20, 40)
	drawStar(x, y, 360, 1, 0, r, fRefresh = True)

def drawFirework(x = None, y = None, r = None, d = None, cnt = 36):
	setRandColor(t)
	if x == None:
		x = ri(-300, 300)
	if y == None:
		y = ri(-300, 300)
	if r == None:
		r = ri(20, 40)
	if d == None:
		d = ri(0, 359)
	t.left(d)
	drawSpiral(x, y, r, 1, 1, cnt, fRefresh = True)
	t.right(d)

def drawOctagon(x = None, y = None, r = None, d = None):
	setRandColor(t)
	if x == None:
		x = ri(-300, 300)
	if y == None:
		y = ri(-300, 300)
	if r == None:
		r = ri(22, 44)
	if d == None:
		d = ri(0, 359)
	drawStar(x, y, 8, 1, d, r, fRefresh = True)

def main():
	screen.onkey(drawSquare, "Up")
	screen.onkey(drawOctagon, "Down")
	screen.onkey(drawFirework, "Left")
	screen.onkey(drawCircle, "Right")
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
