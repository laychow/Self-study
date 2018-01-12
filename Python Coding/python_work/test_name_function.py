
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""test name_function.py"""
	def test_full_name(self):
		formatted_name=get_formatted_name('lay','chow')
		self.assertEqual(formatted_name,"Lay Chow")


unittest.main()
