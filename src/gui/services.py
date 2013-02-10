from Tkinter import *

class ServicesFrame :
	def __init__(self, goshujinsama, application) :
		self.frame = frame = Frame(goshujinsama)

		self.services = serviceslist = Listbox(frame, height=10, width=15)
		self.nodes = nodeslist = Listbox(frame)

		nodelabel = Label(frame, text="Nodes :")
		editbutton = Button(frame, text="Edit")
		startbutton = Button(frame, text="Start")
		stopbutton = Button(frame, text="Stop")
		restartbutton = Button(frame, text="Restart")
		statusbutton = Button(frame, text="Statut")

		serviceslist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		nodelabel.grid(row=0, column=1, sticky=W)
		nodeslist.grid(row=1, column=1, columnspan=4,sticky=W+N+S+E)
		editbutton.grid(row=4, column=0, sticky=W+E)
		startbutton.grid(row=4, column=1, sticky=W)
		stopbutton.grid(row=4, column=2, sticky=W)
		restartbutton.grid(row=4, column=3, sticky=W)
		statusbutton.grid(row=4, column=4, sticky=W)

		editbutton['command'] = application.switchtoservicesedit

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()