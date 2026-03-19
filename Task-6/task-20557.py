from turtle import *
screensize(2000,2000)
k = 10
tracer(0)
pd()
for i in range(4):
    fd(36*k)
    rt(90)
    fd(41*k)
    rt(90)
pu()
for i in range(1):
    rt(90)
    fd(20*k)
    lt(90)
    fd(20*k)
pd()
for i in range(4):
    fd(25*k)
    rt(90)
pu()
for i in range(1):
    fd(7*k)
    lt(90)
    fd(7*k)
    rt(90)
pd()
for i in range(7):
    fd(16*k)
    rt(90)
penup()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*k,y*k)
        dot(3,"red")
update()
done()