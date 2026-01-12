def f(A):
    for x in range(0,100):
        for y in range(0,100):
            f = (x+y<=22) or (y<=x-6) or (y>=A)
            if not f:
                return False
    return True
ans = []
for A in range(0,100):
    if f(A):
        ans.append(A)
print(max(ans))