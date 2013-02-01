import json

config = {}

def fetchNodes(service):
	global config

	if config['services'].has_key(service) :
		return config['services'][service]['nodes']
	elif config['groups'].has_key(service) :
		nodes = []
		for subservice in config['groups'][service]:
			nodes = nodes + config['services'][subservice]['nodes']
		return nodes
	else :
		return []

def load(filename = 'cs-services.json'):
	global config
	configfd = open(filename, 'r')

	config = json.load(configfd)

	configfd.close()
