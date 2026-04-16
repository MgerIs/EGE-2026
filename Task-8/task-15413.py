from itertools import product
from string import printable as alph
s =[]
for val in product(alph[:9],repeat=4):
    val = "".join(val)
    if val[0] != "0" and val.count("8") == 1:
        index = val.index("8")
        levo = val[:index]
        pravo = val[index+1:]
        if sum(map(int,levo)) == sum(map(int,pravo)):
            s.append(val)
print(len(s))
