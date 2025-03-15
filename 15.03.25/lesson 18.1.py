# Список заполняется сотней псевдослучайными целыми числами в диапазоне от 0 до 1_000_000.
# Ищется среднее арифметической от значений всех элементов списка и выводится на экран.
# На экран выводится список элементов, значение которых меньше среднего арифметического.
from random import randint

data = []
l4 = []
for i in range(100):
    data.append(randint(1, 1_000_000))
l1 = sum(data)
l2 = len(data)
l3 = l1 / l2
for i in range(100):
    if data[i] < l3:
        l4.append(data[i])
print(l4)



data = []
l4 = []
for i in range(100):
    data.append(randint(1, 1_000_000))
l1 = min(data)
l2 = max(data)

ind = data.index(l1)
ind2 = data.index(l2)

print(data[min(ind,ind2)+1: max(ind2,ind)])


data = []
l4 = []
for i in range(100):
    data.append(randint(1, 1000))

data[0],data[-1] = data[-1], data[0]
print(data)




