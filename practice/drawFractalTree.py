#!/usr/bin/python3.5
import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()
screen.colormode(255)
screen.tracer(0)
t.speed(0)
t.hideturtle()

def defaultWidth(length):
	if length / 20 > 1:
		return length // 20
	return 1

def drawTree(tree, sz, wf = defaultWidth, maxRec = None, rec = 0, idx = 0, fTrunk = True, fRefresh = False):
	if maxRec == None:
		maxRec = math.log(1000000, sum([len(tree[i]) for i in range(len(tree))]) / len(tree))
	if fTrunk:
		t.pensize(wf(sz))
		t.forward(sz)
	for branch in tree[idx]:
		t.left(branch[0])
		if sz * branch[1] >= 2 and rec < maxRec:
			drawTree(tree, sz * branch[1], wf, rec = rec + 1, idx = branch[2])
		t.right(branch[0])
	if fTrunk:
		t.pensize(wf(sz))
		t.forward(-sz)
	if fRefresh:
		screen.update()

myTree = [[[70, .5, 0], [0, .5, 1]], [[-5, 1, 0], [-80, .8, 0]]]
def myTreeWidth(length):
	return 2

def main():
	global myTree
	t.left(90)
	t.forward(-100)
	drawTree(myTree, 100, wf = myTreeWidth, fRefresh = True)
	screen.onkey(turtle.bye, "Escape")
	screen.listen()
	return 0

if __name__ == "__main__":
	main()
	screen.mainloop()
