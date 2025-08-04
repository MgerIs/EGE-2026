#expirence
#в этой задаче мы столкнулись с разными методами переворота строк
#наш эксперимент заключался в том чтобы узнать какой из методов оптимизированее
#путем несложных вычислений узнаем что команда reverse работает практически в 9 раз быстрее
#исходя из всего вышенаписанного мною сделаю вывод что в будущем буду использовать команду reverse
from random import randint
from timeit import timeit


def f1(l1):
    l1 = l1[::-1]


def f2(l1):
    l1.reverse()


l1 = []
from timeit import timeit
from random import randint


def f1(data):
    data.reverse()


def f2(data):
    data = data[::-1]


data = []
for i in range(1000):
    data.append(randint(1, 1_000_000))

print(timeit('f1(data)', globals=globals(), number=10_000_000))
print(timeit('f2(data)', globals=globals(), number=10_000_000))


print(timeit('f1(l1)', globals=globals(), number=10_000_000))
print(timeit('f2(l1)', globals=globals(), number=10_000_000))

