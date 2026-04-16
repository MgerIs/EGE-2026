from turtle import *
k = 10
screensize(2000,2000)
tracer(0)
pd()
for i in range(4):
    fd(10*k)
    rt(270)
pu()
for i in range(1):
    fd(3*k)
    rt(270)
    fd(5*k)
    rt(90)
pd()
for i in range(2):
    fd(10*k)
    rt(270)
    fd(12*k)
    rt(270)
pu()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,"red")
update()
done()
print()