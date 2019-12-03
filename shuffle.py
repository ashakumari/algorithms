# Shuffle a given array with uniformly random permutation

# Knuth shuffle linear time algorithm O(N)
import random

def shuffle(a):

	n = len(a)

	for i in range(n):
		r = random.choice(range(0, i+1))
		temp = a[i]
		a[i] = a[r]
		a[r] = temp
	
	return a

assert shuffle([2, 3, 5, 10, 15, 22, 29]) != [2, 3, 5, 10, 15, 22, 29]
assert shuffle([-22, -15, -5, 2, 3, 10, 29]) != [-22, -15, -5, 2, 3, 10, 29]
assert shuffle(["bat", "cat", "mat", "pat", "rat", "sat"]) != ["bat", "cat", "mat", "pat", "rat", "sat"]