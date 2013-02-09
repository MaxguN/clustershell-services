from Tkinter import *

class ManagersFrame :
	def __init__(self, goshujinsama) :
		self.frame = frame = Frame(goshujinsama)
		
		self.managers = managerslist = Listbox(frame)
		self.name = nameinput = Entry(frame)

		namelabel = Label(frame, text="Name :")
		managerslabel = Label(frame, text="Command :") 
		manageradd = Button(frame, text="+")
		managerdel = Button(frame, text="-")

		managerslist.grid(row=0, rowspan=4)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2)
		managerslabel.grid(row=1, column=1, sticky=W)
		manageradd.grid(row=2, column=0, sticky=W)
		managerdel.grid(row=2, column=0)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()