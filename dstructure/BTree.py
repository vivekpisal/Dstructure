class BTree:
	nodes=[]
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
		if self.right:
			self.right.getnodes()
		BTree.nodes.append(self.data)
		if self.left:
			self.left.getnodes()
		return BTree.nodes


	def inorder(self,root)->list:
		"""
		Return the inorder traversals of the tree.
		"""
		res=[]
		if root:
			res=self.inorder(root.left)
			res.append(root.data)
			res=res+self.inorder(root.right)
		return res


	def preorder(self,root)->list:
		"""
		Return the preorder traversals of the tree.
		"""
		res=[]
		if root:
			res.append(root.data)
			res=res+self.preorder(root.left)
			res=res+self.preorder(root.right)
		return res


	def postorder(self,root)->list:
		"""
		Return the postorder traversals of the tree.
		"""
		res=[]
		if root:
			res=self.postorder(root.left)
			res=res+self.postorder(root.right)
			res.append(root.data)
		return res


	def get_bfs(self)->list:
		"""
		Return the bfs of the tree.
		"""
		queue=[]
		bfs=[]
		queue.append(self)
		while(len(queue)>0):
			node=queue.pop(0)
			bfs.append(node.data)
			if(node.right!=None):
				queue.append(node.right)
			if(node.left!=None):
				queue.append(node.left)
		return bfs


	def get_dfs(self)->list:
		"""
		Return the dfs of the tree.
		"""
		stack=[]
		dfs=[]
		stack.append(self)
		while(len(stack)>0):
			node=stack.pop(len(stack)-1)
			dfs.append(node.data)
			if(node.right!=None):
				stack.append(node.right)
			if(node.left!=None):
				stack.append(node.left)
		return dfs


	def left_view(self)->list:
		"""
		Return the left view of the tree.
		"""
		queue=[]
		left=[]
		queue.append(self)
		while(len(queue)>0):
			for i in range(len(queue)):
				if(i==0):
					left.append(queue[0].data)
				node=queue[0]
				queue.pop(0)
				if(node.left!=None):
					queue.append(node.left)
				if(node.right!=None):
					queue.append(node.right)
		return left


	def right_view(self)->list:
		"""
		Return the right view of the tree.
		"""
		queue=[]
		right=[]
		queue.append(self)
		while(len(queue)>0):
			size=len(queue)
			for i in range(len(queue)):
				if i==size-1:
					right.append(queue[0].data)
				node=queue[0]
				queue.pop(0)
				if(node.left!=None):
					queue.append(node.left)
				if(node.right!=None):
					queue.append(node.right)
		return right


	def total_nodes(self)->int:
		"""
		Return the total nodes of the tree.
		"""
		queue=[]
		sum=0
		queue.append(self)
		while(len(queue)>0):
			node=queue.pop(0)
			sum+=1
			if(node.right!=None):
				queue.append(node.right)
			if(node.left!=None):
				queue.append(node.left)
		return sum


def maxDepth(node):
	"""
	Return the maxdepth of the tree.
	"""
	if node is None: 
		return 0  
	else: 
		lDepth=maxDepth(node.left)
		rDepth=maxDepth(node.right) 
		if lDepth>rDepth: 
		    return lDepth+1
		else: 
		    return rDepth+1


a=BTree(23)
a.insert(24)
a.insert(13)
a.insert(14)
a.insert(10)
a.insert(26)
a.insert(9)
print(a.total_nodes())