#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "$0 must be run as root"
	exit 1
fi

xl create /etc/xen/node1.cfg
xl create /etc/xen/node2.cfg
xl create /etc/xen/node3.cfg
xl create /etc/xen/node4.cfg
xl create /etc/xen/node5.cfg
xl create /etc/xen/node6.cfg
xl create /etc/xen/node7.cfg
xl create /etc/xen/node8.cfg