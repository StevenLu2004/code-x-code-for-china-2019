#!/usr/bin/python3.5
import random
import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def getRandomNumber(l, r):
	return random.randint(l, r)

def ri(l, r):
	return getRandomNumber(l, r)

def printLowToHigh(l, r):
	print("\n".join([str(i) for i in range(l, r + 1)]))

def addValues(a, b, c):
	return (a + b + c) ** 2

def multiply(a, b):
	return a * b

def countToOneHundred(x):
	print(" ".join([str(i) for i in range(x, 101)]))

def countToZero(x):
	print(" ".join([str(-i) for i in range(-x, 1)]))

def moneyFunction1(money, tooMuchMoney):
	money = money / 10 if money > tooMuchMoney else money * 4
	print(money)

def compareWithZero(number):
	if number > 0:
		print("Bigger than zero")
	elif number == 0:
		print("Equal to zero")
	else:
		print("Smaller than zero")

def drawShapeForAngle(angle):
	d = ri(0, 359)
	t.left(d)
	if angle == 90:
		for _ in range(4):
			t.forward(100)
			t.left(90)
	elif angle == 120:
		for _ in range(3):
			t.forward(100)
			t.left(120)
	else:
		t.circle(100)
	t.right(d)
	screen.update()

def main():
	# print([getRandomNumber(0, 99) for _ in range(12)])
	# printLowToHigh(4, 8)
	# print(addValues(123, 456, 789))
	# print(multiply(int(input()), int(input())))
	# countToOneHundred(int(input()))
	# countToZero(int(input()))
	# moneyFunction1(120, 100)
	compareWithZero(10)
	compareWithZero(0)
	compareWithZero(-10)
	drawShapeForAngle(1)
	drawShapeForAngle(90)
	drawShapeForAngle(120)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
