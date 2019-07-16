#!/usr/bin/python3.5
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def line(x1, y1, x2, y2):
	t.penup()
	t.goto(x1, y1)
	t.pendown()
	t.goto(x2, y2)
	t.penup()

def drawPyramid():
	line(0, 200, 400 / (3 ** .5), -200)
	line(0, 200, -400 / (3 ** .5), -200)
	for i in range(1, 41):
		line(-(10 * i) / (3 ** .5), 200 - i * 10, (10 * i) / (3 ** .5), 200 - i * 10)
	screen.update()

def main():
	drawPyramid()
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
