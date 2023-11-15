CANVAS_SIZE = 500
DENSITY = 12
WIDTH = 40
SPACE = 0

import turtle
import random

def draw_line(t, position, x, y, width):
    match position:
        case 'a':
            pos1= (x,y)
            pos2= (x, y+width-SPACE)
        case 'b':
            pos1= (x,y+width-SPACE)
            pos2= (x+width-SPACE, y+width-SPACE)
        case 'c':
            pos1= (x+width-SPACE,y+width-SPACE)
            pos2= (x+width-SPACE,y)
        case 'd':
            pos1= (x,y)
            pos2= (x+width-SPACE, y)
        case 'e':
            pos1= (x,y)
            pos2= (x+width-SPACE,y+width-SPACE)
        case 'f':
            pos1= (x,y+width-SPACE)
            pos2= (x+width-SPACE, y)
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
    t.hideturtle()
    s.setup(CANVAS_SIZE, CANVAS_SIZE)

    t.penup()
    t.width(5)
    t.goto(-CANVAS_SIZE/2, -CANVAS_SIZE/2)
    t.pencolor("black")
    choose = list('abcedf')
    for row in range(DENSITY):
        for col in range(DENSITY):
            position = random.choice(choose)
            t.pencolor(random.randint(1, 255),random.randint(1, 255), random.randint(1, 255)) 
            draw_line(t, position, col*WIDTH- CANVAS_SIZE / 2+SPACE , row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
    turtle.done()

plot()