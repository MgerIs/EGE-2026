with open(r"files/9_9832.txt") as file:
    data = [list(map(int, x.split())) for x in file]
for line in data:
    u1 = [line.count(i) for i in line]
    if u1.count(2) == 4 and u1.count(1) == 3:
        if line.count(max(line)) == 1:
            print(sum(line))
            break