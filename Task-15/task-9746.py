def f(A):
    for x in range(0,100):
        for y in range(0,100):
            f = (x<A) or (y<A) or (x+2*y > 50)
            if not f:
                return False
    return True
ans = []
for A in range(0,100):
    if f(A):
        ans.append(A)
print(min(ans))