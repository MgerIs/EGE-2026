from itertools import *
ans = 0
for val in permutations("ЗАПИСЬ"):
    val = "".join(val)
    if val[0] not in "Ь" and "АЬ" not in val and "ИЬ" not in val:
        ans += 1
print(ans)