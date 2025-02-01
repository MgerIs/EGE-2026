# 1
a = int(input())

count = 0
while a != 0:
    a //= 10
    count += 1
print(count)

# 2
ans = 1
a = int(input())
while a:
    ans *= a % 10
    a //= 10
print(ans)

# 3
num = int(input())
a = 0
while num:
    a = a * 10 + num % 10
    num //= 10
print(a)

# 4
a = int(input())
x = 0
for i in range(2, a // 2 + 1):  # 7
    if a % i == 0:
        x += 1
if x == 0:
    print('все четко число простое зачилься')
else:
    print("число непростое осади его да")

# 5
# хз как делать сорямбус:((
d = "s"
v = "o"
a = "r"
t = "r"
e = "e"
b = "k"
e = "e"
l = "n"
o = "t"
h = ":(( crying sad disrep"
print(d + v + a + t + e + b + e + l + o + h)
