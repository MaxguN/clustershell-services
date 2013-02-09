from Tkinter import *

class NodesFrame :
	def __init__(self, goshujinsama) :
		managers = ["service", "sysvinit", "bsdinit", "upstart", "systemd"]
		self.manager = manager = StringVar()
		manager.set(managers[0])

		self.frame = frame = Frame(goshujinsama)
		self.nodes = nodeslist = Listbox(frame, height=10, width=15)
		self.name = nameinput = Entry(frame)
		managerslist = OptionMenu(frame, manager, *managers)
		namelabel = Label(frame, text="Name :")
		managerslabel = Label(frame, text="Managers :") 
		nodeadd = Button(frame, text="+")
		nodedel = Button(frame, text="-")

		nodeslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2)
		managerslabel.grid(row=1, column=1, sticky=W)
		managerslist.grid(row=1, column=1, columnspan=3, sticky=E)
		nodeadd.grid(row=4, column=0, sticky=W)
		nodedel.grid(row=4, column=0, sticky=W, padx=37)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()