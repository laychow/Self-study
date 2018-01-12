import unittest
from Employee_class import Employee

class TestEmployee(unittest.TestCase):
	"""for Emplyee_class"""
	def setUp(self):
		self.my_information=Employee('lay','chow',10000)
		
	def test_give_default_raise(self):
		
		self.my_information.give_raise();
		
		self.assertEqual(self.my_information.information_display(),'\nName: Lay Chow 15000')
		
	def test_give_custon_raise(self):
		self.my_information.give_raise(10000)
		self.assertEqual(self.my_information.information_display(),"\nName: Lay Chow 20000")

unittest.main()
