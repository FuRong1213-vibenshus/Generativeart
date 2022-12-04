CANVAS_SIZE = 500
DENSITY = 12
WIDTH = 40
SPACE = 6

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
    t.width(3)
    t.goto(-CANVAS_SIZE/2, -CANVAS_SIZE/2)
    t.pencolor("black")
    choose = range(6)
    for row in range(DENSITY):
        for col in range(DENSITY):
            position = random.choice(choose)
            t.pencolor(random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)) 
            match position:
                case 0: 
                    draw_line(t, 'a', col*WIDTH- CANVAS_SIZE / 2+SPACE , row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                    draw_line(t, 'b', col*WIDTH- CANVAS_SIZE / 2+SPACE , row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                case 1:
                    draw_line(t, 'a', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                    draw_line(t, 'c', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                case 2:    
                    draw_line(t, 'a', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                    draw_line(t, 'd', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                case 3:
                    draw_line(t, 'b', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                    draw_line(t, 'c', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                case 4:
                    draw_line(t, 'b', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                    draw_line(t, 'd', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                case 5:
                    draw_line(t, 'c', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
                    draw_line(t, 'd', col*WIDTH- CANVAS_SIZE / 2+SPACE, row*WIDTH- CANVAS_SIZE / 2+SPACE, WIDTH)
    turtle.done()

plot()