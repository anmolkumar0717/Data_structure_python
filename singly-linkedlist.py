class Node:
	def __init__(self,data):
		self.data=data
		self.ref=None
		

class linkedlist():
	def __init__(self):
		self.head=None
		self.n=0

	def add_begin(self,data):
		new_node=Node(data)
		new_node.ref=self.head
		self.head=new_node
		self.n+=1

	def add_at_end(self,data):
		new_node1=Node(data)
		if(self.head==None):
			self.add_begin(data)
			self.n+=1

		else:
			new_ref=self.head
			while(new_ref.ref!=None):
				new_ref=new_ref.ref

			new_ref.ref=new_node1
			new_node1.ref=None
			self.n+=1

	def del_node_begin(self):
		self.head=self.head.ref
		self.n-=1

	def replace_with(self,val):
		temp=self.head
		cur=self.head
		max_ll_val=self.head.data
		while(temp.ref!=None):
			if(max_ll_val<temp.ref.data):
				max_ll_val=temp.ref.data
				cur=temp.ref
			temp=temp.ref
		cur.data=val

	def sum_odd_node(self):
		odd_sum=0
		count=0
		temp=self.head
		while temp!=None:
			if(count%2==0):
				odd_sum+=temp.data
			count+=1
			temp=temp.ref
		print(odd_sum)

	def printll(self):
		ref1=self.head
		if (ref1==None):
			print("!!! Empty LinkedList !!!")
		else:
			while(ref1!=None):
				print(ref1.data,"-->",end="")
				ref1=ref1.ref
			print("None")

	def reverse(self):

		curr=self.head
		prev=None
		while(curr!=None):
			next_node=curr.ref
			curr.ref=prev
			prev=curr
			curr=next_node

			
		new=self.head
		self.head=prev
		new=None
		
	def length(self):
		print(self.n)


firstnode=linkedlist()

firstnode.add_begin(19)
firstnode.add_begin(30)
firstnode.add_begin(99)

firstnode.printll()
firstnode.replace_with(10)
firstnode.sum_odd_node()
firstnode.printll()
firstnode.length()
firstnode.reverse()
firstnode.printll()




