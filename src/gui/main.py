#!/usr/bin/python

from Tkinter import *

class Application:
    def __init__(self) :
        self.buttons = {}
        self.groupelements = {}
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

    def groups(self) :
        for button in self.buttons :
            self.buttons[button]['relief'] = RAISED
        self.buttons['groups']['relief'] = SUNKEN

        self.groupelements['frame'] = frame = Frame(self.window, width=768, height=576, borderwidth=1)
        self.groupelements['groups'] = grouplist = Listbox(frame)
        self.groupelements['name'] = nameinput = Entry(frame)
        self.groupelements['services'] = serviceslist = Listbox(frame)
        namelabel = Label(frame, text="Name :")
        serviceslabel = Label(frame, text="Services :")

        frame.grid(row=1, column=0, columnspan=4)
        grouplist.grid(row=0, column=0, rowspan=3)
        namelabel.grid(row=0, column=1, sticky=W)
        nameinput.grid(row=0, column=2)
        serviceslabel.grid(row=1, column=1, columnspan=2, sticky=W)
        serviceslist.grid(row=2, column=1, rowspan=2, columnspan=2)

    def start(self) :
        self.groups()
        self.window.mainloop()


app = Application()
app.start()