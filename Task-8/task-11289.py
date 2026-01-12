from itertools import *
from string import printable as alph
cnt = 0
for val in product(alph[:9], repeat=7):
    val = ''.join(val)
    if len(set(val)) == 7:
        if val[0] != "0":
            for i in "0468":
                val = val.replace(i, "*")
            for j in "1357":
                val = val.replace(j, "@")
            if "2" not in val and "**" not in val and "@@" not in val:
                cnt +=1
print(cnt)