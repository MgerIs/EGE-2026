def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1,100000):
    R = convert(N,3)
    if N % 3 != 0:
        R = "1"+R+R[-3:]
    else:
        sum_d = sum(map(int, R))
        sum_d = (convert(sum_d,3) * 8)
        R += sum_d
    R = int(R, 3)
    if 1200 < R < 1300:
        ans.append(R)
print(ans)