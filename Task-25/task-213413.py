def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sixseven(n):
    return str(n).count('6') == 1


def solve():
    start_number = 6086055 + 1
    cnt = 0
    current_num = start_number

    ans = []
    while cnt < 5:
        d = -1
        for i in range(2, int(current_num**0.5) + 1):
            if current_num % i == 0:
                d = i
                break
        if d != -1:
            p1 = d
            p2 = current_num // d

            if is_prime(p2):
                if sixseven(p1) and sixseven(p2):
                    ans.append((current_num, max(p1, p2)))
                    cnt += 1
        current_num += 1
    for res in ans:
        print(res[0],res[1])
solve()
