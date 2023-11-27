import numpy as np
import turtle

fill_posibility = [0, 10, 30, 40, 101, 101]
#fill_posibility = [0, 100, 0, 0, 0, 101]

shapearray = np.arange(4).reshape(2,2)
#shapearray2 = np.arange(9).reshape(3,3)

def fill_square(x, y, width):
    t.fillcolor(np.random.randint(50, 100),
                np.random.randint(0, 100), 
                np.random.randint(150, 255))
    t.goto(x,y)
    t.pendown()
    #t.begin_fill()
    for _ in range(4):
        t.forward(width)
        t.left(90)
    #t.end_fill()
    t.penup()

def plot_squares(width, level, x,y, N):
    if level < N:
        fill = (np.random.randint(0,99)<fill_posibility[level])
        if fill:
            fill_square(x,y,width)
        else:
            for (i,j), _ in np.ndenumerate(shapearray):
                plot_squares(width/2, level+1, x+i*width/2,y+j*width/2, N)
            
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
s = turtle.Screen()
s.setup(0.75,1.0)
t.pencolor('black')
t.penup()
t.width(2)
t.goto(-200, -200)
plot_squares(500, 0, -200, -200, 5)
cv = turtle.getcanvas()
cv.postscript(file="squareblackwhitesquares3.ps", colormode='color')
turtle.done()

