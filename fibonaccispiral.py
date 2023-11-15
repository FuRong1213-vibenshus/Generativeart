import turtle
wn=turtle.Screen()
wn.bgcolor("white")
from turtle import *
 
prev=0
start=1
fibonacci=1
sqs = input("How many Squares do you want?")
for i in range(int(sqs)):
   print(str(i)+". "+str(fibonacci))
   
   color('black')
   for f in range(6):
       forward(5*fibonacci)
       if f<5:right(90)
 
   fibonacci=start+prev
   prev=start
   start=fibonacci