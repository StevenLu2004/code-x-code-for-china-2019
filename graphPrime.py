import getPrime
import turtle
import random
from turtle import TK
import math

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

primes = []

def drawPrimes(rng, delayedUpdate = True, delayStep = .01):
    global primes
    pos = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    d = 0
    len = 1
    cnt = 0
    c = [0, 0]
    wnd = newwindow(size = (math.sqrt(rng) + 16, math.sqrt(rng) + 16))
    if delayedUpdate:
        wnd[2].tracer(0)
    t = turtle.RawTurtle(wnd[2])
    t.speed(0)
    t.hideturtle()
    t.penup()
    progress = 0
    print("Paint progress: {:f}        ".format(progress), end = "\r");
    for i in range(2, rng + 1):
        c[0] += pos[d][0]
        c[1] += pos[d][1]
        if i in primes:
            t.goto(c[0], c[1])
            t.dot(1)
        cnt += 1
        if cnt >= len:
            cnt = 0
            d = (d + 1) & 3
            if d & 1 == 0:
                len += 1
        if progress + delayStep <= i / rng:
            progress += delayStep;
            print("Paint progress: {:f}        ".format(progress), end = "\r");
            if delayedUpdate:
                wnd[2].update()
    print("Paint progress: {:f}".format(progress), end = "\n");
    if delayedUpdate:
        wnd[2].update()
    return wnd

if __name__ == "__main__":
    rng = int(input("range: "))
    primes = getPrime.getPrime(rng, progress_show = "by prog")
    wnd = drawPrimes(rng)
    input("Input anything to destroy window.")
    wnd[0].destroy()
