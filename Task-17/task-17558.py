s = []
a = [int(x) for x in open("files/17_17558.txt")]
mn32 = [x for x in a if abs(x)%32==0]
for p,v in zip(a,a[1:]):
    c1 = (p<0) + (v<0) >= 1
    c2 = (p+v) < len(mn32)
    s3 = p+v
    if c1 and c2:s.append(s3)
print(len(s),max(s))