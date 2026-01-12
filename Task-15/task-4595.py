def f(A):
    for x in range(1,100):
            f = (x%2==0) <= (x%3!=0) or (x + A >= 80)
            if not f:
                return False
    return True
ans = []
for A in range(1,100):
    if f(A):
        ans.append(A)
print(min(ans))