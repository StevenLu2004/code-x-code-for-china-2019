#!/usr/bin/python3.5
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def f1(a, b, k):
	return a * k + b * (1 - k)

def ri(l, r):
	return random.randint(l, r)

def rc():
	return ri(0, 255)

def setRandColor():
	t.color(rc(), rc(), rc())

def singlePane(x, y, L, l, cnt, fRefresh = False):
	t.penup()
	t.goto(x, y)
	t.left(30)
	t.pendown()
	for i in range(cnt):
		for _ in range(3):
			t.forward(f1(L, l, i / (cnt - 1)))
			t.right(120)
	t.penup()
	t.right(30)
	if fRefresh:
		screen.update()

def windowsPane(x, y, L, l, cnt, d = None, variation = 0, fRefresh = True):
	v = [1 + (random.random() - .5) * variation for _ in range(6)]
	if d == None:
		d = ri(0, 359)
	t.left(d)
	for i in range(6):
		setRandColor(); t.left(60)
		singlePane(x, y, L * v[i], l * v[i], cnt)
	if fRefresh:
		screen.update()

def main():
	windowsPane(0, 0, 200, 100, 3)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
