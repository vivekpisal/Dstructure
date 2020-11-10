class DNode:
	def __init__(self,value):
		self.data=value
		self.prev=None
		self.next=None


class DCLL:
	def __init__(self):
		self.root=None


	def insert(self,value):
		node=DNode(value)
		if self.root==None:
			self.root=node
			node.prev=self.root
			node.next=self.root
		else:
			traversal=self.root
			while traversal.next!=self.root:
				traversal=traversal.next
			traversal.next=node
			node.prev=traversal
			node.next=self.root


	def getnodes(self):
		if self.root==None:
			return False
		else:
			nodes=[]
			traversal=self.root
			while traversal.next!=self.root:
				nodes.append(traversal.data)
				traversal=traversal.next
			return nodes


	def print(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal.next!=self.root:
				print(traversal.data,end="")
				print(" <-> ",end="")
				traversal=traversal.next
			print(traversal.data)


	def delete_f(self):
		if self.root==None:
			return False
		else:
			old=self.root
			node=self.root.next
			self.root=node
			node.prev=self.root
			traversal=self.root
			while traversal.next!=old:
				traversal=traversal.next
			traversal.next=self.root
			return True


	def delete_l(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal.next.next!=self.root:
				traversal=traversal.next
			traversal.next=self.root
			return True


	def delete(self,value):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal.next!=None:
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
				node=traversal.next.next
				traversal.next=node