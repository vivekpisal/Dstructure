class MaxHeap:
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
		largest = pos
		if(left < len(self.heap) and self.heap[largest] < self.heap[left]):
			largest = left
		if(right < len(self.heap) and self.heap[largest] < self.heap[right]):
			largest = right

		if(largest!=pos):
			self.heap[largest],self.heap[pos] = self.heap[pos],self.heap[largest]
			self.heapify(largest)



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


