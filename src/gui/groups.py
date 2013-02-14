from Tkinter import *

class GroupsFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)

		self.groups = groupslist = Listbox(frame, height=10, width=15)
		self.nodes = nodeslist = Listbox(frame, selectmode=EXTENDED)

		nodelabel = Label(frame, text="Nodes :")
		editbutton = Button(frame, text="Edit")
		startbutton = Button(frame, text="Start")
		stopbutton = Button(frame, text="Stop")
		restartbutton = Button(frame, text="Restart")
		statusbutton = Button(frame, text="Status")

		groupslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		nodelabel.grid(row=0, column=1, sticky=W)
		nodeslist.grid(row=1, column=1, columnspan=4,sticky=W+N+S+E)
		editbutton.grid(row=4, column=0, sticky=W+E)
		startbutton.grid(row=4, column=1, sticky=W)
		stopbutton.grid(row=4, column=2, sticky=W)
		restartbutton.grid(row=4, column=3, sticky=W)
		statusbutton.grid(row=4, column=4, sticky=W)

		editbutton['command'] = application.switchtogroupsedit

		self.loadgroups()

		self.groups.bind('<ButtonRelease-1>', self.selectgroup)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
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
		self.nodes.delete(0, END)

	def loadnodes(self, group) :
		if group in self.application.config['services'] :
			service = group
			for node in self.application.config['services'][service]['nodes'] :
				self.nodes.insert(END, node + '-' + service)
		else :
			for service in self.application.config['groups'][group] :
				self.loadnodes(service)

	def selectgroup(self, event) :
		group = self.groups.get(self.groups.curselection()[0])
		self.clearnodes()
		self.loadnodes(group)