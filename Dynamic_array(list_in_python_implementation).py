import ctype


class apna_list:

	def __init__(self):
		self.size=1
		self.n=0
		self.A=self.__makearr(self.size)
		self.count=0

	def __len__(self):
		return self.n

	def find(self,item):
		for i in range(self.n):
			if(self.A[i]==item):
				return i
		return "Error -element not found"

	def sort(self):
		for i in range(self.n):
			for j in range(i+1,self.n):
				if(self.A[i]>self.A[j]):
					self.A[i],self.A[j]=self.A[j],self.A[i]

		return self.__str__()

	def reverse(self):
		for i in range(self.n//2):
			self.A[i],self.A[self.n-i-1]=self.A[self.n-i-1],self.A[i]

		return self.__str__()

	def binary_search(self,item):
		start=0
		end=self.n-1
		
		while(start<end):
			mid=(start+end)//2
			if(self.A[mid]==item):
				return mid
			elif(self.A[mid]<item):
				end=mid
			else:
				start=mid
		return "Dhayan se element search kar list mai hai hi nahi"

	def append(self,item):
		if(self.size==self.n):
			self.__resize(self.size*2)
		self.A[self.n]=item
		self.n+=1

	def pop(self):
		if(self.n==0):
			return "Error - List is Empty"
		print(self.A[self.n-1])
		self.n-=1
		self.count+=1


	def insert(self,pos,item):
		if(self.n>=pos):

			if(self.size==self.n):
				self.__resize(self.size*2)
			for i in range(self.n-1,pos,-1):
				self.A[i]=self.A[i+1]
			self.A[pos]=item
			self.n+=1
		else:
			print("Error -Index out of range")

	def remove(self,ele):
		pos=self.find(ele)
		if (type(pos==int)):
			for i in range(pos,self.n):
				self.A[i]=self.A[i+1]
			self.n-=1
			self.count+=1

	def __resize(self,capacity):
		new=(capacity*ctype.py_object)()
		self.size=capacity
		for i in range(self.n):
			new[i]=self.A[i]
		self.A=new

	def __str__(self):
		result=''
		for i in range(self.n):
			result+=str(self.A[i])+","
		return "["+result[:-1]+"]"

	def __getitem__(self,index):
		if(type(index)==int):
			if 0<index<self.n:
				return self.A[index]
			elif(0>index>=	-(self.n)):
				return self.A[self.n+index]
			return "Index Error"
		elif(type(index)==slice):

			print(self.list_slice(index.start,index.stop,index.step))


	def list_slice(self,start,stop,step):
			if(start==None):
				start=0
			if(stop==None):
				stop=self.n
			if(step==None):
				step=1
			new_arr=self.__makearr((stop-start)//step+1)
			count1=0
			for i in range(start,stop,step):
				new_arr[count1]=self.A[i]
				count1+=1
			result=''
			for i in range(count1):
				result+=str(new_arr[i])+","
			return "["+result[:-1]+"]"

	def __makearr(self,capacity):
		return (capacity*ctype.py_object)()

new=apna_list()

new.append(10)
new.append(40)
new.append(30)
new.append(50)
new.insert(4,50)

print(len(new))
print(new)
new.pop()
new.remove(10)
print(new[-3])
new.find(30)
print(new)
print(new.reverse())

