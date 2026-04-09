from ipaddress import *

ans = []
for a in range(256):
    net = ip_network(f"217.109.{a}.94/255.255.254.0", False)  # /23
    ok = True
    for i in net:
        s = f"{int(i):032b}"
        left_zeros = s[:16].count("0")
        right_zeros = s[16:].count("0")
        if left_zeros > right_zeros:
            ok = False
            break
    if ok:
        ans.append(a)
print(max(ans))