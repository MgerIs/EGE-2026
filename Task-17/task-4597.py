cnt = []
s = 0
a= [int(x) for x in open("files/17_4597.txt")]
min_num = min(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] % 117 == min_num or a[j] % 117 == min_num:
            s+=1
            cnt.append(a[i]+a[j])
print(s,max(cnt))
