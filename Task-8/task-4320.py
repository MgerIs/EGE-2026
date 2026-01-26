from itertools import *
from string import printable as alph
ans = 0
for val in permutations(alph[:8],r=6):
    val = "".join(val)
    if int(val,8)%5==0 and val[0]!="0":
        for i in "0246":
            val = val.replace(i,"*")
        for i in "1357":
            val = val.replace(i,"@")
        if "@@" not in val and "**" not in val:
            ans+=1
print(ans)
