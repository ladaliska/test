import ipaddress
IP = input()
net = ipaddress.ip_interface(IP)
tmp = str(net.network)
IPwop = tmp.split("/")
print(IPwop[0])
print(net.netmask)
print(net)