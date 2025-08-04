#task 7274 26
with open('26_7274.txt') as file:
    N = int(file.readline())
    trees = []
    for i in file:
        row, col = map(int, i.split())
        trees.append([row,col])
trees.sort()
ans = []
for i in range(N-1):
    first, second = trees[i], trees[i+1]
    if first[0] == second[0] and second[1] - first[1] == 13:
        ans.append([first,second])
print(max(ans))






