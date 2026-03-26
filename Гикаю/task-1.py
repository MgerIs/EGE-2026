from itertools import permutations

graph = "AC CB BH HD DA HF FE EG GC GA".split()
matrix = "258 17 56 68 138 347 26 145".split()

print(*range(1,8))

for i in permutations("ABCDHFGE"):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)