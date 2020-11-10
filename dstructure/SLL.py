class Node:
	def __init__(self,value):
		self.data=value
		self.next=None


class SLL:
	def __init__(self):
		self.head=None


	def insert(self,value):
		if self.head==None:
			self.head=Node(value)
		else:
			traversal=self.head
			while traversal.next!=None:
				traversal=traversal.next
			traversal.next=Node(value)


	def getnodes(self):
		if self.head==None:
			return False
		else:
			traversal=self.head
			nodes=[]
			while traversal!=None:
				nodes.append(traversal.data)
				traversal=traversal.next
			return nodes


	def print(self):
		if self.head==None:
			return False
		else:
			traversal=self.head
			while traversal.next!=None:
				print(traversal.data,end="")
				print(" -> ",end="")
				traversal=traversal.next
			print(traversal.data)


	def delete_f(self):
		if self.head==None:
			return False
		else:
			self.head=self.head.next
			return True


	def delete_l(self):
		if self.head==None:
			return False
		else:
			traversal=self.head
			while traversal.next.next!=None:
				traversal=traversal.next
			traversal.next=None


	def delete(self,value):
		if self.head==None:
			return False
		else:
			traversal=self.head
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


	def reverse(self):
		current=self.head
		prev=None
		while current!=None:
			nextnode=current.next
			current.next=prev
			prev=current
			current=nextnode
		self.head=prev


