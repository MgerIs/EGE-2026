from itertools import *

cnt =  0
alph =  "0123456"
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = "".join(val)
    if  4 <= int(val[-1]) and val[0] != "0"  and val.count("0")+val.count("2")+val.count("4")+val.count("6") == val.count("1")+val.count("3")+val.count("5"):
        cnt +=1
print(cnt)
