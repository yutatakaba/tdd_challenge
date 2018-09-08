import sys
from input_list import Input_list
from output_list import Output_list


class Calc_price:
	def __init__(self):
		pass

	def calc_price(self, price_list):
		round = lambda x: (x * 2 + 1) // 2
		sum = 0
		for price in price_list:
			sum = sum + price
		result = sum * 1.10
		result = round(result)
		result = int(result)
		return result

	def calc_print(self, input_list):
		output = []
		for calc_list in input_list:
			output.append(self.calc_price(calc_list))
		return output


def calc_tax(input_place, output_place):
	input_list = Input_list(input_place)
	output_list = Output_list(output_place)
	calc_price = Calc_price()

	input = input_list.input_list()
	output = calc_price.calc_print(input)
	output_list.output_list(output)


if __name__ == '__main__':
	calc_tax(sys.stdin, sys.stdout)
