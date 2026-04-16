s = []
a = [int(x) for x in open("17 (2).txt")]
mx2 = 99
for p,v in zip(a,a[1:]):
    u1 = (10<=p<=99) + (10<=v<=99) == 1
    s1 = (p+v)
    if u1 and (p+v)%99==0:
        s.append(s1)
        print(len(s),max(s))