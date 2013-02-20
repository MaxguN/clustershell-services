from Tkinter import *
from ClusterShell.Task import NodeSet

class ServiceseditFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)

		self.services = serviceslist = Listbox(frame, exportselection=0, height=10, width=15)
		self.name = nameinput = Entry(frame)
		self.daemon = daemoninput = Entry(frame)
		self.dependencies = dependencieslist = Listbox(frame, exportselection=0)
		self.nodes = nodeslist = Listbox(frame, exportselection=0)
		self.start = IntVar() 
		self.stop = IntVar()
		self.restart = IntVar()
		self.status = IntVar()

		serviceadd = Button(frame, text="+")
		self.servicedel = servicedel = Button(frame, text="-")
		namelabel = Label(frame, text="Name :")
		daemonlabel = Label(frame, text="Daemon :")
		dependencieslabel = Label(frame, text="Dependencies :")
		self.dependencyadd = dependencyadd = Button(frame, text="+")
		self.dependencydel = dependencydel = Button(frame, text="-")
		nodeslabel = Label(frame, text="Nodes :")
		self.nodeadd = nodeadd = Button(frame, text="+")
		self.nodedel = nodedel = Button(frame, text="-")
		actionslabel = Label(frame, text="Actions :")
		startcheck = Checkbutton(frame, text="start", variable=self.start)
		stopcheck = Checkbutton(frame, text="stop", variable=self.stop)
		restartcheck = Checkbutton(frame, text="restart", variable=self.restart)
		statuscheck = Checkbutton(frame, text="status", variable=self.status)
		self.savebutton = savebutton = Button(frame, text="Save")
		backbutton = Button(frame, text="Back")

		serviceslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		serviceadd.grid(row=4, column=0, sticky=W)
		servicedel.grid(row=4, column=0, sticky=E)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2, columnspan=3, sticky=W)
		daemonlabel.grid(row=1, column=1, sticky=W)
		daemoninput.grid(row=1, column=2, columnspan=3, sticky=W)
		dependencieslabel.grid(row=2, column=1, sticky=W)
		dependencieslist.grid(row=3, column=1, columnspan=2, sticky=W+N+S+E)
		dependencyadd.grid(row=4, column=1)
		dependencydel.grid(row=4, column=2)
		nodeslabel.grid(row=2, column=3, sticky=W)
		nodeslist.grid(row=3, column=3, columnspan=2, sticky=W+N+S+E)
		nodeadd.grid(row=4, column=3)
		nodedel.grid(row=4, column=4)
		actionslabel.grid(row=5, column=1)
		startcheck.grid(row=5, column=2)
		stopcheck.grid(row=6, column=2)
		restartcheck.grid(row=5, column=3)
		statuscheck.grid(row=6, column=3)
		backbutton.grid(row=7, column=3)
		savebutton.grid(row=7, column=4)

		backbutton['command'] = application.switchtoservices

		serviceadd['command'] = self.addservice
		servicedel['command'] = self.delservice
		dependencyadd['command'] = self.dependencyselector
		dependencydel['command'] = self.deldependency
		nodeadd['command'] = self.nodeselector
		nodedel['command'] = self.delnode
		backbutton['command'] = self.back
		savebutton['command'] = self.save

		servicedel['state'] = DISABLED
		dependencyadd['state'] = DISABLED
		dependencydel['state'] = DISABLED
		nodeadd['state'] = DISABLED
		nodedel['state'] = DISABLED
		savebutton['state'] = DISABLED

		self.loadservices()

		self.services.bind('<ButtonRelease-1>', self.selectservice)
		self.name.bind('<KeyRelease>', self.edited)
		self.daemon.bind('<KeyRelease>', self.edited)
		self.dependencies.bind('<ButtonRelease-1>', self.selectdependency)
		self.nodes.bind('<ButtonRelease-1>', self.selectnode)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.clear()
		self.services.selection_clear(0, END)
		self.frame.grid_forget()

	def clearservices(self) :
		self.services.delete(0, END)

	def loadservices(self) :
		for service in self.application.config['services'] :
			self.services.insert(END, service)

	def reloadservices(self, keepselection=True) :
		selection = 0
		if keepselection and self.services.curselection() :
			selection = self.services.curselection()[0]
		self.clearservices()
		self.loadservices()
		if keepselection :
			self.services.selection_set(selection)
			self.selectservice()

	def clear(self) :
		self.name.delete(0, END)
		self.daemon.delete(0, END)
		self.dependencies.delete(0, END)
		self.nodes.delete(0, END)
		self.dependencyadd['state'] = DISABLED
		self.dependencydel['state'] = DISABLED
		self.nodeadd['state'] = DISABLED
		self.nodedel['state'] = DISABLED

	def load(self, service) :
		config = self.application.config['services'][service]
		self.name.insert(0, service)
		self.daemon.insert(0, config['daemon'])
		for dependency in config['dependencies'] :
			self.dependencies.insert(END, dependency)
		for node in config['nodes'] :
			self.nodes.insert(END, node)

	def selectservice(self, event=None) :
		service = self.services.get(self.services.curselection()[0])
		self.clear()
		self.load(service)
		self.servicedel['state'] = NORMAL
		self.dependencyadd['state'] = NORMAL
		self.nodeadd['state'] = NORMAL

	def selectdependency(self, event) :
		self.dependencydel['state'] = NORMAL

	def selectnode(self, event) :
		self.nodedel['state'] = NORMAL

	def dependencyselector(self) :
		selection = self.application.config['services'].keys()
		self.application.openselector(selection, self.adddependency)

	def nodeselector(self) :
		selection = self.application.config['nodes'].keys()
		self.application.openselector(selection, self.addnode, EXTENDED)

	def addservice(self) :
		self.services.selection_clear(0, END)
		self.clear()
		self.services.insert(END, 'new_service')
		self.name.insert(0, 'new_service')
		self.services.selection_set(END)
		self.dependencyadd['state'] = NORMAL
		self.nodeadd['state'] = NORMAL

	def delservice(self) :
		service = self.services.get(self.services.curselection()[0])
		config = self.application.config
		self.services.delete(self.services.curselection()[0])
		if service in config['services'] :
			del config['services'][service]
		self.application.save()
		self.application.reloadservices()

	def adddependency(self, dependency) :
		self.dependencies.insert(END, dependency)
		self.edited()

	def deldependency(self) :
		self.dependencies.delete(self.dependencies.curselection()[0])
		self.edited()

	def addnode(self, nodelist) :
		self.nodes.insert(END, unicode(NodeSet.fromlist(map(str, nodelist))))
		self.edited()

	def delnode(self) :
		self.nodes.delete(self.nodes.curselection()[0])
		self.edited()

	def save(self) :
		service = self.services.get(self.services.curselection()[0])
		config = self.application.config
		if service in config['services'] :
			del config['services'][service]
		service = self.name.get()
		config['services'][service] = {
			"daemon" : self.daemon.get(),
			"dependencies" : list(self.dependencies.get(0, END)),
			"nodes" : list(self.nodes.get(0, END)),
			"actions" : ["start", "stop", "restart", "status"]
		}
		self.application.save()
		self.savebutton['state'] = DISABLED
		self.application.reloadservices()

	def back(self) :
		self.application.switchtoservices()

	def edited(self, event=None) :
		if self.services.curselection() :
			self.savebutton['state'] = NORMAL