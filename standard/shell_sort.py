# Shellsort implementation

# Time Complexity O(N3) for compares and O(N-1) for exchange; commplexity reduces to O(N) for compares and O(0) for the sorted array
def shell_sort(a):
	
	n = len(a)

	x = 1
	# Use 3x+1 sequencing
	while x < n//3:
		x = 3*x + 1

	while x >= 1:

		for i in range(x, n):
			j = i
			while j >= x and a[j] < a[j-x]:
				temp = a[j-x]
				a[j-x] = a[j]
				a[j] = temp
				j -= x
		x = x//3

	return a

assert shell_sort([10, 15, 2, 5, 29, 22, 3]) == [2, 3, 5, 10, 15, 22, 29]
assert shell_sort([10, -15, 2, -5, 29, -22, 3]) == [-22, -15, -5, 2, 3, 10, 29]
assert shell_sort(["rat", "mat", "sat", "bat", "cat", "pat"]) == ["bat", "cat", "mat", "pat", "rat", "sat"]
