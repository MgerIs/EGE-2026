ans = []
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for N in range(1,10000):
    R = convert(N,3)
    if N % 5 == 0:
        R = R + convert(N,3)[-2:]
    else:
        R = R + convert(7*(N%5),3)
    R = int(R,3)
    if R<=273:
        ans.append(N)
print(max(ans))