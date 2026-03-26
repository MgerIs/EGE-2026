with open(r"files/09_9778.txt") as file:
    data = [list(map(int, x.split())) for x in file]
for pos, line in enumerate(data, start=1):
    cnt = [line.count(i) for i in set(line)]
    if sorted(cnt) == [1, 1, 1, 1, 2]:
        pov = [i for i in line if line.count(i) > 1]
        nepov = [i for i in line if line.count(i) == 1]
        if sum(nepov) / len(nepov) <= pov[0]:
            print(pos)
            break