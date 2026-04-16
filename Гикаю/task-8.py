from itertools import *
cnt =0
sp = []
for val in product("СТРОКА",repeat=5):
    cnt+=1
    val = "".join(val)
    if val[0] not in "АСТ" and val.count("О")==2 and cnt%2==0:
        sp.append(cnt)
print(max(sp))
