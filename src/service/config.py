import json
from ClusterShell.NodeSet import *

config = {
	"services" : {}
}

def fetchNodes(service, action, blacklist=[]) :
	global config

	nodes = []

	if service in config['services'] :
		if not action in ['status'] :
			for dependency in config['services'][service]['dependencies'] :
				if not dependency in blacklist :
					blacklist.append(dependency)
					nodes.extend(fetchNodes(dependency, action, blacklist))
		for nodeset in map(str, config['services'][service]['nodes']) :
			daemon = config['services'][service]['daemon']
			for node in expand(nodeset) :
				manager = config['managers'][config['nodes'][node]['manager']]
				nodes.append((service, daemon, manager, node))
	elif service in config['groups'] :
		for subservice in config['groups'][service]:
			if not subservice in blacklist :
				blacklist.append(subservice)
				nodes.extend(fetchNodes(subservice, action, blacklist))

	return nodes


def checkAction(service, action) :
	global config

	if service in config['services'] :
		return (action in config['services'][service]['actions'])

	return True


def listActions(service) :
	global config

	actions = ''

	if service in config['services'] :
		actions = '{' + '|'.join(config['services'][service]['actions']) + '}'

	return actions


def load(filename = 'cs-services.json') :
	global config
	configfd = open(filename, 'r')

	config = json.load(configfd)

	configfd.close()

def save(filename = 'cs-services.json') :
	global config
	configfd = open(filename, 'w')

	json.dump(config, configfd, indent=1)

	configfd.close()
