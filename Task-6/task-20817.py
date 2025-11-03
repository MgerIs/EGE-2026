from turtle import*
tracer(0)
screensize(2000,2000)
k=10
pendown()
for i in range(3):
    fd(27*k)
    rt(90)
    fd(12*k)
    rt(90)
penup()
for i in range(1):
    fd(4*k)
    rt(90)
    fd(6*k)
    lt(90)
pendown()
for i in range(4):
    fd(83*k)
    rt(90)
    fd(77*k)
    rt(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
print(84*78+28*13-7*24)
update()
done()