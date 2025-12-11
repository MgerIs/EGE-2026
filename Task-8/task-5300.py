from itertools import *
ans = set()
for val in set(permutations("ХОЧУ В ВУЗ")):
    val = "".join(val)
    if val[0] not in (" ", "У") and val[-1] != " " and all(sub not in val for sub in("  ", " У")):
        ans.add(val)
print(len(ans) - 1)