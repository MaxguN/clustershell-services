from Tkinter import *

class ManagersFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
		self.frame = frame = Frame(goshujinsama)
		
		self.managers = managerslist = Listbox(frame, exportselection=0, height=10, width=15)
		self.name = nameinput = Entry(frame)
		self.command = commandsinput = Entry(frame)

		namelabel = Label(frame, text="Name :")
		commandslabel = Label(frame, text="Command :")
		manageradd = Button(frame, text="+")
		self.managerdel = managerdel = Button(frame, text="-")
		self.savebutton = savebutton = Button(frame, text="Save")


		managerslist.grid(row=0, column=0, rowspan=4, sticky=N+W)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2)
		commandslabel.grid(row=1, column=1, sticky=W)
		commandsinput.grid(row=1, column=2, sticky=W)
		manageradd.grid(row=4, column=0, sticky=W)
		managerdel.grid(row=4, column=0, sticky=W, padx=37)
		savebutton.grid(row=4, column=2, sticky=E)

		manageradd['command'] = self.addmanager
		managerdel['command'] = self.delmanager
		savebutton['command'] = self.save

		self.loadmanagers()

		managerdel['state'] = DISABLED
		savebutton['state'] = DISABLED

		self.managers.bind('<ButtonRelease-1>', self.selectmanager)
		self.name.bind('<KeyRelease>', self.edited)
		self.command.bind('<KeyRelease>', self.edited)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()

	def clearmanagers(self) :
		self.managers.delete(0, END)

	def loadmanagers(self) :
		for manager in self.application.config['managers'] :
			self.managers.insert(END, manager)

	def reloadmanagers(self) :
		self.clearmanagers()
		self.loadmanagers()

	def clear(self) :
		self.name.delete(0, END)
		self.command.delete(0,END)

	def load(self, manager) :
		self.name.insert(0, manager)
		self.command.insert(0, self.application.config["managers"][manager])

	def selectmanager(self, event) :
		manager = self.managers.get(self.managers.curselection()[0])
		self.clear()
		self.load(manager)
		self.managerdel['state'] = NORMAL

	def addmanager(self) :
		self.managers.selection_clear(0, END)
		self.clear()
		self.managers.insert(END, "<new_manager>")
		self.managers.selection_set(END)
		self.name.insert(0, "<new_manager>")
		self.managerdel['state'] = NORMAL
	
	def delmanager(self) :
		manager = self.managers.get(self.managers.curselection()[0])
		config = self.application.config
		if manager in config['managers'] :
			del config['managers'][manager]
		self.managers.delete(self.managers.curselection()[0])
		self.clear()
		self.application.save()
		self.application.reloadmanagers()

	def save(self) :
		manager = self.managers.get(self.managers.curselection()[0])
		config = self.application.config
		if manager in config['managers'] :
			del config['managers'][manager]
		manager = self.name.get()
		config['managers'][manager] = self.command.get()
		self.application.save()
		self.savebutton['state'] = DISABLED
		self.application.reloadmanagers()

	def edited(self, event=None) :
		if self.managers.curselection() :
			self.savebutton['state'] = NORMAL