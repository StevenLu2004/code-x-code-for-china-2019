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

def line(x1, y1, x2, y2):
	t.penup()
	t.goto(x1, y1)
	t.pendown()
	t.goto(x2, y2)
	t.penup()

def singlePane(x, y, L, l, q, cnt, fRefresh = False):
	q %= 4
	if q == 0:
		fx = fy = 1
	elif q == 1:
		fx = -1; fy = 1
	elif q == 2:
		fx = fy = -1
	else:
		fx = 1; fy = -1
	line(x, y, x + fx * L, y)
	line(x, y, x, y + fy * L)
	for i in range(cnt):
		line(x + fx * f1(L, l, i / (cnt - 1)), y, x + fx * f1(L, l, i / (cnt - 1)), y + fy * f1(L, l, i / (cnt - 1)))
		line(x, y + fy * f1(L, l, i / (cnt - 1)), x + fx * f1(L, l, i / (cnt - 1)), y + fy * f1(L, l, i / (cnt - 1)))
	if fRefresh:
		screen.update()

def windowsPane(x, y, L, l, cnt, variation = 0, fRefresh = True):
	v = [1 + (random.random() - .5) * variation for _ in range(4)]
	t.color("green")
	singlePane(x, y, L * v[0], l * v[0], 0, cnt)
	t.color("red")
	singlePane(x, y, L * v[1], l * v[1], 1, cnt)
	t.color("blue")
	singlePane(x, y, L * v[2], l * v[2], 2, cnt)
	t.color("yellow")
	singlePane(x, y, L * v[3], l * v[3], 3, cnt)
	if fRefresh:
		screen.update()

def main():
	windowsPane(0, 0, 200, 100, 3, 0)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
