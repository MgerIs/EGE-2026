from itertools import product
from string import printable

cnt = 0
for val in product(printable[:25], repeat=4):
    val = "".join(val)
    if val[0] != "0":
        even = sum(val.count(i) for i in printable[:25:2])
        m15 = sum(val.count(j) for j in printable[16:25])
        if even >= 1 and m15 > 2:
            cnt += 1
print(cnt)