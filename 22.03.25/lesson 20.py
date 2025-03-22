from random import randint, choices, sample
from math import sqrt
# data2= []
# data = []
# for i in range(15):
#     data.append(randint(1,100))
# data2 = list(map(sqrt, data))
# print(data2)
# data = [5, 6 , 7, 8 , 9, 10]
# print(choices(data))
# print(sample(data, k=3))
# data = []
# data2 = []
# for i in range(10):
#     a = chr(randint(32,127))
#     data += a
# print(data)
# for i in range(10):
#     b = (data[i]*randint(1,20))
#     c = str(b)
#     data2.append(c)
# print(data2)
# print(list(map(len, data2)))
data = []
for i in range(10):
    a = str(i) * randint(1,20)
    data.append(a)
b = (list(map(int, data)))
print(list(map(sqrt, b)))


