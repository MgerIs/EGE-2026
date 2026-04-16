from itertools import *

cnt= 0
alph = sorted("АРГУМЕНТ")
for pos,val in enumerate(sorted(product(alph,repeat=4)),start=1):
    slova = "".join(val)
    if len(slova) == len(set(slova)):
        if list(slova) == sorted(slova):
            print(pos)


