from turtle import *
from random import randint
from math import sqrt

def drawTree(t, bL, change, penSize, ratio, angle, limit):
    if bL > limit:
        t.pensize(penSize * ratio)
        t.forward(bL)
        t.right(angle)
        drawTree(t, bL-change, change, penSize * ratio, ratio, angle, limit)
        t.left(2 * angle)
        drawTree(t, bL-change, change, penSize * ratio, ratio, angle, limit)
        t.right(angle)
        t.backward(bL)

def drawTreeR(t, bL, penSize, r):
    if bL > randint(r[0], r[1]):
        ratio = randint(5, 8) / 10
        t.pensize(penSize * ratio)
        t.forward(bL)
        angle1 = randint(r[2], r[3])
        angle2 = randint(r[4], r[5])
        t.right(angle1)
        drawTreeR(t, bL-randint(r[6], r[7]),penSize * ratio, r)
        t.left(angle2)
        drawTreeR(t, bL-randint(r[6], r[7]),penSize * ratio, r)
        t.right(angle2 - angle1)
        t.backward(bL)


t = Turtle()
t.hideturtle()
t._tracer(0,0)
myWin = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
t.speed(0)
'''
realistic dead looking tree
'''
drawTreeR(t, 100, 10, [2, 15, 5, 30, 10, 60, 2, 30])
'''
realistic dense tree
drawTreeR(t, 100, 10, [3, 5, 10, 20, 30, 40, 5, 15])
'''
t._update()
myWin.exitonclick()