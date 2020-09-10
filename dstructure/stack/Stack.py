class Stack:
	def __init__(self,size):
		self.stack=[]
		self.size=size
		self.max=None
		self.min=None

	def push(self,value):
		flag=self.isFull()
		if flag==False:
			self.stack.append(value)
		else:
			print("")



	def isFull(self):
		if len(self.stack)==self.size:
			return True
		elif len(self.stack)<self.size:
			return False

