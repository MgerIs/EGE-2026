from ipaddress import *

net = ip_network("228.172.236.0/255.255.240.0", False)
cnt = 0
for i in net:
    i = f"{int(i):032b}"
    if i.count('1') % 6 != 0 and (i[-1] == "0" and i[-2] == "0" and i[-3] == "0" and i[-4] == "1"):
        cnt += 1
print(cnt)
a ="1234567890abcdefg"
print(a[:8])
print(a[-8:])
