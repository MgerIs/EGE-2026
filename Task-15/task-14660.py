from itertools import combinations

def f(x):
    P = 16<=x<=84
    Q = 27<=x<=43
    A = A1<=x<A2
    return (A <= P) or Q

lineA = [16,27,43,84]
lineX = [17,28,44]

ans = []
for A1,A2 in combinations(lineA,2):
    if all(f(x) for x in lineX):
        ans.append(A2-A1)
print(max(ans))