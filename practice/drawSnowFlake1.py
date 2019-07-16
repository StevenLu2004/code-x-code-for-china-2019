#!/usr/bin/python3.5
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def ri(l, r):
	try:
		return random.randint(l, r)
	except:
		return (l + r) // 2

def fRefreshHandler(fRefresh):
	if fRefresh:
		screen.update()

def drawBranch(L, l, cnt):
	if cnt == 0:
		return
	t.forward(l)
	t.left(60)
	t.forward(L); t.forward(-L)
	t.right(120)
	t.forward(L); t.forward(-L)
	t.left(60)
	drawBranch(L, l, cnt - 1)
	t.forward(-l)

def drawFlake(x, y, L, l, d, cnt, fRefresh = False):
	t.penup()
	t.goto(x, y)
	t.left(d)
	t.pendown()
	for _ in range(6):
		drawBranch(L, l, cnt)
		t.left(60)
	t.penup()
	t.right(d)
	fRefreshHandler(fRefresh)

def randFlake(x = None, y = None, fRefresh = True):
	if x == None:
		x = ri(-300, 300)
	if y == None:
		y = ri(-300, 300)
	l = ri(4, 8)
	L = l * (1 + random.random() * .2)
	d = ri(0, 359)
	cnt = ri(5, 10)
	drawFlake(x, y, L, l, d, cnt)
	fRefreshHandler(fRefresh)

def main():
	screen.onclick(randFlake, btn = 1)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
