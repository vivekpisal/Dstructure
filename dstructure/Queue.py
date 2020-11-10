class Queue:
	def __init__(self,size):
		self.queue=[]
		self.size=size

	def enqueue(self,element):
		if len(self.queue)>=size:
			print('Queue is Full')
		else:
			self.queue.append(element)


	def dequeue(self):
		if len(self.queue)==0:
			print("Queue is Empty")
		else:
			self.pop(0)

			
	def printqueue(self):
		print(self.queue)


	def isFull(self):
		if len(self.queue)==size:
			return True
		else:
			return False


	def isEmpty(self):
		if len(self.queue)==0:
			return True
		else:
			return False

