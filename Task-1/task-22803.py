from itertools import permutations

graph = 'af fe eg gb ba ad fd ec cb'.split()
matrix = '234 957 '.split()

print(*range(1, 8))

for i in permutations('abcdefg'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)