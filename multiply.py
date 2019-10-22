import math

"Very simple algorithm that multiples two numbers using addition operation"
def naive(a, b):
	x = a; y = b
	z = 0
	while x > 0:
		z = z + y
		x = x - 1
	return z

def rec_naive(a, b):
	if a == 0:
		return 0
	return b + rec_naive(a-1, b)

def time_for_naive(a):
	return 3 + (2*a)


"Russian Peasant algorithm multiplies two numbers but uses mod and bitwise operators to perform this operation"
def russianpeasant(a, b):
	x = a; y = b
	z = 0
	while x > 0:
		if x % 2 == 1: z = z + y
		y = y << 1
		x = x >> 1
	return z

def rec_russianpeasant(a,b):
	if a == 0:
		return 0
	if a % 2 == 0:
		return rec_russianpeasant(a >> 1, b << 1)
	return b + rec_russianpeasant(a >> 1, b << 1)

def time_for_russian(a):
	return 3 + math.ceil((math.log(a) + 1)) * 3


def multiple2numbers(a,b):
	print("Naive Algorithm")
	print(naive(a,b))
	print(rec_naive(a,b))
	print(time_for_naive(a))
	print("Russian Peasant Algorithm")
	print(russianpeasant(a,b))
	print(rec_russianpeasant(a,b))
	print(time_for_russian(a))


multiple2numbers(80,11)