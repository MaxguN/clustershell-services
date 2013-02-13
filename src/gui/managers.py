from Tkinter import *

class ManagersFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)
		
		self.managers = managerslist = Listbox(frame, height=10, width=15)
		self.name = nameinput = Entry(frame)
		self.command = commandsinput = Entry(frame)

		namelabel = Label(frame, text="Name :")
		commandslabel = Label(frame, text="Command :")
		manageradd = Button(frame, text="+")
		managerdel = Button(frame, text="-")

		managerslist.grid(row=0, column=0, rowspan=4, sticky=N+W)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2)
		commandslabel.grid(row=1, column=1, sticky=W)
		commandsinput.grid(row=1, column=2, sticky=W)
		manageradd.grid(row=4, column=0, sticky=W)
		managerdel.grid(row=4, column=0, sticky=W, padx=37)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()