#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "$0 must be run as root"
	exit 1
fi

brctl addbr xenbr0
ifup xenbr0
dnsmasq -z -i xenbr0 --pid-file=dnsmasq.pid

sysctl net.ipv4.ip_forward=1
iptables -t nat -A POSTROUTING -s 172.16.10.0/24 -j MASQUERADE

xl create /etc/xen/node1.cfg
xl create /etc/xen/node2.cfg
xl create /etc/xen/node3.cfg
xl create /etc/xen/node4.cfg
xl create /etc/xen/node5.cfg
xl create /etc/xen/node6.cfg
xl create /etc/xen/node7.cfg
xl create /etc/xen/node8.cfg