from itertools import permutations
graph = "dg gb bz ze ev vd da ak bk gk ae".split()
matrix = "248 137 268 15 467 357 256 13".split()

print(*range(1,8))
for i in permutations('abvgdezk'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)