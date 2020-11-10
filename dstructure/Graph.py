class Graph:
	def __init__(self):
		self.edges={}

	def insert(self,x,y):
		try:
			if self.edges[x] or self.edges[y]:
				self.edges[x].add(y)
				self.edges[y].add(x)
		except:
			try:
				if self.edges[x]:
					self.edges[x].add(y)
			except:
				self.edges[x]=set([y])

			try:
				if self.edges[y]:
					self.edges[y].add(x)
			except:
				self.edges[y]=set([x])


	def show(self):
		for i in self.edges:
			print(i,"-> ",end="")
			for j in self.edges[i]:
				print(j,end=" ")
			print()


	def get_elements(self):
		return self.edges


	def get_vertices(self):
		nodes=[]
		for i in self.edges:
			nodes.append(i)
		return nodes


	def get_bfs(self,node):
		queue=[node]
		visited={x:False for x in self.edges}
		visited[node]=True
		bfs=[]
		while(len(queue)>0):
			node=queue.pop(0)
			bfs.append(node)
			for i in self.edges[node]:
				if(visited[i]==False):
					queue.append(i)
					visited[i]=True
		return bfs


