from Tkinter import *

class GroupsFrame :
	def __init__(self, goshujinsama) :
		self.frame = frame = Frame(goshujinsama)
		self.groups = grouplist = Listbox(frame)
		self.name = nameinput = Entry(frame)
		self.services = serviceslist = Listbox(frame)
		namelabel = Label(frame, text="Name :")
		serviceslabel = Label(frame, text="Services :")
		groupslabel = Label(frame, text="Groups :")


		groupadd = Button(frame, text="+")
		servicesadd = Button(frame, text="+")
		groupdel = Button(frame, text="-")
		servicesdel = Button(frame, text="-")

		grouplist.grid(row=0, rowspan=4)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2)
		serviceslabel.grid(row=1, column=1, columnspan=2, sticky=W)
		serviceslist.grid(row=2, column=1, rowspan=2, columnspan=2)
		groupslabel.grid(row=0, column=0, sticky=W)

		groupadd.grid(row=2, column=0, sticky=W)
		groupdel.grid(row=2, column=0)
		servicesadd.grid(row=2, column=2, sticky=W)
		servicesdel.grid(row=2, column=2)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()