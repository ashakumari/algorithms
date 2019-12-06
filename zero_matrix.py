# Write an algorithm such that if an element in an MXN matrix is 0, its entire row and column are set to 0

# Time complexity O(M*N) and Space complexity O(M+N)
def zero_matrix(a):
	n = len(a)
	m = len(a[0])
	zero_rows = []
	zero_columns = []

	for i in range(n):
		for j in range(m):
			if a[i][j] == 0:
				zero_rows.append(i)
				zero_columns.append(j)

	for r in zero_rows:
		for c in range(m):
			a[r][c] = 0

	for c in zero_columns:
		for r in range(n):
			a[r][c] = 0
	
	return a

# Time complexity O(M*N) and Space complexity O(1)
def zero_matrix_optimized(a):
	n = len(a)
	m = len(a[0])

	first_row_zero = False
	first_column_zero = False

	for i in range(n):
		for j in range(m):
			if a[i][j] == 0:
				a[i][0] = 0
				a[0][j] = 0
				if (i == 0):
					first_row_zero = True
				if (j == 0):
					first_column_zero = True

	for i in range(1, n):
		for j in range(1, m):
			if a[i][0] == 0 or a[0][j] == 0:
				a[i][j] = 0

	if first_row_zero:
		for c in range(m):
			a[0][c] = 0

	if first_column_zero:
		for r in range(n):
			a[r][0] = 0
	
	return a

def print_matrix(a):
	n = len(a)
	m = len(a[0])
	print("\n", end=" ")
	for i in range(n):
		for j in range(m):
			print(a[i][j], end=" ")
		print("\n", end=" ")

assert zero_matrix([[1,2,3,4,9],[5,0,7,8,8],[9,10,11,12,6],[13,14,0,15,16]]) == [[1,0,0,4,9],[0,0,0,0,0],[9,0,0,12,6],[0,0,0,0,0]]
assert zero_matrix([[1,2,3],[0,5,9],[3,3,0],[4,4,4]]) == [[0,2,0],[0,0,0],[0,0,0],[0,4,0]]
assert zero_matrix([[1,2,0],[1,5,9],[3,3,0],[4,4,4]]) == [[0,0,0],[1,5,0],[0,0,0],[4,4,0]]
assert zero_matrix([[1,2,10],[1,5,9],[3,3,10],[4,4,4]]) == [[1,2,10],[1,5,9],[3,3,10],[4,4,4]]

assert zero_matrix_optimized([[1,2,3,4,9],[5,0,7,8,8],[9,10,11,12,6],[13,14,0,15,16]]) == [[1,0,0,4,9],[0,0,0,0,0],[9,0,0,12,6],[0,0,0,0,0]]
assert zero_matrix_optimized([[1,2,3],[0,5,9],[3,3,0],[4,4,4]]) == [[0,2,0],[0,0,0],[0,0,0],[0,4,0]]
assert zero_matrix_optimized([[1,2,0],[1,5,9],[3,3,0],[4,4,4]]) == [[0,0,0],[1,5,0],[0,0,0],[4,4,0]]
assert zero_matrix_optimized([[1,2,10],[1,5,9],[3,3,10],[4,4,4]]) == [[1,2,10],[1,5,9],[3,3,10],[4,4,4]]