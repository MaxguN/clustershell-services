#!/usr/bin/python

from Tkinter import *
from groups import *
from managers import *
from nodes import *
from services import *
from servicesedit import *

import sys
sys.path.append('../service')

import config

class Application :
    def __init__(self) :
        self.current = ''
        config.load()
        self.config = config.config
        self.buttons = {}
        self.frames = {}
        self.main()

    def main(self) :
        self.window = Tk()

        self.buttons['services'] = services = Button(self.window, text="Services")
        self.buttons['nodes'] = nodes = Button(self.window, text="Nodes")
        self.buttons['groups'] = groups = Button(self.window, text="Groups")
        self.buttons['managers'] = managers = Button(self.window, text="Managers")
        self.buttons['servicesedit'] = services
        
        services.grid(row=0, column=0)
        nodes.grid(row=0, column=1)
        groups.grid(row=0, column=2)
        managers.grid(row=0, column=3)

        nodes['command'] = self.switchtonodes
        groups['command'] = self.switchtogroups
        managers['command'] = self.switchtomanagers
        services['command'] = self.switchtoservices

        self.frames['services'] = ServicesFrame(self.window, self)
        self.frames['servicesedit'] = ServiceseditFrame(self.window, self)
        self.frames['nodes'] = NodesFrame(self.window, self)
        self.frames['groups'] = GroupsFrame(self.window, self)
        self.frames['managers'] = ManagersFrame(self.window, self)

    def switchtonodes(self) :
        if self.current :
            self.frames[self.current].detach()
            self.buttons[self.current]['relief'] = RAISED
        self.current = 'nodes'
        self.buttons[self.current]['relief'] = SUNKEN
        self.frames[self.current].attach()

    def switchtogroups(self) :
        if self.current :
            self.frames[self.current].detach()
            self.buttons[self.current]['relief'] = RAISED
        self.current = 'groups'
        self.buttons[self.current]['relief'] = SUNKEN
        self.frames[self.current].attach()  

    def switchtomanagers(self) :
        if self.current :
            self.frames[self.current].detach()
            self.buttons[self.current]['relief'] = RAISED
        self.current = 'managers'
        self.buttons[self.current]['relief'] = SUNKEN
        self.frames[self.current].attach()

    def switchtoservices(self) :
        if self.current :
            self.frames[self.current].detach()
            self.buttons[self.current]['relief'] = RAISED
        self.current = 'services'
        self.buttons[self.current]['relief'] = SUNKEN
        self.frames[self.current].attach()

    def switchtoservicesedit(self) :
        if self.current :
            self.frames[self.current].detach()
            self.buttons[self.current]['relief'] = RAISED
        self.current = 'servicesedit'
        self.buttons[self.current]['relief'] = SUNKEN
        self.frames[self.current].attach()

    def start(self) :
        self.switchtoservices()
        self.window.mainloop()


app = Application()
app.start()