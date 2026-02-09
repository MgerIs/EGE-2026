from itertools import *
from string import printable
ans = 0
for val in product(printable[:9], repeat=7):
    val = "".join(val)
    if val.count("8")==1:
        if val[0] != "0":
            for i in "1357":
                val = val.replace(i,"*")
            for j in "02468":
                val = val.replace(j  ,"@")
            if val[0]!="*" and val[-1] != "@":
                ans += 1
print(ans)