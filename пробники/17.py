s=[]
a = [int(x) for x in open("17_11236 (2).txt")]
mn1 = min(i for i in a if len(str(abs(i)))==2)**2
mx1 = abs(max(i for i in a if str(i)[-1]=="1" and len(str(abs(i)))==4))
print(mx1)
for p,v,t in zip(a,a[1:],a[2:]):
    u1 = (p>mn1)+(v>mn1)+(t>mn1) == 2
    u2 = ((abs(p)*abs(v)*abs(t))%mx1==0)
    c1 = (abs(p)+abs(v)+abs(t))
    if u1 and u2: s.append(c1)
print(len(s),max(s))

