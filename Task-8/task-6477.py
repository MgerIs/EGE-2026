from itertools import *
ans = 0
for val in permutations("ЛЕВИОСА"):
    if val[0] not in "ЕОАИ" and val[3] not in "ЛВС":
        ans += 1
print(ans)