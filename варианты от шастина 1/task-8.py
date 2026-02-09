from itertools import *
alph = sorted("БУРАТИНО")
for pos,val in enumerate(product(alph,repeat=5),start=1):
    val = "".join(val)
    if pos % 2== 1 and val[0] != "А" and val[0] != "У" and val[0] != "И" and val[0] != "О" and len(set(val)) == len(val):
        print(pos)