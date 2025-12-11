from itertools import *
ans = 0
for val in set(permutations("ХОЧУ СОТКУ")):
    val = "".join(val)
    if val[0] not in " У" and " У" not in val and val[-1] not in " ":
        ans += 1
print(ans - 1)
