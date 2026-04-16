s = []
cnt = 0
a = [int(x) for x in open("files/17_9840.txt")]
mx39 = max(x for x in a if abs(x)%100==39 and 1000<=abs(x)<=9999)
for p,v in zip(a,a[1:]):
    c1 = (1000<=abs(p)<=9999) + (1000<=abs(v)<=9999) == 1
    c2 = (p+v)**2 <= mx39**2
    s3 = p+v
    if c1 and c2: s.append(s3)
print(len(s),max(s))