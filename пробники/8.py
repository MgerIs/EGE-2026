from itertools import *
from string import printable as alph

cnt = 0
for val in product(alph[:7],repeat=7):
    val = "".join(val)
    if val[0] != "0":
        if "22" not in val and "44" not in val and val[0] not in "35":
            cnt +=1
print(cnt)
a = "123456"
print(a[:2])