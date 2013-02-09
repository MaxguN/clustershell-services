#!/usr/bin/python

from Tkinter import *

class Application:
    def __init__(self) :
        self.current = ""
        self.buttons = {}
        self.frames = {}
        self.main()

    def main(self) :
        self.window = Tk()

        self.buttons['services'] = services = Button(self.window, text="Services")
        self.buttons['nodes'] = nodes = Button(self.window, text="Nodes")
        self.buttons['groups'] = groups = Button(self.window, text="Groups")
        self.buttons['managers'] = managers = Button(self.window, text="Managers")

        services.grid(row=0, column=0)
        nodes.grid(row=0, column=1)
        groups.grid(row=0, column=2)
        managers.grid(row=0, column=3)

        nodes['command'] = self.switchtonodes
        groups['command'] = self.switchtogroups

    def switchtonodes(self) :
        self.frames[self.current]['frame'].grid_forget()
        self.nodes()

    def switchtogroups(self) :
        self.frames[self.current]['frame'].grid_forget()
        self.groups()

    def groups(self) :
        for button in self.buttons :
            self.buttons[button]['relief'] = RAISED
        self.buttons['groups']['relief'] = SUNKEN
        self.current = "groups"

        self.frames['groups'] = {}

        self.frames['groups']['frame'] = frame = Frame(self.window, width=768, height=576, borderwidth=1)
        self.frames['groups']['groups'] = grouplist = Listbox(frame)
        self.frames['groups']['name'] = nameinput = Entry(frame)
        self.frames['groups']['services'] = serviceslist = Listbox(frame)
        namelabel = Label(frame, text="Name :")
        serviceslabel = Label(frame, text="Services :")
        groupslabel = Label(frame, text="Groups :")
  

        groupadd = Button(self.window, text="+")
        servicesadd = Button(self.window, text="+")
        groupdel = Button(self.window, text="-")
        servicesdel = Button(self.window, text="-")

        frame.grid(row=1, column=0, columnspan=4)
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

    def nodes(self) :
        for button in self.buttons :
            self.buttons[button]['relief'] = RAISED
        self.buttons['nodes']['relief'] = SUNKEN
        self.current = "nodes"

        self.frames['nodes'] = {}

        managers = ["service", "sysvinit", "bsdinit", "upstart", "systemd"]
        self.frames['nodes']['manager'] = manager = StringVar()
        manager.set(managers[0])

        self.frames['nodes']['frame'] = frame = Frame(self.window, width=768, height=576, borderwidth=1)
        self.frames['nodes']['nodes'] = nodeslist = Listbox(frame)
        self.frames['nodes']['name'] = nameinput = Entry(frame)
        managerslist = OptionMenu(frame, manager, *managers)
        namelabel = Label(frame, text="Name :")
        managerslabel = Label(frame, text="Managers :") 
        nodeadd = Button(self.window, text="+")
        nodedel = Button(self.window, text="-")

        frame.grid(row=1, column=0, columnspan=4)
        nodeslist.grid(row=0, rowspan=4)
        namelabel.grid(row=0, column=1, sticky=W)
        nameinput.grid(row=0, column=2)
        managerslabel.grid(row=1, column=1, sticky=W)
        managerslist.grid(row=1, column=2, sticky=W)
        nodeadd.grid(row=2, column=0, sticky=W)
        nodedel.grid(row=2, column=0)
        

    def start(self) :
        self.nodes()
        self.window.mainloop()


app = Application()
app.start()