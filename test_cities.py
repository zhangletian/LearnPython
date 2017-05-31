import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
	def test_city_country(self):
		formatted_message = city_country('santiago','chile')
		self.assertEqual(formatted_message,'Santiago,Chile')
	
	def test_city_country_population(self):
		formatted_message = city_country('santiago','chile',population=5000000)
		self.assertEqual(formatted_message,'Santiago,Chile - population 5000000')
	
unittest.main()
