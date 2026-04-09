from ipaddress import *
ans = []
for A in range(256):
    net = ip_network(f"192.214.{A}.184/255.255.255.224",False)
    for i in net:
        ok = True
        i = f"{int(i):032b}"
        if i.count("1") <= 15:
            ok = False
            break
    if ok:
        ans.append(A)
print(min(ans))