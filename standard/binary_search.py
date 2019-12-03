# Binary search implemented - Find a given key in a given sorted array

# Time complexity O(log N)
def binary_search(a, key):
	
	n = len(a)
	low = 0
	high = n-1

	while low <= high:
		mid = (low + high)//2

		if a[mid] == key:
			return mid
		elif key > a[mid]:
			low = mid + 1
		else:
			high = mid - 1

	return -1

assert binary_search([2, 4, 6, 9, 15, 18], 15) == 4
assert binary_search([2, 6, 16, 18, 26, 65, 93], 60) == -1
assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0
assert binary_search([3, 5, 20, 34, 55, 67, 89, 105], 105) == 7
assert binary_search([2, 4, 6, 8, 10], 6) == 2
assert binary_search([3, 6, 9, 12, 15, 18], 12) == 3 
