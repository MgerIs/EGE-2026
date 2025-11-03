from turtle import*
screensize(2000,2000)
tracer(0)
k = 10
pendown()
for i in range(2):
    fd(28*k)
    rt(90)
    fd(18*k)
    rt(90)
penup()
for i in range(1):
    fd(14*k)
    rt(90)
    fd(10*k)
    lt(90)
pendown()
for i in range(2):
    fd(30*k)
    rt(90)
    fd(7*k)
    rt(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
print(31*8+29*19-15*8)
update()
done()
