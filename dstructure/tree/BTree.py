class BTree:
	def __init__(self,value):
		self.data=value
		self.left=None
		self.right=None


	def insert(self,value):
		if self.data:
			if self.data>value:
				if self.left==None:
					self.left=BTree(value)
				else:
					self.left.insert(value)
			elif self.data<value:
				if self.right==None:
					self.right=BTree(value)
				else:
					self.right.insert(value)
		else:
			self.data=data 


	def getnodes(self):
		nodes=[]
		if self.right:
			self.right.getnodes()
		nodes.append(self.data)
		if self.left:
			self.left.getnodes()
		return nodes


	def inorder(self,root):
		res=[]
		if root:
			res=self.inorder(root.left)
			res.append(root.data)
			res=res+self.inorder(root.right)
		return res


	def preorder(self,root):
		res=[]
		if root:
			res.append(root.data)
			res=res+self.preorder(root.left)
			res=res+self.preorder(root.right)
		return res


	def postorder(self,root):
		res=[]
		if root:
			res=self.postorder(root.left)
			res=res+self.postorder(root.right)
			res.append(root.data)
		return res