from itertools import *
ans = 0
for val in set(permutations("ТИХОРЕЦК", r=4)):
    val = "".join(val)
    for i in "ИОЕ":
        val = val.replace(i,"*")
    if val.count("*")==2:
        ans += 1
print(ans)
