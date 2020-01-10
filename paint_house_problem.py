# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

def minimum_painting_cost(nk):
	n = len(nk)
	k = len(nk[0])

	for i in range(1,n):
		for j in range(0,k):
			nk[i][j] = nk[i][j] + get_minimum_number(nk[i-1], j)

	return get_minimum_number(nk[n-1], None)

def get_minimum_number(a, skip_index):
	min = None

	for j in range(0, len(a)):
		if skip_index is not None and j == skip_index:
			continue
		if min is None or a[j] < min:
			min = a[j]

	return min


assert minimum_painting_cost([[5, 8, 7, 3], [6, 2, 9, 4], [1, 8, 6, 5]]) == 6
	