from itertools import *
cnt = 0

for pos,val in enumerate(sorted(product("сулак",repeat=6)), start=1):
    val = "".join(val)
    if pos%2==0 and val[0] == "с" or val[0]=="л":
        for i in "уа":
            val = val.replace(i,"@")
        for j in "слк":
            val = val.replace(i,"#")
        if val.count("@") <= 2 and "@@" not in val:
            print(pos)


