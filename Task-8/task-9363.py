from itertools import *
ans = 0
for val in permutations("ХОЧУНАБЮДЖЕТ"):
    val ="".join(val)
    for i in "ОУАЮЕ":
        val = val.replace(i, "*")
    if "*****" not in val:
        ans +=1
print(ans)
