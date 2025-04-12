with open("26_21424.txt") as file:
    N = int(file.readline())
    sizes = [int(i) for i in file]


sizes.sort(reverse=True)
last = sizes[0]
cnt = 1


for i in sizes:
    if last - i >= 9:
        cnt += 1
        last = i

print(cnt, last)



with open("26_7602.txt") as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]




cells = [0] * K
cnt = 0
last_cell = 1
a = sorted(times)
print(a)

for time in times:
    for i in range(K):
        if time[0] >= cells[i]:
            cell = time[1] + 1
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)

