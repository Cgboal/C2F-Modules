#!/usr/bin/env python
from c2sdk import rest
from netaddr import IPNetwork, iter_unique_ips
import socket
import fcntl
import struct
import subprocess

iface = "eth0"
netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface))[20:24])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
cidr = IPNetwork(local_ip+"/"+netmask).cidr
print str(cidr)
alive_hosts = []

for ip in iter_unique_ips(cidr):
    res = subprocess.call(['ping', '-c', '3', str(ip)])
    if res == 0:
        alive_hosts.append(ip)
print alive_hosts
#rest.post("PingSweepResult", {"subnet": (cidr), "hosts_alive": ",".join(alive_hosts)})str