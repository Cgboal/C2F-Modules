#!/usr/bin/env python
from c2sdk import rest
from netaddr import IPNetwork, iter_unique_ips
import os
import socket
import fcntl
import struct
import subprocess

local_ip = os.environ["LOCAL_IP"]
netmask = os.environ["NETMASK"]

cidr = IPNetwork(local_ip+"/"+netmask).cidr
print str(cidr)
alive_hosts = []

for ip in iter_unique_ips(cidr):
    res = subprocess.call(['ping', '-c', '1', '-t', '1', str(ip)])
    if res == 0:
        alive_hosts.append(ip)
print alive_hosts

http = rest.Rester()
http.post("PingSweepResult", {"subnet":  str(cidr), "hosts_alive": ",".join(alive_hosts)})

