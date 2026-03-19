def f(s, e, cnt):
    if s == e and cnt > 51: return 1
    if s > e: return 0
    return f(s + 2, e, cnt + 1) + f(s * 3, e, cnt + 1) + f(s * 4, e, cnt + 1)

print(f(2, 400, 0))
