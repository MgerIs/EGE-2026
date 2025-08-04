#task 3664
with open("26_3664.txt") as file:
    N = int(file.readline())
    trees = []
    for i in file:
        row, place = map(int, i.split())
        trees.append([row,place])
trees.sort()
max_num = []
for i in range(N-1):
    first, second = trees[i], trees[i+1]
    if first[0] == second[0]:
        max_num.append([second[1] - first[1] - 1, first[0]])
print(max(max_num))
