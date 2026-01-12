from itertools import *
from string import printable
def convert(num,sys):
    res = ""
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
cnt = 0
cnt2 = 0
for val in product(printable[:25], repeat=4):
    val = "".join(val)
    for i in convert(val,25):
        if i % 2 == 0:
            cnt +=1
        if cnt == 3:
            cnt2 += 1
print(cnt2)


