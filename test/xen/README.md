Test - Xen VMs
==============

For testing purpose, we use 8 quantal VMs running with xen 4.1 with a quantal dom0.

The network used is 172.16.10.0/24 with :

* __172.16.10.1__ being dom0
* __172.16.10.1X__ being the domUs with X the number of the node

The VMs are named '__node1-8__'.

The dom0 has a bridge interface configured called '__xenbr0__'

Disk images are stored in `test/xen/disks`

Each VM has those specs :

* 1 vCPU
* 128 MB RAM
* 512 MB Swap
* 5 GB disk

Then all VM running at once only take 1 GB of RAM.


Set up
======

Installing Dom0
---------------

Base Ubuntu 12.10 install.

Install Xen :

	aptitude install xen-hypervisor-4.1-amd64 xen-tools

Change toolstack to `xl`, `xm` is deprecated in 4.2. In `/etc/default/xen` :

	TOOLSTACK=xl

Configure bridge interface in `/etc/network/interfaces` :

	iface xenbr0 inet static
		address 172.16.10.1
		netmask 255.255.255.0
		network 172.16.10.0
		broadcast 172.16.10.255

When booting, choose xen kernel. Reboot on xen kernel for next part.

To enable bridge after boot :

	brctl addbr xenbr0
	ifup xenbr0


Installing DomUs
----------------

Create the first VM :

	xen-create-image --config=`pwd`/node<X>.conf

Create subsequent VMs faster :

	mkdir -p /media/iso
	mount disks/domains/node1/disk.img /media/iso
	xen-create-image --config=`pwd`/node<X>.conf --install-source=/media/iso

Or run install script (it will install all 8 DomUs, erasing any existing one) :

	sh build-domus.sh

Run a VM :

	xl create /etc/xen/node<X>.cfg

Run all VMs :

	sh start-domus.sh

Connect via SSH :

	ssh root@172.16.10.1<X>

or console :

	xl console node<X>

Shutdown when finished :

	xl shutdown node<X>

Or shutdown all VMs :

	sh stop-domus.sh


Configuring DomUs
-----------------

TODO