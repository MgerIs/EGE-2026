with open("26_4956.txt") as file:
    N, M = map(int,file.readline().split())
    cheap = {}
    exp = {}
    for i in file:
        price, status = map(int,i.split())
        if price <= M:
            if price in cheap:
                cheap[price][status] += 1
            else:
                cheap[price] = [0,0]
                cheap[price][status] += 1
        else:
            if price in exp:
                exp[price][status] += 1
            else:
                exp[price] = [0, 0]
                exp[price][status] += 1
popular_cheap = min(cheap)
for product in cheap:
    if cheap[popular_cheap][1] < cheap[product][1]:
        popular_cheap = product
print(popular_cheap)
print(cheap)
pop_exp = min(exp)
for product in exp:
    if exp[pop_exp][1] < exp[product][1]:
        pop_exp = product
print(pop_exp)
print(exp)
revenue = popular_cheap * cheap[popular_cheap][1] + pop_exp * exp[pop_exp][1]
in_stock =cheap[popular_cheap][0] + exp[pop_exp][0]
print(revenue)
print(in_stock)