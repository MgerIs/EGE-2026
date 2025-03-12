a = input()
a = a.split()
cnt = 0
print(a)
for i in range(len(a)):
    if a[i].count("-")%2 != 0:
        cnt += 1
print(cnt)
