class MinHeap:
	def __init__(self,heap):
		self.heap = heap


	def __str__(self):
		return f"{self.heap}"


	def heapify(self,pos):
		"""
		This method convert list into heap.
		"""
		left = (2*pos)
		right = (2*pos) + 1
		smallest = pos
		if(left < len(self.heap) and self.heap[smallest] > self.heap[left]):
			smallest = left
		if(right < len(self.heap) and self.heap[smallest] > self.heap[right]):
			smallest = right

		if(smallest!=pos):
			self.heap[smallest],self.heap[pos] = self.heap[pos],self.heap[smallest]
			self.heapify(smallest)



	def make_heap(self):
		"""
		obj.make_heap()
		Make heap is use for making the heap
		"""
		i = len(self.heap)//2
		while i>=0:
			self.heapify(i)
			i-=1



	def pop(self):
		"""
		obj.pop()
		This method delete the first element in the heap.
		"""
		del self.heap[0]
		self.make_heap()



	def push(self,ele):
		"""
		obj.push(element)
		This function is use for inserting the element in heap.
		"""
		self.heap.append(ele)
		self.make_heap()


	def top(self)->int:
		"""
		obj.top()
		Return the minimum element in the heap.
		"""
		return self.heap[0]


