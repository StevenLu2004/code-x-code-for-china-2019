#!/usr/bin/python3.5
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)

def main():
	screen.onkey(turtle.bye, "Escape")
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
