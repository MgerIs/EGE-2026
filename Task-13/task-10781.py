from ipaddress import *

ip1 = ip_address("112.117.107.70")
ip2 = ip_address("112.117.121.80")
cnt = 0
for mask in range(10, 32)[::-1]:
    net = ip_network(f"{ip1}/{mask}", False)
    if ip1 in net.hosts() and ip2 in net.hosts():
        print(net.num_addresses)
        break

