from Tkinter import *

class SelectorFrame :
	def __init__(self, goshujinsama, selectmode=BROWSE) :
		self.selector = selector = Toplevel()

		selector.transient(goshujinsama)

		self.selection = selection = Listbox(selector, selectmode=selectmode)
		closebutton = Button(selector, text="Close")
		self.select = selectbutton = Button(selector, text="Select")

		selection.grid(row=0, sticky=N+W+S+E)
		closebutton.grid(row=1, sticky=W)
		selectbutton.grid(row=1, sticky=E)

		closebutton['command'] = selector.destroy

		selectbutton['state'] = DISABLED

		selection.bind('<ButtonRelease-1>', self.selectelement)

	def load(self, selection, callback) :
		for element in selection :
			self.selection.insert(END, element)
		self.select['command'] = lambda : self.selectaction(callback)

	def selectaction(self, callback) :
		selected = ''
		if self.selection['selectmode'] in (MULTIPLE, EXTENDED) :
			selected = []
			selection = self.selection.curselection()
			for item in selection :
				selected.append(self.selection.get(item))
		else :
			selected = self.selection.get(self.selection.curselection()[0])
		callback(selected)
		self.selector.destroy()

	def selectelement(self, event) :
		self.select['state'] = NORMAL
