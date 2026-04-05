s  = []
a = [int(x) for x in open("17_23902 (1).txt")]
for p,v,t in zip(a,a[1:],a[2:]):
    u1 = (str(p)[0]==str(p)[-1])+(str(v)[0]==str(v)[-1])+(str(t)[0]==str(t)[-1])==1
    u2 = (p//100%10 ==2 and 1000<=p<=9999) + (v//100%10 == 2 and 1000<=v<=9999) + (t//100%10==2 and 1000<=t<=9999) == 2
    c1 = max(p,v,t)
    if u1 and u2:s.append(c1)

print(len(s),sum(s))
