#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "$0 must be run as root"
	exit 1
fi

xl shutdown node1
xl shutdown node2
xl shutdown node3
xl shutdown node4
xl shutdown node5
xl shutdown node6
xl shutdown node7
xl shutdown node8