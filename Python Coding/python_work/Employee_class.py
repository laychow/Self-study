class Employee():
	def __init__(self,first,last,salary):
		self.first_name=first
		self.last_name=last
		self.salary=salary
	
	def give_raise(self,increase=5000):
		self.salary+=increase
		
	def information_display(self):
		full_name=self.first_name+' '+self.last_name
		return "\nName: "+full_name.title()+" "+str(self.salary)
		
		
