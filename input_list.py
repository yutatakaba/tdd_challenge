class Input_list:
	def __init__(self, io):
		self.io = io

	def input_list(self):
		result_list = []
		l_strip = [s.strip() for s in self.io.readlines()]
		for value in l_strip:
			line_list = value.split(',')
			try:
				line_list = [int(i) for i in line_list]
			except:
				line_list = []
			result_list.append(line_list)

		return result_list
