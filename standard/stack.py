# Stack implementation

class Stack:

	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)

	def pop(self):
		n = len(self.items)
		return None if self.is_empty() else self.items.pop(n-1)

	def peek(self):
		n = len(self.items)
		return None if self.is_empty() else self.items[n-1]

	def is_empty(self):
		return True if len(self.items) == 0 else False

	def values(self):
		return self.items


def parse_string(str):
	
	str_stack = Stack()
	result = ""
 
	for c in str:
		if c == '-':
			result += str_stack.pop()
		else:
			str_stack.push(c)

	return result

assert parse_string("12345-----") == "54321"
assert parse_string("5-4-3-2-1-") == "54321"
assert parse_string("15-24-3---") == "54321"






