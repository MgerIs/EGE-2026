from math import *
for N in range(1,100000):
    L = 261
    i= ceil(log2(N))
    I = ceil(L*i/8)
    if 252500*I > 31*1024*1024:
        print(N)
        break