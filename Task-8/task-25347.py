from itertools import *
ans = []
alph = sorted("ГРАНИТ")
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = "".join(val)
    if pos%2 ==1 and "А" not in val[0] and "И" not in val[0] and "Г" not in val[0] and val.count("А") == 1:
        ans.append(pos)
print(min(ans))
