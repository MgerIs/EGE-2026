cnt= 0
s = []
a = [int(x) for x in open("17_15333.txt")]
mx19 = max(x for x in a if x%19==0)
for p,v in zip(a,a[1:]):
    c1 = (p>mx19) + (v>mx19) >= 1
    s1 = p+v
    if c1: s.append(s1)
print(len(s),max(s))
