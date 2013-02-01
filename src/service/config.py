import json
from ClusterShell.Task import NodeSet

config = {}

def fetchNodes(service):
	global config

	nodes = {}

	if config['services'].has_key(service) :
		nodes[config['services'][service]['daemon']] = NodeSet.fromlist(map(unicode.encode, config['services'][service]['nodes']))
	elif config['groups'].has_key(service) :
		for subservice in config['groups'][service]:
			nodes[config['services'][subservice]['daemon']] = NodeSet.fromlist(map(unicode.encode, config['services'][subservice]['nodes']))

	return nodes

def load(filename = 'cs-services.json'):
	global config
	configfd = open(filename, 'r')

	config = json.load(configfd)

	configfd.close()
