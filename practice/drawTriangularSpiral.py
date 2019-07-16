#!/usr/bin/python3.5
import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

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
		setRandColor(t)
		t.forward(L)
		t.left(120)
		L += l
	t.penup()
	if fRefresh:
		screen.update()

def main():
	drawSpiral(0, 0, 16, 16, 4, 32, fRefresh = True)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
