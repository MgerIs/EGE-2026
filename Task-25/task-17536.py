
def f(num):
    d = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            d |= {i, num // i}

    if len(d):
        summ = min(d) + max(d)
        if summ % 10 == 4:
            return summ
    return 0


cnt = 0
for i in range(800001, 10 ** 20):
    M = f(i)
    if M:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break