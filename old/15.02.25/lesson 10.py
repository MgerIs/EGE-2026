#task-24
with open("24_25361.txt") as file:
    s = file.read().strip()
n = len(s)
max_len = 0

for start in range(n):
    if s[start] not in "02468":
        continue

    f_cnt = 0
    even_cnt = 0
    right = start

    while right < n and even_cnt <= 1 and f_cnt <= 76:
        if s[right] in "02468":
            even_cnt += 1
        if s[right] == "F":
            f_cnt +=1

        if even_cnt == 1 and f_cnt == 76:
            max_len = max(max_len, right - start + 1)
        right += 1


print(max_len)
