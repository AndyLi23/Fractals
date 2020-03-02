from turtle import *

def drawTriangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, t):
    colormap = ['brown', 'violet','white', 'yellow', 'orange', 'green', 'red', 'blue', 'pink']
    drawTriangle(points, colormap[degree], t)
    if degree > 0:
        sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree - 1, t)
        sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree - 1, t)
        sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree - 1, t)


t = Turtle()
t._tracer(0, 0)
t.speed(0)
t.hideturtle()
myWin = t.getscreen()
myPoints = [(-400, -200), (0, 400), (400, -200)]
sierpinski(myPoints, 7, t)
t._update()
myWin.exitonclick()