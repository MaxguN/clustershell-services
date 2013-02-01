#!/bin/sh

if [ "$(id -u)" != "0" ]; then
	echo "$0 must be run as root"
	exit 1
fi

ssh node1 "\
	echo \"Installing services on node1\";\
	apt-get update > /dev/null;\
	apt-get install -y isc-dhcp-server proftpd;\
	echo \"Finished installing services on node1\";"
ssh node2 "\
	echo \"Installing services on node2\";\
	apt-get update > /dev/null;\
	apt-get install -y isc-dhcp-server proftpd;\
	echo \"Finished installing services on node2\";"
ssh node3 "\
	echo \"Installing services on node3\";\
	apt-get update > /dev/null;\
	apt-get install -y bind9;\
	echo \"Finished installing services on node3\";"
ssh node4 "\
	echo \"Installing services on node4\";\
	apt-get update > /dev/null;\
	apt-get install -y bind9 proftpd;\
	echo \"Finished installing services on node4\";"
ssh node5 "\
	echo \"Installing services on node5\";\
	apt-get update > /dev/null;\
	apt-get install -y ntp proftpd;\
	echo \"Finished installing services on node5\";"
ssh node6 "\
	echo \"Installing services on node6\";\
	apt-get update > /dev/null;\
	apt-get install -y ntp;\
	echo \"Finished installing services on node6\";"
ssh node7 "\
	echo \"Installing services on node7\";\
	apt-get update > /dev/null;\
	apt-get install -y ntp proftpd;\
	echo \"Finished installing services on node7\";"
ssh node8 "\
	echo \"Installing services on node8\";\
	apt-get update > /dev/null;\
	apt-get install -y ntp proftpd;\
	echo \"Finished installing services on node8\";"