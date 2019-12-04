# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def sum_pair_indices(a, target_sum):
	n = len(a)
	for i in range(n):
		for j in range(i+1, n):
			if a[i] + a[j] == target_sum:
				return [i, j]
	return None

def sum_pair_indices_in_single_pass(a, target_sum):
	n = len(a)
	a_dict = {}
	for i in range(n):
		diff = target_sum - a[i]
		if diff in a_dict:
			return [a_dict[diff], i]
		a_dict[a[i]] = i
	return None


test_data = {
	"0" : {
		'a' : [-1, 3, 8, 2, 9, 5],
		'k' : 13,
		'expected_result' : [2, 5]
	},
	"1" : {
		'a' : [7, 4, 1, 10],
		'k' : 13,
		'expected_result' : None
	},
	"2" : {
		'a' : [6, 8, -1, -8, -3],
		'k' : 4,
		'expected_result' : None
	},
	"3" : {
		'a' : [19, 14, 6, 11, -16, 14, -9, 16, 13],
		'k' : 3,
		'expected_result' : [0, 4]
	},
	"4" : {
		'a' : [10, 15, 3, 7],
		'k' : 17,
		'expected_result' : [0, 3]
	},
	"5" : {
		'a' : [3, 2, 4],
		'k' : 6,
		'expected_result' : [1, 2]
	},
	"6" : {
		'a' : [3, 3],
		'k' : 6,
		'expected_result' : [0, 1]
	}
}

for test_no in test_data:
	dataset = test_data[test_no]
	assert sum_pair_indices(dataset['a'], dataset['k']) == dataset['expected_result']
	assert sum_pair_indices_in_single_pass(dataset['a'], dataset['k']) == dataset['expected_result']