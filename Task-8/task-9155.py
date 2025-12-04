from itertools import *

cnt = 0
alph = sorted("АПРЕЛЬ")[::-1]
for pos,val in enumerate(product(alph, repeat=5), start=1):
    val = "".join(val)
    if val[-1:] == "Ь" and pos<=387:
        cnt+=1
print(cnt)
