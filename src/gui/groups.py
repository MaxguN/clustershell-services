from Tkinter import *
from ClusterShell.Task import NodeSet

class GroupsFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)

		self.groups = groupslist = Listbox(frame, exportselection=0, height=10, width=15)
		self.nodes = nodeslist = Message(frame, width=500)

		nodelabel = Label(frame, text="Nodes :")
		editbutton = Button(frame, text="Edit")
		self.buttons = buttons = {
			"start" : Button(frame, text="Start"),
			"stop" : Button(frame, text="Stop"),
			"restart" : Button(frame, text="Restart"),
			"status" : Button(frame, text="Status")
		}

		groupslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		nodelabel.grid(row=0, column=1, sticky=W)
		nodeslist.grid(row=1, column=1, columnspan=4,sticky=W+N)
		editbutton.grid(row=4, column=0, sticky=W+E)
		buttons['start'].grid(row=4, column=1, sticky=W)
		buttons['stop'].grid(row=4, column=2, sticky=W)
		buttons['restart'].grid(row=4, column=3, sticky=W)
		buttons['status'].grid(row=4, column=4, sticky=W)

		editbutton['command'] = application.switchtogroupsedit

		buttons['start']['command'] = lambda : self.application.do('start', groupslist.get(groupslist.curselection()[0]), self.display)
		buttons['stop']['command'] = lambda : self.application.do('stop', groupslist.get(groupslist.curselection()[0]), self.display)
		buttons['restart']['command'] = lambda : self.application.do('restart', groupslist.get(groupslist.curselection()[0]), self.display)
		buttons['status']['command'] = lambda : self.application.do('status', groupslist.get(groupslist.curselection()[0]), self.display)

		self.loadgroups()

		self.groups.bind('<ButtonRelease-1>', self.selectgroup)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.clearnodes()
		self.groups.selection_clear(0, END)
		self.frame.grid_forget()

	def cleargroups(self) :
		self.groups.delete(0, END)

	def loadgroups(self) :
		for group in self.application.config['groups'] :
			self.groups.insert(END, group)

	def reloadgroups(self) :
		self.cleargroups()
		self.loadgroups()

	def clearnodes(self) :
		self.nodes['text'] = ''

	def loadnodes(self, group) :
		if group in self.application.config['services'] :
			service = group
			for node in self.application.config['services'][service]['nodes'] :
				self.nodes['text'] += node + '-' + service + '\n'
		else :
			for service in self.application.config['groups'][group] :
				self.loadnodes(service)

	def display(self, task) :
		self.clearnodes()
		for output, nodeset in task.iter_buffers() :
			self.nodes['text'] += str(NodeSet.fromlist(nodeset)) + ' ' + str(output) + '\n'

	def selectgroup(self, event) :
		group = self.groups.get(self.groups.curselection()[0])
		self.clearnodes()
		self.loadnodes(group)

	def enableactions(self, actions=[]) :
		for button in self.buttons :
			self.buttons[button]['state'] = DISABLED
		for action in actions :
			if action in self.buttons :
				self.buttons[action]['state'] = NORMAL