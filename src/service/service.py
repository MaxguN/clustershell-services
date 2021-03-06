#!/usr/bin/python

import sys
import config
from ClusterShell.Task import task_self, NodeSet

action = ''
nodes = {}

if len(sys.argv) == 4 :
	action = sys.argv[2]
	nodes = [(sys.argv[1], 'service ', sys.argv[1], sys.argv[3])]
elif len(sys.argv) == 3 :
	config.load()

	action = sys.argv[2]
	nodes = config.fetchNodes(sys.argv[1], action)
	
	if len(nodes) == 0 :
		print 'Service ' + sys.argv[1] + ' not found'
		exit(2)

else :
	print 'Usage : ' + sys.argv[0] + ' <service> <action> <nodeset>'
	exit(1)

task = task_self()

for service, daemon, manager, node in nodes:
	if config.checkAction(service, action) :
		task.shell(manager + daemon + ' ' + action, nodes=node)

	else :
		print 'Action "' + action + '" is not supported by ' + service
		print 'Actions supported : ' + config.listActions(service)
task.run()

for output, nodeset in task.iter_buffers():
	print NodeSet.fromlist(nodeset), output