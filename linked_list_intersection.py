# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


# Time complexity O(M+N) and space complexity O(M)
def find_intersecting_point(l1, l2):
	l1_hash = {}


	
	for n in l1:
		l1_hash[n] = 1

	for n in l2:
		if l1_hash.get(n) != None:
			return n

	return None

def find_intersecting_point_optimized(l1, l2):
	m = len(l1)
	n = len(l2)
	i = 0
	j = 0

	d = abs(m-n)

	if m > n:
		i = i + d
	else:
		j = j + d

	while i < m:
		if l1[i] == l2[j]:
			return l1[i]
		i = i + 1
		j = j + 1

	return None


assert find_intersecting_point([3, 7, 8, 10], [99, 1, 8, 10]) == 8
assert find_intersecting_point([3, 7, 8, 11], [99, 1, 9, 10]) == None
assert find_intersecting_point([14,11,8,4,5], [15,0,1,8,4,5]) == 8
assert find_intersecting_point([0,9,1,2,4], [3,2,4]) == 2
assert find_intersecting_point([2,6,4], [1,5]) == None


assert find_intersecting_point_optimized([3, 7, 8, 10], [99, 1, 8, 10]) == 8
assert find_intersecting_point_optimized([3, 7, 8, 11], [99, 1, 9, 10]) == None
assert find_intersecting_point_optimized([14,11,8,4,5], [15,0,1,8,4,5]) == 8
assert find_intersecting_point_optimized([0,9,1,2,4], [3,2,4]) == 2
assert find_intersecting_point_optimized([2,6,4], [1,5]) == None