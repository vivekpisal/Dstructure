class Node:
	def __init__(self,value):
		self.data=value
		self.next=None


class SCLL:
	def __init__(self):
		self.root=None


	def insert(self,value):
		node=Node(value)
		if self.root==None:
			self.root=node
			node.next=self.root
		else:
			traversal=self.root
			while traversal.next!=self.root:
				traversal=traversal.next
			traversal.next=node
			node.next=self.root


	def getnodes(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			nodes=[]
			while traversal.next!=self.root:
				nodes.append(traversal.data)
				traversal=traversal.next
			return nodes


	def print(self):
		if self.root==None:
			return False
		else:
			traversal=self.root
			try:
				while traversal.next!=self.root:
					print(traversal.data,end="")
					print(" -> ",end="")
					traversal=traversal.next
				print(traversal.data)
				print("\n")
			except:
				pass
			

	
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
			traversal.next=None


	def delete(self,value):
		if self.root==None:
			return False
		else:
			traversal=self.root
			while traversal.next!=self.root:
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