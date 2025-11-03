from turtle import*
screensize(2000,2000)
tracer(0)
k = 20
pendown()
for i in range(2):
    fd(5*k)
    left(90)
    bk(13*k)
    left(90)
penup()
for i in range(1):
    bk(10*k)
    right(90)
    fd(9*k)
    left(90)
pendown()
for i in range(2):
    fd(11*k)
    right(90)
    fd(7*k)
    right(90)
penup()
for x in range(-10, 20):
    for y in range(-20, 10):
        goto(x * k, y * k)
        dot(3, 'red')
done()
