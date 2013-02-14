from Tkinter import *

class NodesFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.managers = managers = self.application.config["managers"].keys()
		self.manager = manager = StringVar()
		manager.set(managers[0])

		self.frame = frame = Frame(goshujinsama)
		self.nodes = nodeslist = Listbox(frame, exportselection=0, height=10, width=15)
		self.name = nameinput = Entry(frame)
		managerslist = managerslist = OptionMenu(frame, manager, *managers)
		namelabel = Label(frame, text="Name :")
		managerslabel = Label(frame, text="Managers :") 
		nodeadd = Button(frame, text="+")
		self.nodedel = nodedel = Button(frame, text="-")
		self.savebutton = savebutton = Button(frame, text="Save")

		nodeslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2)
		managerslabel.grid(row=1, column=1, sticky=W)
		managerslist.grid(row=1, column=1, columnspan=3, sticky=E)
		nodeadd.grid(row=4, column=0, sticky=W)
		nodedel.grid(row=4, column=0, sticky=W, padx=37)
		savebutton.grid(row=4, column=2, sticky=E)

		nodeadd['command'] = self.addnode
		nodedel['command'] = self.delnode
		savebutton['command'] = self.save

		self.loadnodes()

		nodedel['state'] = DISABLED
		savebutton['state'] = DISABLED

		self.nodes.bind('<ButtonRelease-1>', self.selectnode)
		self.name.bind('<KeyRelease>', self.edited)
		managerslist["menu"].bind('<Unmap>', self.edited)


	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()

	def clearnodes(self) :
		self.nodes.delete(0, END)

	def loadnodes(self) :
		for node in self.application.config['nodes'] :
			self.nodes.insert(END, node)

	def reloadnodes(self) :			
		self.clearnodes()
		self.loadnodes()

	def reloadmanagers(self) :
		self.managers = []
		self.managers = self.application.config["managers"].keys()

	def clear(self) :
		self.name.delete(0, END)
		self.manager.set(self.managers[0])

	def load(self, node) :
		self.name.insert(0, node)
		self.manager.set(self.managers[self.managers.index(self.application.config["nodes"][node]["manager"])])

	def selectnode(self, event) :
		node = self.nodes.get(self.nodes.curselection()[0])
		self.clear()
		self.load(node)
		self.nodedel['state'] = NORMAL

	def addnode(self) :
		self.nodes.selection_clear(0, END)
		self.clear()
		self.nodes.insert(END, "<new_node>")
		self.nodes.selection_set(END)
		self.name.insert(0, "<new_node>")
		self.nodedel['state'] = NORMAL
	
	def delnode(self) :
		node = self.nodes.get(self.nodes.curselection()[0])
		config = self.application.config
		if node in config['nodes'] :
			del config['nodes'][node]
		self.nodes.delete(self.nodes.curselection()[0])
		self.clear()
		self.application.save()
		self.application.reloadnodes()

	def save(self) :
		node = self.nodes.get(self.nodes.curselection()[0])
		config = self.application.config
		if node in config['nodes'] :
			del config['nodes'][node]
		node = self.name.get()
		config['nodes'][node] = {'manager' : self.manager.get()}
		self.application.save()
		self.savebutton['state'] = DISABLED
		self.application.reloadnodes()

	def edited(self, event=None) :
		if self.nodes.curselection() :
			self.savebutton['state'] = NORMAL