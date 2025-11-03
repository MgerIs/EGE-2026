from turtle import*
screensize(2000,2000)
tracer(0)
k = 10
pendown()
for i in range(2):
    fd(23*k)
    lt(90)
    bk(27*k)
    lt(90)
penup()
for i in range(1):
    bk(5*k)
    rt(90)
    fd(11*k)
    lt(90)
pendown()
for i in range(2):
    fd(26*k)
    rt(90)
    fd(32*k)
    rt(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
print(24*28+27*33-22*17)
update()
done()