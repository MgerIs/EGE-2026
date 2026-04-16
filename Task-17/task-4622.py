
cnt = []
s = 0
a=[int(x) for x in open("files/17_4622.txt")]
for p,v in zip(a, a[1:]):
    numm = min( i for i in a if i> 0 and i%19==0)
    c1 = (p+v<numm) == 1
    s3 = p+v
    if c1: cnt.append(s3)
print(len(cnt),abs(max(cnt)))