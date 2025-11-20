#проверка числа на простоту
a = int(input())
num = 0
for i in range(2, int(a**0.5)+1):
    if a % i == 0:
        num += 1
if num == 0:
        print("число простое")
else:
        print("непростое")

from time import time

# Проверка числа на простоту
num = int(input())

start = time()
# Первый способ без оптимизации
for i in range(2, num): # 17
    if num % i == 0:
        print('Число непростое')
        break
else:
    print('Число простое')
print(time() - start)

start = time()
# Второй способ с оптимизацией в два раза
for i in range(2, num // 2 + 1): # 17
    if num % i == 0:
        print('Число непростое')
        break
else:
    print('Число простое')
print(time() - start)

start = time()
# Третий способ самый эффективный
for i in range(2, int(num ** 0.5) + 1): # 17
    if num % i == 0:
        print('Число непростое')
        break
else:
    print('Число простое')
print(time() - start)







a = int(input())
if a%2 == 0:
    for i in ram #перебор ток четных
else:













from functools import*
def H(p):
    return p-3, p-5, p//2
@lru_cache(None)
def f(p):
    if p <= N: return "L"
    return "W" if any(f(h)=="L" for h in H(p)) else "L"
@lru_cache(None)
def c(p):
    if p <= N:
        return 0
    if f(p) == "L": return 1+max(c(h) for h in H(p))
    return 1+min(c(h) for h in H(p) if f(h)=="L")
print("19:", [s for s in range(1,N) if c(s)==2])
print("20:", [s for s in range(1,N) if c(s)==3])
print("21:", [s for s in range(1,N) if c(s)==4])

