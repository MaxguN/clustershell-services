from Tkinter import *

class ServiceseditFrame :
	def __init__(self, goshujinsama, application) :
		self.frame = frame = Frame(goshujinsama)

		self.services = serviceslist = Listbox(frame, height=10, width=15)
		self.name = nameinput = Entry(frame)
		self.daemon = daemoninput = Entry(frame)
		self.dependencies = dependencieslist = Listbox(frame)
		self.nodes = nodeslist = Listbox(frame)
		self.start = IntVar() 
		self.stop = IntVar()
		self.restart = IntVar()
		self.status = IntVar()

		servicesadd = Button(frame, text="+")
		servicesdel = Button(frame, text="-")
		namelabel = Label(frame, text="Name :")
		daemonlabel = Label(frame, text="Daemon :")
		dependencieslabel = Label(frame, text="Dependencies :")
		dependenciesadd = Button(frame, text="+")
		dependenciesdel = Button(frame, text="-")
		nodeslabel = Label(frame, text="Nodes :")
		nodesadd = Button(frame, text="+")
		nodesdel = Button(frame, text="-")
		actionslabel = Label(frame, text="Actions :")
		startcheck = Checkbutton(frame, text="start", variable=self.start)
		stopcheck = Checkbutton(frame, text="stop", variable=self.stop)
		restartcheck = Checkbutton(frame, text="restart", variable=self.restart)
		statuscheck = Checkbutton(frame, text="status", variable=self.status)
		savebutton = Button(frame, text="Save")
		backbutton = Button(frame, text="Back")

		serviceslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		servicesadd.grid(row=4, column=0, sticky=W)
		servicesdel.grid(row=4, column=0, sticky=E)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2, columnspan=3, sticky=W)
		daemonlabel.grid(row=1, column=1, sticky=W)
		daemoninput.grid(row=1, column=2, columnspan=3, sticky=W)
		dependencieslabel.grid(row=2, column=1, sticky=W)
		dependencieslist.grid(row=3, column=1, columnspan=2, sticky=W+N+S+E)
		dependenciesadd.grid(row=4, column=1)
		dependenciesdel.grid(row=4, column=2)
		nodeslabel.grid(row=2, column=3, sticky=W)
		nodeslist.grid(row=3, column=3, columnspan=2, sticky=W+N+S+E)
		nodesadd.grid(row=4, column=3)
		nodesdel.grid(row=4, column=4)
		actionslabel.grid(row=5, column=1)
		startcheck.grid(row=5, column=2)
		stopcheck.grid(row=6, column=2)
		restartcheck.grid(row=5, column=3)
		statuscheck.grid(row=6, column=3)
		backbutton.grid(row=7, column=3)
		savebutton.grid(row=7, column=4)

		backbutton['command'] = application.switchtoservices

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()