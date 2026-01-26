from itertools import *
from string import printable as alph
ans = 0
for val in product(alph[:14], repeat=5):
    val = "".join(val)
    if val[0] != "0" and val[-1] in "03" and len(set(val)) == 2:
        ans += 1
print(ans)
