with open("26_9077.txt") as file:
    M, N = map(int,file.readline().split())
    scooters = []
    for i in file:
        a = list(map(int,i.split()))
        scooters.append(a)
parking = {}
for i in range(1,M+1):
    parking[i] = []
scooters.sort(key=lambda x:(x[0], x[1]))
print(scooters)
print(parking)
for i in scooters:
    if i[3]