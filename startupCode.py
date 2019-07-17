#!/usr/bin/python3
import turtle
import random
from turtle import TK

def sizetostr(size,pos):
    return str(int(size[0]))+"x"+str(int(size[1]))+"+"+str(int(pos[0]))+"+"+str(int(pos[1]))

randerlib="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#*"
def rander(a=3,b=4,confirm=False):
    res=""
    for i in range(a):
        if i!=0:
            res+="-"
        cur=""
        num=0
        for j in range(b):
            i=random.randint(0,len(randerlib)-1)
            cur+=randerlib[i]
            num=num^i
        if confirm:
            cur+=randerlib[num]
        res+=cur
    return res

def newwindow(title=None,size=(200,200),pos=(100,100)):
    wn=TK.Tk()
    wn.geometry(sizetostr(size,pos))
    if title==None:
        title=rander()
    wn.title(title)
    cv=TK.Canvas(wn,width=size[0],height=size[1])
    cv.pack()
    sc=turtle.TurtleScreen(cv)
    return (wn,cv,sc)

def delwindow(wnd):
	wnd[0].destroy()

def main():
	global wnd
	wnd = newwindow(title = "Practice", size = (400, 300))
	def destroy_wrapper():
		delwindow(wnd)
	wnd[2].onkey(destroy_wrapper, "Escape")
	wnd[2].listen()
	return 0

if __name__ == "__main__":
	main()
	wnd[2].mainloop()
