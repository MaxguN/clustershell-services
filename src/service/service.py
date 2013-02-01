#!/usr/bin/python

import sys
import config
from ClusterShell.Task import task_self, NodeSet

service = ''
action = ''
nodes = ''

if len(sys.argv) == 4 :
	service = sys.argv[1]
	action = sys.argv[2]
	nodes = sys.argv[3]
elif len(sys.argv) == 3 :
	config.load()

	service = sys.argv[1]
	action = sys.argv[2]
	nodes = map(unicode.encode, config.fetchNodes(service))
	
	if len(nodes) == 0 :
		print 'Service ' + service + ' not found'
		exit(2)

	nodes = NodeSet.fromlist(nodes)
else :
	print 'Usage : ' + sys.argv[0] + ' <service> <action> <node_list>'
	exit(1)

task = task_self()
task.run('service ' + service + ' ' + action, nodes=nodes)

for output, nodeset in task.iter_buffers():
	# for node in nodeset:
	# 	print node, output
	print NodeSet.fromlist(nodeset), output