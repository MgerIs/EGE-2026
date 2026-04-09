from ipaddress import *

ans = []
for a in range(256):
    net = ip_network(f"116.242.{a}.26/255.255.255.224", False)
    for i in net:
        i = f"{int(i):08b}"
        if i[:16].count("1") >= i[-16:].count("1"):
            ans.append(a)
print(max(ans))