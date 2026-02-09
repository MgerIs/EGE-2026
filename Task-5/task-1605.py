ans=[]
for N in range(1,10000):
    R = f"{2+N:b}"
    R = R+str(R.count("1") % 2)
    R = R+str(R.count("1") % 2)
    R = int(R, 2)
    if R < 61:
        ans.append(N)
print(max(ans))
