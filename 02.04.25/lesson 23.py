from operator import index

with open("26_4684 (3).txt") as file:
    N = int(file.readline())
    price = []
    prices = file.readlines()
    for i in prices:
        price.append(int(i))
    print(price)
sale = N // 6
summ = sum(price)
price.sort()
N = 6
chunks = []
for i in range(0, len(prices), N):
    chunk = price[i:i + N]
    chunks.append(chunk)

shop = sum(price[sale:]) + sum(price[:sale]) // 2
print(shop)
print(chunks)
for i in chunks:
    skidka2 = chunks[i][-1] / 2
