from math import *
s = []
a = [int(x) for x in open("17_3749.txt")]

sq = max(i for i in a if i**0.5 == int(i**0.5)) *3

for num in zip(a,a[1:]):
    u1 = prod(num) ** 0.5 %1 == 0
    u2 = [i<= sq for i in num]
    if u1 and u2: s.append(prod(num)**0.5)

print(len(s),max(s)+min(s))
