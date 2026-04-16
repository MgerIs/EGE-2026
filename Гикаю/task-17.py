cnt = 0
s = []
a = [int(x) for x in open("17_23757.txt")]
mn2 = min(x for x in a if 10<=x<=99)
for p,v in zip(a,a[1:]):
    c1 = (10<=p<=99)+(10<=v<=99)==1
    c2 = (p+v) % mn2 == 0
    s2 = p+v
    if c1 and c2: s.append(s2)
print(len(s),max(s))