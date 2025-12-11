from itertools import *
ans = 0
for val in set(permutations("АМФИБРАХИЙ")):
    val = "".join(val)
    if val[4] + val[5] == "БР":
        ans += 1
print(ans)