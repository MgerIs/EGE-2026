from itertools import combinations

def f(x):
    P = 10 <= x <= 150
    Q = 160 <= x <= 250
    R = 240 <= x <= 300
    A = A1 <= x <= A2
    return ((x in Q) <= (x in P)) or (((not x) in A) <= (x in R))

lineA = [10, 150, 160,240, 250,300]
lineX = [11,151,161,241,251]

ans = []
for A1, A2 in combinations(lineA, 2):
    if all(f(x) for x in lineX):
        ans.append(A2-A1)
print(max(ans))

