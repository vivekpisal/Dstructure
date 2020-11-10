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
			print("Stack is full")



	def isFull(self):
		if len(self.stack)==self.size:
			return True
		elif len(self.stack)<self.size:
			return False



	def pop_element(self):
		if len(self.stack)!=0:
			self.stack.pop()
		else:
			print("Stack is empty")



	def get_min(self):
		return min(self.stack)


	def get_max(self):
		return max(self.stack)

