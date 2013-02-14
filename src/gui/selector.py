from Tkinter import *

class SelectorFrame :
	def __init__(self, goshujinsama) :
		self.selector = selector = Toplevel()

		selector.transient(goshujinsama)

		self.selection = selection = Listbox(selector)
		closebutton = Button(selector, text="Close")
		self.select = selectbutton = Button(selector, text="Select")

		selection.grid(row=0, sticky=N+W+S+E)
		closebutton.grid(row=1, sticky=W)
		selectbutton.grid(row=1, sticky=E)

		closebutton['command'] = selector.destroy

	def load(self, selection, callback) :
		for element in selection :
			self.selection.insert(END, element)
		self.select['command'] = lambda : self.selectaction(callback)

	def selectaction(self, callback) :
		callback(self.selection.get(self.selection.curselection()[0]))
		self.selector.destroy()
