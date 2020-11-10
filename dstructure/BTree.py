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


	def get_bfs(self):
		queue=[]
		queue.append(self)
		while(len(queue)>0):
			node=queue.pop(0)
			size=len(queue)
			print(node.data)
			for i in range(size):
				if(node.right!=None):
					queue.append(node.right)
				if(node.left!=None):
					queue.append(node.left)


def maxDepth(node): 
    if node is None: 
        return 0  
    else: 
        lDepth=maxDepth(node.left)
        rDepth=maxDepth(node.right) 
        if lDepth>rDepth: 
            return lDepth+1
        else: 
            return rDepth+1


