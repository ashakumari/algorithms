# Insertion sort implementation

# Time Complexity O(N2) for compares and O(N-1) for exchange; commplexity reduces to O(N) for compares and O(0) for the sorted array
def insertion_sort(a):
	
	n = len(a)

	for i in range(1, n):
		for j in range(i, 0, -1):
			if a[j] < a[j-1]:
				temp = a[j-1]
				a[j-1] = a[j]
				a[j] = temp
			else:
				break

	return a

assert insertion_sort([10, 15, 2, 5, 29, 22, 3]) == [2, 3, 5, 10, 15, 22, 29]
assert insertion_sort([10, -15, 2, -5, 29, -22, 3]) == [-22, -15, -5, 2, 3, 10, 29]
assert insertion_sort(["rat", "mat", "sat", "bat", "cat", "pat"]) == ["bat", "cat", "mat", "pat", "rat", "sat"]
