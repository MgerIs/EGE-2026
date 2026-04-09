from itertools import *
from string import printable

cnt = 0
for val in product(printable[:7], repeat=5):
    val = "".join(val)
    if val[0] != "0":
        if all(val[i] != val[i + 1] for i in range(len(val) - 1)):
            for i in "345":
                val = val.replace(i, "@")
            if val.count("@") ==2:
                cnt += 1
print(cnt)
