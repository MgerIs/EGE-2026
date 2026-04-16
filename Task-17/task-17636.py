s=[int(x) for x in open('files/17_17636.txt')]
a=[int(x) for x in s]
m=-100001
for i in range(len(a)):
    if abs(a[i])%10==3 and (abs(a[i])>99 and abs(a[i])<1000) and a[i]>m:
        m=a[i]
b=[]
for i in range(len(a)-2):
    if ((abs(a[i])%10 == 3 and (abs(a[i])>99 and abs(a[i])<1000)) or
            (abs(a[i+1])%10 == 3 and (abs(a[i+1])>99 and abs(a[i+1])<1000)) or
            (abs(a[i+2])%10 == 3 and (abs(a[i+2])>99 and abs(a[i+2])<1000))):
        if (a[i]+a[i+1]+a[i+2]<m):
            b.append(a[i]+a[i+1]+a[i+2])
print(len(b),max(b))