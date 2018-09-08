import unittest
from stack import Stack


class StackTest(unittest.TestCase):
	def setUp(self):
		self.stack = Stack()

	def testCreate(self):
		self.assertEqual(self.stack.isEmpty(), True)

	def test_Push_and_Top(self):
		self.stack.push(1)
		self.assertEqual(1, self.stack.top())

	def test_Push_and_Size(self):
		self.stack.push(1)
		self.assertEqual(1, self.stack.size())
