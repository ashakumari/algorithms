# Find element of non-empty list l that maximizes the return value of function f

def findmax(f, l):
	best_element_sofar = None
	best_f_value_sofar = None

	for i in range(len(l)):
		ele = l[i]
		f_value = f(ele)
		if best_f_value_sofar == None or f_value > best_f_value_sofar:
			best_f_value_sofar = f_value
			best_element_sofar = ele

	return best_element_sofar

def apos(word):
	return word.find("a")

test_data = {
	'0': {
		'l': ["smart", "quirks", "sober", "dramatic", "lazy"],
		'f': len
	},
	'1': {
		'l': [5, 8, -12, -16, 9, 10, -4],
		'f': abs
	},
	'2': {
		'l': ["smart", "quirks", "sober", "dramatic", "creapy"],
		'f': apos
	}
}

for i in test_data:
	dataset = test_data[i]
	print(findmax(dataset['f'], dataset['l']))
