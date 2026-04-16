a = sorted([int(i) for i in open('26_5066.txt')][1:])
b = []
for x in a:
    for i in range(len(b)):
        if b[i] <= x - 7:
            b[i] = x
            break
    else:
        b.append(x)
cnt  = 0
for i in range(len(a)):
    curr = 0
    lasts = a[i]
    for j in a[i+1:]:
        if j >= lasts + 7:
            curr += 1
            lasts = j
    cnt = max(cnt,curr)
print(len(b), cnt)