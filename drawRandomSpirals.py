#!/usr/bin/python3.5
import turtle
import tkinter
import math
import random

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
	t.penup()
	t.forward(r)
	t.pendown()
	t.left(90 + 180 * theta)
	for _ in range(n):
		t.forward(sideL)
		t.left(360 * theta)
	t.right(90 + 180 * theta)
	t.penup()
	t.forward(-r)
	t.right(d)
	if fRefresh:
		screen.update()

def rndc():
	return random.randint(0, 255)

comb = [[3, 1], [4, 1], [5, 2], [7, 2], [7, 3], [8, 3], [9, 2], [9, 4], [100, 1]]
def randStar():
	global comb
	x = random.randint(-300, 300)
	y = random.randint(-300, 300)
	i = random.randint(0, len(comb) - 1)
	d = random.randint(0, 359)
	r = random.randint(30, 100)
	t.color(rndc(), rndc(), rndc())
	drawStar(x, y, comb[i][0], comb[i][1], d, r, fRefresh = True)

def main():
	for _ in range(10):
		randStar()
	turtle.onkey(randStar, "space")
	screen.exitonclick()
	return 0

if __name__ == "__main__":
	main()
