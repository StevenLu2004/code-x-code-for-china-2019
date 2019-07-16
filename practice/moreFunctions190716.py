#!/usr/bin/python3.5
import random

def getRandomNumber(l, r):
	return random.randint(l, r)

def printLowToHigh(l, r):
	print("\n".join([str(i) for i in range(l, r + 1)]))

def addValues(a, b, c):
	return (a + b + c) ** 2

def main():
	print([getRandomNumber(0, 99) for _ in range(12)])
	printLowToHigh(4, 8)
	print(addValues(123, 456, 789))

if __name__ == "__main__":
	main()
