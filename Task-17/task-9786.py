cnt = 0
s = []
a = [int(x) for x in open("files/17_9786.txt")]
mx25 = max(x for x in a if abs(x)%100==25)
for p,v,t in zip(a,a[1:],a[2:]):
    c1 = (1000<=abs(p)<=9999)+(1000<=abs(v)<=9999)+(1000<=abs(t)<=9999) <= 2
    c2 = (p+v+t)<=mx25
    s3 = p+v+t
    if c1 and c2: s.append(s3)
print(len(s),max(s))