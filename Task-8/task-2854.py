from itertools import *
ans = 0
for val in set(permutations("РОСОМАХА")):
    val = "".join(val)
    for i in "ОА":
        val = val.replace(i,"*")
    for j in "РСМХ":
        val = val.replace(j,"@")
    if "**" not in val and "@@" not in val:
        ans +=1
print(ans)