#!/usr/bin/python3
import intervals2 as itv
import turtle
import tkinter
import timeit
import time
import random

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def ri(l, r):
	return random.randint(l, r)

def fun1():
	global t, screen, ri
	t.forward(ri(1, 10))
	t.left(90)
	screen.update()

def exitHandler():
	global interval1
	interval1.cancel()
	turtle.bye()
	print(interval1.thread1.is_alive())

def main():
	global interval1
	interval1 = itv.Interval(fun1, .1, True)
	interval1.start()
	screen.onkey(exitHandler, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
