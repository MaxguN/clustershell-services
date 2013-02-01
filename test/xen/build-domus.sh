#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "$0 must be run as root"
	exit 1
fi

xen-create-image --force --config=`pwd`/node1.conf

mkdir disks/iso
mount disks/domains/node1/disk.img disks/iso

xen-create-image --force --config=`pwd`/node2.conf --install-source=disks/iso
xen-create-image --force --config=`pwd`/node3.conf --install-source=disks/iso
xen-create-image --force --config=`pwd`/node4.conf --install-source=disks/iso
xen-create-image --force --config=`pwd`/node5.conf --install-source=disks/iso
xen-create-image --force --config=`pwd`/node6.conf --install-source=disks/iso
xen-create-image --force --config=`pwd`/node7.conf --install-source=disks/iso
xen-create-image --force --config=`pwd`/node8.conf --install-source=disks/iso

umount disks/iso
rmdir disks/iso