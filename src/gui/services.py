from Tkinter import *

class ServicesFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)

		self.services = serviceslist = Listbox(frame, exportselection=0, height=10, width=15)
		self.nodes = nodeslist = Listbox(frame, exportselection=0, selectmode=EXTENDED)

		nodelabel = Label(frame, text="Nodes :")
		editbutton = Button(frame, text="Edit")
		self.buttons = buttons = {
			"start" : Button(frame, text="Start"),
			"stop" : Button(frame, text="Stop"),
			"restart" : Button(frame, text="Restart"),
			"status" : Button(frame, text="Status")
		}

		serviceslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		nodelabel.grid(row=0, column=1, sticky=W)
		nodeslist.grid(row=1, column=1, columnspan=4,sticky=W+N+S+E)
		editbutton.grid(row=4, column=0, sticky=W+E)
		buttons['start'].grid(row=4, column=1, sticky=W)
		buttons['stop'].grid(row=4, column=2, sticky=W)
		buttons['restart'].grid(row=4, column=3, sticky=W)
		buttons['status'].grid(row=4, column=4, sticky=W)

		editbutton['command'] = application.switchtoservicesedit

		self.loadservices()
		self.enableactions()

		self.services.bind('<ButtonRelease-1>', self.selectservice)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.clearnodes()
		self.services.selection_clear(0, END)
		self.frame.grid_forget()

	def clearservices(self) :
		self.services.delete(0, END)

	def loadservices(self) :
		for service in self.application.config['services'] :
			self.services.insert(END, service)

	def reloadservices(self) :
		self.clearservices()
		self.loadservices()

	def clearnodes(self) :
		while self.nodes.get(0) :
			self.nodes.delete(0)
		self.enableactions()

	def loadnodes(self, service) :
		for node in self.application.config['services'][service]['nodes'] :
			self.nodes.insert(END, node)
		self.nodes.selection_set(0, END)
		self.enableactions(self.application.config['services'][service]['actions'])

	def selectservice(self, event) :
		service = self.services.get(self.services.curselection()[0])
		self.clearnodes()
		self.loadnodes(service)

	def enableactions(self, actions=[]) :
		for button in self.buttons :
			self.buttons[button]['state'] = DISABLED
		for action in actions :
			if action in self.buttons :
				self.buttons[action]['state'] = NORMAL