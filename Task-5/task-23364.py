def convert(num,sys):
    res = ""
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1,100000):
    R = convert(N,3)
    if N % 3 == 0:
        R = "1" + R + "02"
    else:
        R = R + convert((N%3)*4,3)
    R = int(R,3)
    if R<100:
        ans.append(N)
print(max(ans))