# Stack implementation
import stack

class SortedStack:

	def __init__(self):
		self.primary = stack.Stack()
		self.secondary = stack.Stack()
	
	def push(self, item):
		while not self.primary.is_empty() and self.primary.peek() < item:
			self.secondary.push(self.primary.pop())

		self.primary.push(item)
		while not self.secondary.is_empty():
			self.primary.push(self.secondary.pop())

	def pop(self):
		return self.primary.pop()

	def peek(self):
		return self.primary.peek()

	def is_empty(self):
		return self.primary.is_empty()

	def values(self):
		return self.primary.values()


def parse_string(str):
	
	str_stack = SortedStack()
	result = ""
 
	for c in str:
		if c == '-':
			result += str_stack.pop()
		else:
			str_stack.push(c)

	return result

assert parse_string("54321-----") == "12345"
assert parse_string("12345-----") == "12345"
assert parse_string("5-4-3-2-1-") == "54321"
assert parse_string("15-24-3---") == "12345"
