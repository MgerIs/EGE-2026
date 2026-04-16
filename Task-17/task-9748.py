cnt = []
s = 0
a=[int(x) for x in open("files/17_9748.txt")]
mx15 = max(x for x in a if x%100==15)
for p,v,t in zip(a, a[1:],a[2:]):
    c1= (1000<=p<=9999)+(1000<=v<=9999)+(1000<=t<=9999) == 1
    c2 = ((p+v+t)>=mx15) == 1
    s3 = p+v+t
    if c1 and c2: cnt.append(s3)
print(len(cnt), max(cnt))