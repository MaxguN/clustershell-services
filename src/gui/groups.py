from Tkinter import *

class GroupsFrame :
	def __init__(self, goshujinsama) :
		self.frame = frame = Frame(goshujinsama)
		self.groups = grouplist = Listbox(frame, height=10, width=15)
		self.name = nameinput = Entry(frame)
		self.services = serviceslist = Listbox(frame)
		namelabel = Label(frame, text="Name :")
		serviceslabel = Label(frame, text="Services :")

		groupadd = Button(frame, text="+")
		servicesadd = Button(frame, text="+")
		groupdel = Button(frame, text="-")
		servicesdel = Button(frame, text="-")

		grouplist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2, sticky=W)
		serviceslabel.grid(row=1, column=1, sticky=W)
		serviceslist.grid(row=2, column=1, rowspan=2, columnspan=2, sticky=W)

		groupadd.grid(row=4, column=0, sticky=W)
		groupdel.grid(row=4, column=0, sticky=W, padx=37)
		servicesadd.grid(row=4, column=1, sticky=W)
		servicesdel.grid(row=4, column=1, sticky=W, padx=37)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()