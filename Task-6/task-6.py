from turtle import *
screensize(2000,2000)
k = 10
tracer(0)
pd()
for i in range(2):
    fd(14*k)
    lt(270)
    bk(12*k)
    rt(90)
pu()
for i in range(1):
    fd(9*k)
    rt(90)
    bk(7*k)
    lt(90)
pd()
for i in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)
penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, 'red')
done()
