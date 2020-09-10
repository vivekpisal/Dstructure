class Node:
	def __init__(self,value):
		self.data=value
		self.next=None


class SLL:
	def __init__(self):
		self.root=None


	def insert(self,value):
		if self.root==None:
			self.root=Node(value)
		else:
			traversal=self.root
			while traversal.next!=None:
				traversal=traversal.next
			traversal.next=Node(value)


	def getnodes(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			nodes=[]
			while traversal!=None:
				nodes.append(traversal.data)
				traversal=traversal.next
			return nodes


	def print(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal.next!=None:
				print(traversal.data,end="")
				print(" -> ",end="")
				traversal=traversal.next
			print(traversal.data)


	def delete_f(self):
		if self.root==None:
			return False
		else:
			self.root=self.root.next
			return True


	def delete_l(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal.next.next!=None:
				traversal=traversal.next
			traversal.next=None


	def delete(self,value):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal!=None:
				try:
					if traversal.next.data==value:
						f=0
						break
					else:
						traversal=traversal.next
						f=1
				except:
					traversal=traversal.next
			if f==0:
				traversal.next=traversal.next.next