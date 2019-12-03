# Stack implementation

class Stack:

	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)


	def pop(self):
		n = len(self.items)
		return None if self.is_empty() else self.items.pop(n-1)

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

# Dijkstra's two-stack algorithm
def parse_arithmetic_expression(exp):

	value_stack = Stack()
	operator_stack = Stack()

	for c in exp:
		if c == ')':
			operator = operator_stack.pop()
			operand_2 = value_stack.pop()
			operand_1 = value_stack.pop()

			if operand_1 == None:
				return "Invalid Arithmetic Expression"

			value_stack.push(perform_operation(operator, operand_1, operand_2))
		elif c == '(':
			continue
		elif c == '+' or c == '-' or c == '*' or c == '/':
			operator_stack.push(c)
		else:
			value_stack.push(c)

	result = value_stack.pop()

	if not value_stack.is_empty() or not operator_stack.is_empty():
		return "Invalid Arithmetic Expression"
	else:
		return result

def perform_operation(operator, op1, op2):
	if operator == '*':
		return int(op1) * int(op2)
	elif operator == '/':
		return int(op1) / int(op2)
	elif operator == '+':
		return int(op1) + int(op2)
	elif operator == '-':
		return int(op1) - int(op2)

	return None


assert parse_arithmetic_expression("((4*5)+(6+3))") == 29
assert parse_arithmetic_expression("(1+((2+3)*(4*5)))") == 101

assert parse_arithmetic_expression("1+2*3") == "Invalid Arithmetic Expression"
assert parse_arithmetic_expression("1+(2*3)") == "Invalid Arithmetic Expression"
assert parse_arithmetic_expression("(1+(2*3)") == "Invalid Arithmetic Expression"






