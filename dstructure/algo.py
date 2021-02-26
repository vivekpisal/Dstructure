def merge2list(first,second)->list:
	"""
	Return the Merge Two Sorted List.
	"""
	i=0
	j=0
	ans=[]
	while(i<len(first) and j<len(second)):
		if first[i]>second[j]:
			ans.append(second[j])
			j+=1
		else:
			ans.append(first[i])
			i+=1
	if(i>=len(first)):
		while j<len(second):
			ans.append(second[j])
			j+=1
	else:
		while i<len(first):
			ans.append(first[i])
			i+=1
	return ans



def binarysearch(arr,ser)->int:
	"""
	Binary Search In Sorted Array
	"""
	first=0
	second=len(arr)-1
	mid=(first+second)//2
	while first<=second:
		if arr[mid]==ser:
			return mid+1
		elif arr[mid]>ser:
			second=mid-1
		elif arr[mid]<ser:
			first=mid+1
		mid=(first+second)//2
	return -1



def rotateright(arr,k)->list:
	"""
	Rotate the array right side k number of times.
	"""
	temp=a[0]
	poi=0
	for i in range(len(arr)):
		for j in range(0,k):
			poi+=1
			if(poi==len(arr)):
				poi=0
		temp1=arr[poi]
		arr[poi]=temp
		temp=temp1
	return arr



def rotateleft(arr,k)->list:
	"""
	Rotate the array left side k number of times.
	"""
	temp=a[len(arr)-1]
	poi=len(arr)-1
	for i in range(len(arr)-1,-1,-1):
		for i in range(0,k):
			poi-=1
			if(poi==-1):
				poi=len(arr)-1
		temp1=arr[poi]
		arr[poi]=temp
		temp=temp1
	return arr



def ispalindrome(no)->bool:
	"""
	If number is palindrome function return true else false.
	"""
	if type(no)==list:
		if no==no[::-1]:
			return True
		else:
			return False
	else:
		no=str(no)
		rev=no[::-1]
		if no==rev:
			return True
		else:
			return False



def all_palindrome(string)->list:
	"""
	Return the all non empty palindrome string of given string.
	"""
	if type(string)==str:
		pali=[]
		for i in range(len(string)):
			for j in range(i,len(string)):
				if(string[i:j+1]=="".join(reversed(string[i:j+1]))):
					pali.append(string[i:j+1])
		return pali
	else:
		return None



def all_prime(no)->list:
	"""
	Return the list of all prime numbers till the number given by user.
	This function uses the concept the sieve.
	"""
	prime=[0 for i in range(no+1)]
	no_prime=[]
	for i in range(2,no+1):
		if prime[i]==0:
			for j in range(i*i,no+1,i):
				prime[j]=1
	for i in range(2,no+1):
		if prime[i]==0:
			no_prime.append(i)
	return no_prime



def prime_factors(no)->list:
	"""
	Return the list of prime factors of the number.
	"""
	prime=[i for i in range(no+1)]
	factors=[]
	for i in range(2,no+1):
		if prime[i]==i:
			for j in range(i*i,no+1,i):
				prime[j]=i
	while(no>=2):
		factors.append(prime[no])
		no=no//prime[no]
	return factors



def repeated_elements(arr)->dict:
	"""
	Return the dictionary of the elements with it's count.
	"""
	dic={}
	for i in arr:
		try:
			if dic[i]:
				dic[i]+=1
		except:
			dic[i]=1 
	return dic 



def common_elements(arr,arr1)->list:
	"""
	Return the list of common elements between two arrays.
	"""
	dic={}
	for i in arr:
		try:
			if dic[i]:
				dic[i]+=1
		except:
			dic[i]=1
	common=[]
	for i in arr1:
		try:
			if dic[i]:
				common.append(i)
		except:
			pass
	return common

