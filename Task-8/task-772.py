from itertools import *
ans = 0
for val in permutations("ПРОБНИК"):
    val = "".join(val)
    if val[0] in "ПРБНК" and val[-1]  in "ПРБНК" and "ИО" not in val and "ОИ" not in val:
        ans +=1
print(ans)