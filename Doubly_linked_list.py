class node:
	def __init__(self,data):
		self.data=data
		self.prev=None
		self.next=None
		
class Doubly_ll:
	def __init__(self):
		self.head=None

	def addNode(self,data):
		new_node=node(data)
		if (self.head==None):
			self.head=new_node
		else:
			current=self.head
			while(current.next!=None):
				current=current.next

			current.next=new_node
			new_node.prev=current


	def Add_at_begin(self,data):
		new_node=node(data)
		if(self.head==None):
			self.head=new_node

		else:
			cur=self.head
			new_node.next=cur
			cur.prev=new_node
			self.head=new_node

	def printll(self):
		head1=self.head
		
		while(head1!=None):
			print(head1.data,"-->",end="")
			head1=head1.next
		print("None")



new=Doubly_ll()
new.addNode(10)
new.addNode(10)
new.addNode(10)
new.addNode(10)
new.Add_at_begin(20)
new.Add_at_begin(30)
new.printll()







