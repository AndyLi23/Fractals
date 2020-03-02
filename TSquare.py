from turtle import *
from math import sqrt

def drawSquare(t, center, width):
    t.goto((center[0]-(width/2)), center[1]+(width/2))
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.goto((center[0] + (width / 2)), center[1] + (width / 2))
    t.goto((center[0] + (width / 2)), center[1] - (width / 2))
    t.goto((center[0] - (width / 2)), center[1] - (width / 2))
    t.goto((center[0] - (width / 2)), center[1] + (width / 2))
    t.end_fill()
    t.penup()

def TSquareR(center, width, t, skip, degree, ratio=2):
    drawSquare(t, center, width)
    if degree-1 > 0:
        if skip != 0:
            TSquareR((center[0]-(width/ratio), center[1]+(width/ratio)), width/ratio, t, 2, degree-1, ratio)
        if skip != 1:
            TSquareR((center[0] + (width / ratio), center[1] + (width / ratio)), width / ratio, t, 3, degree-1, ratio)
        if skip != 2:
            TSquareR((center[0] + (width / ratio), center[1] - (width / ratio)), width / ratio, t, 0, degree-1, ratio)
        if skip != 3:
            TSquareR((center[0] - (width / ratio), center[1] - (width / ratio)), width / ratio, t, 1, degree-1, ratio)


def TSquare2R(center, width, t, skip, degree, ratio):
    drawSquare(t, center, width)
    if degree-1 > 0:
        newCenter = width / 2 + width / ratio / 2
        if skip != 0:
            TSquare2R((center[0] - newCenter, center[1] + newCenter), width / ratio, t, 2, degree-1, ratio)
        if skip != 1:
            TSquare2R((center[0] + newCenter, center[1] + newCenter), width / ratio, t, 3, degree-1, ratio)
        if skip != 2:
            TSquare2R((center[0] + newCenter, center[1] - newCenter), width / ratio, t, 0, degree-1, ratio)
        if skip != 3:
            TSquare2R((center[0] - newCenter, center[1] - newCenter), width / ratio, t, 1, degree-1, ratio)

t = Turtle()
t._tracer(0, 0)
t.hideturtle()
t.penup()
t.speed(0)
myWin = t.getscreen()

'''
1/2 ratio t-square, degree 8
'''
TSquareR((0, 0), 300, t, None, 8)



'''
1/phi ratio square branches, degree 9

TSquare2R((0, 0), 100, t, None, 9, (sqrt(5) + 1) / 2)
'''

t._update()





