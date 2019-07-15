#!/usr/bin/python3.5
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def main():
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
