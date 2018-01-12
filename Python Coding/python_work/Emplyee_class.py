class Employee():
	def _init_(self,first,last,salary):
		self.first_name=first
		self.last_name=last
		self.salary=salary
	
	def give_raise(self,increase=5000):
		self.salary+=increase
		
	def Information_display(self):
		full_name=first_name+' '+last_name
		print("\nName: "+full_name.title()+" "+salary);
		
		
