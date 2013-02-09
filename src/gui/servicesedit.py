from Tkinter import *

class ServiceseditFrame :
	def __init__(self, goshujinsama) :
		self.frame = frame = Frame(goshujinsama)

	def attach(self) :
		self.frame.grid(row=1, column=0, columnspan=4)

	def detach(self) :
		self.frame.grid_forget()