import unittest
from input_list import Input_list
from output_list import Output_list
from calc_price import Calc_price, calc_tax
import io
import os


class InputTest(unittest.TestCase):
	def setUp(self):
		self.input_list = Input_list(io.StringIO("""10,12
40,16
100,45

50,50,55"""))
		self.calc_price = Calc_price()

	def testInput(self):
		self.assertEqual(self.input_list.input_list(), [[10, 12], [40, 16], [100, 45], [], [50, 50, 55]])


class OutputTest(unittest.TestCase):
	def setUp(self):
		self.output = io.StringIO()
		self.output_list = Output_list(self.output)

	def testOutput(self):
		self.output = self.output_list.output_list([24, 62, 160, 0, 171])
		self.assertEqual(self.output.getvalue(), """24
62
160
0
171
""")


class CalcTest(unittest.TestCase):
	def testCalc(self):
		input_place = io.StringIO("""10,12
40,16
100,45

50,50,55""")

		output_place = io.StringIO()
		calc_tax(input_place, output_place)
		self.assertEqual(output_place.getvalue(), """24
62
160
0
171
""")
