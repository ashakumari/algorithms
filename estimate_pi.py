# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

import random as rdm

def estimate_pi():

	# If x2 + y2 <= 1, it is inside circle; otherwise inside square
	# π = 4 * points inside circle / points inside square

	points_in_the_circle = 0
	points_in_the_square = 0

	for i in range(100000):
		x = rdm.random()
		y = rdm.random()

		if (x**2) + (y**2) <= 1:
			points_in_the_circle += 1
		
		points_in_the_square += 1

		
	pi = 4 * float(points_in_the_circle / points_in_the_square)

	print(round(pi, 3))


for i in range(10):
	estimate_pi()
