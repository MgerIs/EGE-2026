s = set()

def f(x, cnt):
    if cnt == 6:
        s.add(x)
        return
    f(x + 1, cnt + 1)
    f(x + 2, cnt + 1)
    f(x * 2, cnt + 1)


f(1, 0)
print(len([x for x in s if 34 <= x <= 59]))
