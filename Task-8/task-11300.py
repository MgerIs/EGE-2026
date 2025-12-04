from itertools import *

cnt = 0
alph = sorted("ГОНДУБШ")
for pos,val in enumerate(product(alph, repeat=6), start=1):
    val = "".join(val)
    if pos % 2 == 1 and val[0] !=    "Б" and val.count("Н") >= 2 and "У" not in val:
        print(pos)