def f(s,cnt):
    if cnt == 15:
        mn.add(s)
        return
    f(s+10,cnt+1)
    f(s-5,cnt+1)

mn = set()
f(0,0)
print(len(mn))