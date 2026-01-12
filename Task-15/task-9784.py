def f(A):
    for x in range(0,100):
        for y in range(0,100):
            f = (x*y<A) or (x<y) or (9<x)
            if not f:
                return False
    return True
ans = []
for A in range(0,100):
    if f(A):
        ans.append(A)
print(min(ans))