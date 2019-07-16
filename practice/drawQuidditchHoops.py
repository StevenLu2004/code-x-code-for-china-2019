#!/usr/bin/python3.5
import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

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
		# t.begin_fill()
		t.left(90 + 180 * theta)
		for _ in range(n):
			t.forward(sideL)
			t.left(360 * theta)
		t.right(90 + 180 * theta)
		# t.end_fill()
		t.penup()
		t.forward(-r)
		t.left(360 / n / g)
	t.right(360 / n)
	t.right(d)
	if fRefresh:
		screen.update()

def drawQuidditchHoop(x = None, y = None, fRefresh = True):
	global t, screen
	t.penup()
	t.goto(x, -200)
	t.pendown()
	t.goto(x, y - 10)
	drawStar(x, y, 360, 1, 0, 10)
	if fRefresh:
		screen.update()

def main():
	drawQuidditchHoop(-50, 50)
	drawQuidditchHoop(0, 100)
	drawQuidditchHoop(50, 50)
	screen.onclick(drawQuidditchHoop, btn = 1)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
