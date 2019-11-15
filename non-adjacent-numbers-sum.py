# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, 
# [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

def max_sum(arr):
	incl = 0
	excl = 0

	for n in arr:
		prev_incl = incl

		incl = excl + n
		excl = prev_incl if prev_incl > excl else excl

	return (excl if excl > incl else incl)

assert max_sum([2, 4, 6, 2, 5]) == 13
assert max_sum([5, 1, 1, 5]) == 10
assert max_sum([3, 2, 7, 10]) == 13
assert max_sum([3, 2, 5, 10, 7]) == 15
assert max_sum([3, 2, -5, 10, 7]) == 13
assert max_sum([-3, 2, 7, 10]) == 12
