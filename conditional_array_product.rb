# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

def array_product_bruteforce(a)
	prod = Array.new(a.size)
	i = 0

	while i < a.size
		c = a[0..a.size]
		c.delete_at(i)
		prod[i] = c.inject(:*)
		i += 1
	end
	return prod
end

def array_product_optimized(a)
	prod = Array.new(a.size)
	full_product_with_zero = a.inject(:*)
	full_product_without_zero = a.reject(&:zero?).inject(:*)
	i = 0

	while i < a.size
		if a[i] == 0
			prod[i] = full_product_without_zero
		else
			prod[i] = full_product_with_zero / a[i]
		end	
		i += 1
	end
	return prod
end

def array_product_without_division(a)
	n = a.size
	left = Array.new(a.size)
	right = Array.new(a.size)
	prod = Array.new(a.size)

	left[0] = 1
	i = 1
	while i < a.size
		left[i] = a[i-1] * left[i-1]
		i += 1
	end

	right[n-1] = 1
	i = n-2
	while i >= 0
		right[i] = a[i+1] * right[i+1]
		i -= 1
	end

	i=0
	while i < a.size
		prod[i] = left[i] * right[i]
		i += 1
	end

	return prod
end

test_data = {
	'0' => [1, 2, 3, 4, 5],
	'1' => [7, 6, 5, 4, 3],
	'2' => [5, 0, 3, 2, 8]
}

test_data.each do |key, dataset|
	print("\n\nConditional product array using for #{dataset.to_s} : ")
	print("\n-- Using bruteforce method : " + array_product_bruteforce(dataset).to_s)
	print("\n-- Using optimized method : " + array_product_optimized(dataset).to_s)
	print("\n-- Using optimized method without division : " + array_product_without_division(dataset).to_s)
end