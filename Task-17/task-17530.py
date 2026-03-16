s = []
a = [int(x) for x in open("files/17_17530.txt")]
mn = min(x for x in a)
for p,v in zip(a,a[1:]):
    c1 = (p%55==mn)+(v%55==mn)>=1
    s2 = (p+v)
    if c1: s.append(s2)
print(len(s),min(s))