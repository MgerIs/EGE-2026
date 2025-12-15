from turtle import*
screensize(2000,2000)
tracer(0)
k = 10
pendown()
for i in range(6):
    fd(33*k)
    rt(90)
    fd(20*k)
    rt(90)
penup()
for i in range(1):
    fd(3*k)
    rt(90)
    fd(9*k)
    lt(90)
pendown()
for i in range(6):
    fd(24*k)
    rt(90)
    fd(25*k)
    rt(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3, 'red')
print()
update()
done()
