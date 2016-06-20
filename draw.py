import turtle

def drawshape(sides, length):
    angle = 360.0 / sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(angle)

def moveturtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def drawsquare(length):
    drawshape(4, length)

def drawtriangle(length):
    drawshape(3, length)

def drawcircle(length):
    drawshape(360,length)

import random

def drawrandom():
    x = random.randrange(1, 200, 200)
    y = random.randrange(1, 200, 200)
    length = random.randrange(75)
    shape = random.randrange(1, 4)

    moveturtle(x, y)

    if shape == 1:
        drawsquare(length)
    elif shape == 2:
        drawtriangle(length)
    elif shape == 3:
        length = length % 10
        drawcircle(length)

for shape in range(20):
    drawrandom()
turtle.done()
