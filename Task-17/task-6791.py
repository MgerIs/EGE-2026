s = []
cnt = 0
a = [int(x) for x in open("17_6791.txt")]
minsq68 = min(int(x) for x in a if abs(x)%100 == 68)
for p,v in zip(a,a[1:]):
    c1 = (abs(p)%100 == 68) + (abs(v)%100==68) == 1
    c2 = (p**2 + v**2) >= minsq68**2
    u1 = (p**2+v**2)
    if c1 and c2: s.append(u1)
print(len(s), max(s))


