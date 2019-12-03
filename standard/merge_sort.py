# Merge sort implementation

# Time complexity O(N log N) compares with extra space of O(N) and the complexity remains the same for best case as well

def merge_sort(a):
	n = len(a)
	aux = [0]*n

	sort(a, aux, 0, n-1)
	return a

def sort(a, aux, low, high):
	
	if low >= high:
		return
	mid = (low + high) // 2
	sort(a, aux, low, mid)
	sort(a, aux, mid+1, high)
	merge(a, aux, low, mid, high)

def merge(a, aux, low, mid, high):
	for k in range(low, high+1):
		aux[k] = a[k]

	i = low
	j = mid+1
	
	for k in range(low, high+1):
		if i > mid:
			a[k] = aux[j]
			j += 1
		elif j > high:
			a[k] = aux[i]
			i += 1
		elif aux[j] < aux[i]:
			a[k] = aux[j]
			j += 1
		else:
			a[k] = aux[i]
			i += 1

assert merge_sort([10, 15, 2, 5, 29, 22, 3]) == [2, 3, 5, 10, 15, 22, 29]
assert merge_sort([10, -15, 2, -5, 29, -22, 3]) == [-22, -15, -5, 2, 3, 10, 29]
assert merge_sort(["rat", "mat", "sat", "bat", "cat", "pat"]) == ["bat", "cat", "mat", "pat", "rat", "sat"]