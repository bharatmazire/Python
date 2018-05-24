class Observable(object):
	def __init__(self,val):
		self.val = val
		self.observer = []

	def set(self,val):
		old = self.val
		self.val = val
		self.notifyAllObserver(old , self.val)

	def get(self):
		return self.val

	def addObserver(self,o):
		self.observer.append(o)

	def removeObserver(self,o):
		if o in self.observer:
			self.observer.remove(o)

	def notifyAllObserver(self,old,new):
		for o in self.observer:
			o.valueChange(old,new)

class Observer(object):
	def __init__(self,foo):
		self.foo = foo
		self.foo.addObserver(self)

	def __del__(self):
		self.foo.removeObserver(self)

	def valueChange(self,old,new):
		print ("value change form  {} to {}".format(old,new))

foo = Observable(1)
bar = Observer(foo)
foo.set(2)
foo.set(3)
foo.removeObserver(bar)
foo.set(4)
foo.addObserver(bar)
foo.set(5)
