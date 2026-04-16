from math import *
for N in range(1,100000):
    l = 377
    i = ceil(log2(N))
    I = ceil(l*i)/8
    if 23155*I >5536*1024:
        print(N)
        break
print(int("01111000",2))