from itertools import *
def f(x,y,z,w):
    return z or (x==(y<=w))
for i in product((0,1),repeat=4):
    table = [
        (1,0,1,i[0]),
        (1,0,i[1],1),
        (i[2],i[3],1,0)
    ]
    if len(set(table))==len(table):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,t))) for t in table] == [0,0,0]:
                print(*p,sep="")