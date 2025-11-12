import turtle
from turtle import *
screensize(2000,2000)
shape("turtle")
k = 10
tracer(0)
speed(10000000000)
left(90)
pendown()
for i in range(2):
    forward(10*k)
    right(90)
    forward(18*k)
    right(90)

penup()
for i in range(1):
    forward(5*k)
    right(90)
    forward(7*k)
    left(90)
pendown()
for i in range(2):
    forward(10 * k)
    right(90)
    forward(7 * k)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x * k, y * k)
        dot(3, "red")
for x in range(-100,100):
    for y in range(-100,100):
        goto(x * k, y * k)
        dot(3, "red")

done()