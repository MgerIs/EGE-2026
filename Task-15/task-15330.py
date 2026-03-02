from itertools import *
def f(x):
    B = 24 <=x <= 90
    C = 47 <=x<= 115
    A = A1 <= x <= A2
    return C <= (((not A) and B) <= (not C))

LineA = [24,47,90,115]
LineX = [25,48,91]

ans = []
for A1, A2 in combinations(LineA,2):
    if all(f(x) for x in LineX):
        ans.append(A2-A1)
print(min(ans))