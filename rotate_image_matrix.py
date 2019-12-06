# Given an image represented by NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
# Try doing it in-place

def rotate_image_90_bruteforce(a):
	n = len(a)
	d = [[0 for i in range(n)] for j in range(n)] 

	for r in range(n):
		for c in range(n):
			d[c][n-r-1] = a[r][c]

	return d

def rotate_image_90_inplace(a):
	n = len(a)

	for r in range(n):
		for c in range(r, n):
			t = a[r][c]
			a[r][c] = a[c][r]
			a[c][r] = t

	for r in range(n):
		for c in range(n//2):
			t = a[r][c]
			a[r][c] = a[r][n-c-1]
			a[r][n-c-1] = t

	return a

def rotate_image_180_bruteforce(a):
	n = len(a)
	d = [[0 for i in range(n)] for j in range(n)] 

	for r in range(n):
		for c in range(n):
			d[n-r-1][n-c-1] = a[r][c]

	return d

def print_matrix(a):
	n = len(a)
	print("\n", end=" ")
	for i in range(n):
		for j in range(n):
			print(a[i][j], end=" ")
		print("\n", end=" ")

assert rotate_image_90_bruteforce([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
assert rotate_image_90_inplace([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]

assert rotate_image_180_bruteforce([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]) == [[16,15,14,13],[12,11,10,9],[8,7,6,5],[4,3,2,1]]
