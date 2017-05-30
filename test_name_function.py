import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	#≤‚ ‘name_function.py
	
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')

unittest.main()
