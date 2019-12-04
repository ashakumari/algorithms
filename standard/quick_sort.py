# Quick sort algorithm

# Time complexity O(N log N) and worst case (sorted, reversed etc.) could be O(N2) 
# But the performance is still better than mergesort as the operation done in each compare is simple
# This algorithm doesn't use extra space
# Shuffling is important to guarantee performance
import random

def quick_sort(a):
	shuffle(a)
	sort(a, 0, len(a)-1)
	return a

def shuffle(a):

	n = len(a)

	for i in range(n):
		r = random.choice(range(0, i+1))
		temp = a[i]
		a[i] = a[r]
		a[r] = temp

def sort(a, low, high):
	
	if low >= high:
		return

	key = partition(a, low, high)
	sort(a, low, key-1)
	sort(a, key+1, high)

def partition(a, low, high):

	ele = a[low]
	i = low + 1
	j = high

	while True:

		while a[i] < ele:
			i += 1
			if i > high:
				break

		while a[j] > ele:
			j -= 1
			if j < low:
				break

		if i >= j:
			break
		else:
			swap(a, i, j)

	swap(a, low, j)
	return j

def swap(a, i, j):

	temp = a[i]
	a[i] = a[j]
	a[j] = temp

assert quick_sort([10, 15, 2, 5, 29, 22, 3]) == [2, 3, 5, 10, 15, 22, 29]
assert quick_sort([10, -15, 2, -5, 29, -22, 3]) == [-22, -15, -5, 2, 3, 10, 29]
assert quick_sort(["rat", "mat", "sat", "bat", "cat", "pat"]) == ["bat", "cat", "mat", "pat", "rat", "sat"]
assert quick_sort([10, 15, 22, 15, 29, 22, 3]) == [3, 10, 15, 15, 22, 22, 29]

