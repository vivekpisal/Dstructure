class HashMap:
	def __init__(self,size):
		self.map=[None]*size
		self.size=size


	def set_hash(self,value):
		if type(value)==str:
			loc=len(value)
			if self.map[loc]==None:
				self.map[loc]=list([value])
			else:
				self.map[loc].append(value)
		elif type(value)==int or type(value)==float:
			loc=value%self.size
			if self.map[loc]==None:
				self.map[loc]=list([value])
			else:
				self.map[loc].append(value)


	def search(self,value):
		if type(value)==str:
			loc=len(value)
			if type(self.map[loc])==list:
				for i in self.map[loc]:
					if i==value:
						return True
				else:
					return False
			else:
				if self.map[loc]==value:
					return True
				else:
					return False
		elif type(value)==int or type(value)==float:
			loc=value%self.size
			if type(self.map[loc])==list:
				for i in self.map[loc]:
					if i==value:
						return True
				else:
					return False
			else:
				if self.map[loc]==value:
					return True
				else:
					return False


	def ascii_hash(self,value):
		if type(value)==str:
			loc=0
			for i in value:
				loc+=ord(i)
			loc=loc%self.size
			if self.map[loc]==None:
				self.map[loc]=list([value])
			else:
				self.map[loc].append(value)
		elif type(value)==int or type(value)==float:
			loc=0
			for i in str(value):
				loc+=ord(i)
			loc=loc%self.size
			if self.map[loc]==None:
				self.map[loc]=list([value])
			else:
				self.map[loc].append(value)


	def ascii_search(self,value):
		if type(value)==str:
			loc=0
			for i in value:
				loc+=ord(i)
			loc=loc%self.size
			if type(self.map[loc])==list:
				for i in self.map[loc]:
					if i==value:
						return True
				else:
					return False
			else:
				if self.map[loc]==value:
					return True
				else:
					return False
		elif type(value)==int or type(value)==float:
			loc=0
			for i in str(value):
				loc+=ord(i)
			loc=loc%self.size
			if type(self.map[loc])==list:
				for i in self.map[loc]:
					if i==value:
						return True
				else:
					return False
			else:
				if self.map[loc]==value:
					return True
				else:
					return False

	def print(self):
		print(self.map)




