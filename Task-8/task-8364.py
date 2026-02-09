from itertools import *
ans = 0
words = {}
for val,pos in enumerate(product("АЕКРТ",repeat=6),1):
    words["".join(pos)]=val
print(words["РАКЕТА"]-words["КАРЕТА"]-1)