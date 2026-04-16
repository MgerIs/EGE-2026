from string import printable
from itertools import *
cnt = 0
for val in product(printable[:7],repeat=7):
    val = "".join(val)
    if val[0] not in "035":
        if "2244" not in val and "4422" not in val:
            cnt +=1
print(cnt)
 