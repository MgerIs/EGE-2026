from itertools import *
from string import printable
ans = 0
for val in product(printable[10:16], repeat=6):
    val = "".join(val)
    if val[0] != "a" and val[0] !="e" and val[-1] != "a" and val[-1] != "e":
        ans += 1
print(ans)