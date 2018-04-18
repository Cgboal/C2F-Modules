#!/usr/bin/env python
from c2sdk import rest
from netaddr import IPNetwork
import socket
import fcntl
import struct

iface = "eth0"
netmask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack('256s', iface))[20:24])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
print str(IPNetwork(local_ip+"/"+netmask).cidr)
