def convert(num,sys):
    res = ""
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]
max_prod = []
for x in range(1, 100):
    for y in range(1, 100):
        val = 5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x
        if val > 0:
            res = convert(val,5)
            if res.count('0') == 10:
                ans = x*y
                max_prod.append(ans)
print(max(max_prod))
print(int("1010111111",2))