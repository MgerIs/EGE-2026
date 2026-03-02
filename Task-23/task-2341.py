s = {1}
for p in range(8):
    s = {x+1 for x in s} | {x+5 for x in s} | {x*3 for x in s}
ans = [x for x in s if 1000 <= x <= 1024]
print(len(ans))
