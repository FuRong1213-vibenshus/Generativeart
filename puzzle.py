CANVAS_SIZE = 500
DENSITY = 20

import turtle

def draw_line1(row, col):
    pass
def draw_line2(row, col):
    lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    t.goto(lower_left)
    t.pendown()
    t.goto(upper_right)
    t.penup()
    

import random
def draw_line3(row, col):
    lower_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    lower_right = (
        ((col + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        (row * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )
    upper_left = (
        (col * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2,
        ((row + 1) * CANVAS_SIZE / DENSITY) - CANVAS_SIZE / 2
    )

    res = random.randint(0,5)

    if res == 0:
        t.goto(upper_left)
        t.pendown()
        t.goto(lower_right)
        t.penup()
    elif res == 1:
        t.goto(lower_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()
    elif res == 2:
        t.goto(upper_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()
    if res == 3:
        t.goto(lower_left)
        t.pendown()
        t.goto(upper_left)
        t.penup()
    elif res == 4:
        t.goto(lower_left)
        t.pendown()
        t.goto(lower_right)
        t.penup()
    elif res == 5:
        t.goto(lower_right)
        t.pendown()
        t.goto(upper_right)
        t.penup()
t = turtle.Turtle()
turtle.colormode(255)
s = turtle.Screen()
s.bgcolor("black")
s.setup(CANVAS_SIZE, CANVAS_SIZE)

t.penup()
t.width(10)
for row in range(DENSITY):
    for col in range(DENSITY):
        t.pencolor(random.randint(0, 255),random.randint(0, 255), random.randint(0, 255)) 
        draw_line3(row, col)
turtle.done()