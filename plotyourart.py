CANVAS_SIZE = 500
DENSITY = 20
WIDTH = 20
SPACE = 5

import turtle
import random

def draw_line(t, position, x, y, width):
    # TBD: You should calculate the start and end positions (pos1, pos2) 
    # for each line
    pos1=(x,y)
    pos2=(x+width,y+width)
    match position:
        case 'a':
           pass
        case 'b':
           pass
        case 'c':
           pass 
        case 'd':
           pass
        case _:
            pass

    t.goto(pos1)
    t.pendown()
    t.goto(pos2)
    t.penup()


def plot():
    t = turtle.Turtle()
    turtle.colormode(255)
    s = turtle.Screen()
    s.setup(CANVAS_SIZE, CANVAS_SIZE)
    t.penup()
    t.width(2)
    t.goto(-CANVAS_SIZE/2, -CANVAS_SIZE/2)
    t.pencolor("black")
    choose = list('abcd')
    for row in range(DENSITY):
        for col in range(DENSITY):
            position = random.choice(choose)
            # TBD: Call the function draw_line
            # and draw the different line choices
            pass
    turtle.done()

plot()