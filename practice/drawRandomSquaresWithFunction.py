#!/usr/bin/python3.5
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def ri(low, high):
	return random.randint(low, high)

def line(x1, y1, x2, y2):
	t.penup()
	t.goto(x1, y1)
	t.pendown()
	t.goto(x2, y2)
	t.penup()

def drawSquare(x = None, y = None, l = None, fRefresh = True):
	if x == None:
		x = ri(-300, 300)
	if y == None:
		y = ri(-300, 300)
	if l == None:
		l = ri(10, 100)
	t.penup()
	t.goto(x - l/2, y - l/2)
	t.pendown()
	t.goto(x + l/2, y - l/2)
	t.goto(x + l/2, y + l/2)
	t.goto(x - l/2, y + l/2)
	t.goto(x - l/2, y - l/2)
	t.penup()

def main():
	for _ in range(50):
		drawSquare()
	screen.onclick(drawSquare, btn = 1)
	screen.onkey(drawSquare, "space")
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
