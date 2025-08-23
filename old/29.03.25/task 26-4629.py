with open("26_4629.txt") as file:
    N = int(file.readline())
    cost = []
    costs = file.readlines()
    for i in costs:
        cost.append(int(i))
    print(cost)
sale = N//4
cost.sort()
summ = sum(cost)

print(cost)
print(cost[::-1])
ans1 = sum(cost[:-sale]) + sum(cost[-sale:]) // 2 # customer
print(ans1)
ans2 = sum(cost[sale:]) + sum(cost[:sale]) // 2 # commercial
print(ans2)