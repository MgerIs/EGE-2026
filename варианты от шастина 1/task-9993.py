from math import *
def is_prime(num):
    if num < 2: return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


s = []
a = [int(x) for x in open("17_9993.txt")]
mx = max(i for i in a if abs(i)%100==17)
for num in zip(a,a[1:]):
    u1 = sum(is_prime(i) for i in num)==1
    u2 =abs(sum(num))%mx == 0
    if u1+u2 == 2:
        s.append(prod(num))
print(len(s),max(s))
