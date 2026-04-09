cnt = 0
s = []
a = [int(x) for x in open("17_21595.txt")]
mx = [i for i in a if len(str(abs(i)))==4 and str(i)[-1]=="3"]
lmx = len(mx)
for p,v,t in zip(a,a[1:],a[2:]):
    sp = sorted([p,v,t])[::-1]
    u1 = sp[0] + sp[1] > lmx**2
    s1 = p+v+t
    if u1:s.append(s1)
print(len(s),max(s))
