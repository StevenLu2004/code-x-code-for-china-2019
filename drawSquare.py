#!/usr/bin/python3.5
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)

def main():
	t.speed(0)
	screen.tracer(0)
	for _ in range(4):
		t.fd(200)
		t.left(90)
	screen.update()
	screen.exitonclick()
	return 0

if __name__ == "__main__":
	main()
