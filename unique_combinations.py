# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.


def get_unique_ways_count(n, possible_count_at_once):
	
	counter_arr = [0]*(n+1)
	counter_arr[0] = 1
	i = 1

	for i in range(1, n+1):
		for possible_step in possible_count_at_once:
			if counter_arr[i-possible_step] != 0:
				counter_arr[i] += counter_arr[i-possible_step]
		
		i += 1
	return counter_arr[n]


assert get_unique_ways_count(4, [1, 2]) == 5
assert get_unique_ways_count(6, [1, 3, 5]) == 8