from Tkinter import *

class GroupseditFrame :
	def __init__(self, goshujinsama, application) :
		self.application = application
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
		backbutton = Button(frame, text="Back")
		self.savebutton = savebutton = Button(frame, text="Save")

		grouplist.grid(row=0, column=0, rowspan=4, sticky=N+S)
		namelabel.grid(row=0, column=1, sticky=W)
		nameinput.grid(row=0, column=2, sticky=W)
		serviceslabel.grid(row=1, column=1, sticky=W)
		serviceslist.grid(row=2, column=1, rowspan=2, columnspan=2, sticky=W)
		groupadd.grid(row=4, column=0, sticky=W)
		groupdel.grid(row=4, column=0, sticky=W, padx=37)
		servicesadd.grid(row=4, column=1, sticky=W)
		servicesdel.grid(row=4, column=1, sticky=W, padx=37)
		backbutton.grid(row=5, column=1)
		savebutton.grid(row=5, column=2)

		groupadd['command'] = self.addgroup
		groupdel['command'] = self.delgroup
		servicesadd['command'] = self.addservice
		servicesdel['command'] = self.delservice
		backbutton['command'] = self.back
		savebutton['command'] = self.save

		groupdel['state'] = DISABLED
		servicesdel['state'] = DISABLED
		savebutton['state'] = DISABLED

		self.loadgroups()

		self.groups.bind('<ButtonRelease-1>', self.selectgroup)
		self.name.bind('<KeyRelease>', self.edited)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()

	def loadgroups(self) :
		for group in self.application.config['groups'] :
			self.groups.insert(END, group)

	def clear(self) :
		while self.name.get() :
			self.name.delete(0)
		while self.services.get(0) :
			self.services.delete(0)

	def load(self, group) :
		self.name.insert(0, group)
		for service in self.application.config['groups'][group] :
			self.services.insert(END, service)

	def selectgroup(self, event) :
		group = self.groups.get(self.groups.curselection()[0])
		self.clear()
		self.load(group)

	def addgroup(self) :
		self.edited()

	def delgroup(self) :
		self.edited()

	def addservice(self) :
		self.edited()

	def delservice(self) :
		self.edited()

	def save(self) :
		self.savebutton['state'] = DISABLED

	def back(self) :
		self.clear()
		self.application.switchtogroups()

	def edited(self, event=None) :
		if self.groups.curselection() :
			self.savebutton['state'] = NORMAL
