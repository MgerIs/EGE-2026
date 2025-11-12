ans = []
def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(1,100000):
    R = convert(N,4)
    if R[0]==3:

print(R)
