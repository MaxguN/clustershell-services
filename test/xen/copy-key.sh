#!/bin/sh

if [ "$(id -u)" != "0" ]; then
	echo "$0 must be run as root"
	exit 1
fi

if [ $# -ne 1 -o ! -f $1 ] ; then
	echo "usage : $0 <public_key>"
	exit 2
fi

ssh-copy-id -i $1 node1
ssh-copy-id -i $1 node2
ssh-copy-id -i $1 node3
ssh-copy-id -i $1 node4
ssh-copy-id -i $1 node5
ssh-copy-id -i $1 node6
ssh-copy-id -i $1 node7
ssh-copy-id -i $1 node8