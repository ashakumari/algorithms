# Selection sort implementation

# Time Complexity O(N2) for compares and O(1) for exchange; complexity remains same even for the sorted array
def selection_sort(a):

	n = len(a)

	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			if a[j] < a[min_index]:
				min_index = j
		if i != min_index:
			temp = a[i]
			a[i] = a[min_index]
			a[min_index] = temp

	return a

assert selection_sort([10, 15, 2, 5, 29, 22, 3]) == [2, 3, 5, 10, 15, 22, 29]
assert selection_sort([10, -15, 2, -5, 29, -22, 3]) == [-22, -15, -5, 2, 3, 10, 29]
assert selection_sort(["rat", "mat", "sat", "bat", "cat", "pat"]) == ["bat", "cat", "mat", "pat", "rat", "sat"]