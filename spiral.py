from turtle import *
color('red')
colormode(255)
begin_fill()
len = 5
increment = 1
color_increment = 3
red, green, blue = 0, 255, 0

for i in range(90):
    if red >=0 and red <250:
        red += color_increment
    if green>=5:
        green -= color_increment 
    if blue >=0 and blue < 250:
        blue += color_increment
    pencolor(red, green, blue) 
    forward(len)
    left(90-0.3*i)
    len += increment



done()