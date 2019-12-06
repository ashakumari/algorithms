import stack

# Dijkstra's two-stack algorithm
def parse_arithmetic_expression(exp):

	value_stack = stack.Stack()
	operator_stack = stack.Stack()

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