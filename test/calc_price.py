import unittest
from calc_price import Calc_price


class CalcTest(unittest.TestCase):
	def setUp(self):
		self.calc_price = Calc_price()

	def testPrice(self):
		self.assertEqual(self.calc_price.calc_price([10, 12]), 24)
		self.assertEqual(self.calc_price.calc_price([40, 16]), 62)
		self.assertEqual(self.calc_price.calc_price([100, 45]), 160)
		self.assertEqual(self.calc_price.calc_price([50, 50, 55]), 171)
		self.assertEqual(self.calc_price.calc_price([]), 0)
		self.assertEqual(self.calc_price.calc_price([40, 15]), 61)
