from itertools import *

cnt = 0
alph = sorted("ЗЕРКАЛО")
for val in product(alph, repeat=6):
    val = "".join(val)
    if "К" in val and val.count("К")<=4:
        for i in "ЗЕРКАЛО":