class a:
	def __init__(self):
		self.name=None
		self.next=None
	
	def add_head(self,name):
		new_a = a()
		new_a.name=name
		new_a.next=None
		self.next =new_a
		
	def get(self,index):
		temp=self
		for i in range(index):
			temp=temp.next
		return temp.name
		

list_a = a()
list_a.add_head("zhangshuai0")
list_a.add_head("zhangshuai1")
list_a.add_head("zhangshuai2")
list_a.add_head("zhangshuai3")
list_a.get(2)
