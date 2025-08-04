st = input()
cnt = 1
m = 1
for i in range(0, len(st)-1 ):
    if st[i] in "ABC" and st[i+1] in "89" or \
            st[i] in "89" and st[i+1] in "ABC":
        cnt += 1
        if cnt > m:
            m = cnt
    else:
        cnt = 1
print(m)



