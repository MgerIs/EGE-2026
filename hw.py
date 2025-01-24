# 1
a = int(input())
if a % 10 == 0:
    print(a)
elif a % 5 == 0:
    print(a)
elif a % 2 == 0:
    print(a)
else:
    print(a + 1)

# 2
a = int(input())
if a > 0:
    print(a + 1)
else:
    print(a - 1)

# 3
for i in range(0, 100):
    if i % 3 == 0:
        print(i / 3)
    else:
        print(i * 2)

# 4
x = int(input())
if x > 0:
    print(2 * x + 5)
if x == 0:
    print(x)
if x < 0:
    print(x ** 2 - 1)

# 5
for i in range(100, 999):
    if i % 2 == 1:
        print(i)
    else:
        print("нет такого друган")
