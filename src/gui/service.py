from ClusterShell.Task import task_self, NodeSet
from threading import Thread

class Service(Thread):
	def __init__(self, config) :
		Thread.__init__(self)
		self.config = config
		self.action = ''
		self.nodes = []
		self.callback = None

	def set(self, action, service, callback) :
		self.action = action
		self.nodes = self.config.fetchNodes(service, action)
		self.callback = callback

	def run(self) :
		task = task_self()
		for service, manager, daemon, node in self.nodes:
			task.shell(manager + daemon + ' ' + self.action, nodes=node)
		task.run()
		self.callback(task)
