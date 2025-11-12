ans = []
def f(n):
    chet = sum([1 for i in n if int(i,8)%2==0])
    return chet

for N in range(1,100000):
    R = f"{N:o}"
    if f(R) %2 == 0:
        R = R[-3:]  + "46"
    else:
        R = f"{(N%8*5):o}"+R
    R = int(R,8)
    if N >=80:
        ans.append(R)
print(min(ans))
