#!/usr/bin/python

from ClusterShell.Task import task_self, NodeSet

task = task_self()
task.run("uname -r", nodes="node[1-8]")

for output, nodes in task.iter_buffers():
    print NodeSet.fromlist(nodes), output