def f(x,y):
    for x in range(-100, 100):
        for y in range(-100, 100):
            f = ((a < x) or (x ** 2 - 7 * x + 10 > 0)) and ((a >= y) or (y ** 2 + 7 * y + 12 > 0))
            if not f:
                return False
    return True


ans = 0
for a in range(100):
    if all(f(x,y) for x in range(100) for y in range(100)):
        ans +=1
print(ans)
