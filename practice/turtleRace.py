#!/usr/bin/python3
import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
t1 = turtle.Turtle()
t1.speed(2)
t1.shape("turtle")
t1.hideturtle()
t2 = turtle.Turtle()
t2.speed(2)
t2.shape("turtle")
t2.hideturtle()
t3 = turtle.Turtle()
t3.speed(2)
t3.shape("turtle")
t3.hideturtle()
rulerPen = turtle.Turtle()
rulerPen.speed(0)
rulerPen.hideturtle()

def ri(l, r):
    return random.randint(l, r)

gameDone = False

def game(x, y):
    global t1, t2, t3, rulerPen, gameDone
    if gameDone:
        return
    gameDone = True
    t1.penup(); t2.penup(); t3.penup()
    t1.goto(-200, 50); t2.goto(-200, 0); t3.goto(-200, -50)
    t1.pendown(); t2.pendown(); t3.pendown()
    t1.showturtle(); t2.showturtle(); t3.showturtle()
    t1.color("#ff0000"); t2.color("#00ff00"); t3.color("#0000ff")
    for _ in range(25):
        t1.forward(ri(0, 16))
        t2.forward(ri(0, 16))
        t3.forward(ri(0, 16))

def main():
    for i in range(-20, 21):
        rulerPen.penup()
        rulerPen.goto(i * 10, 100)
        rulerPen.pendown()
        rulerPen.goto(i * 10, -100)
        rulerPen.penup()
    screen.onclick(game, btn = 1)
    screen.onkey(turtle.bye, "Escape")
    screen.listen()
    return 0

if __name__ == "__main__":
    main()
    screen.mainloop()
