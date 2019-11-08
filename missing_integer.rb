# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def find_missing_positive_integer_bruteforce(a)
	
	i = 1

	while i
		i_found = false
		for n in a
			if (n == i)
				i_found = true
				i += 1
				break
			end
		end
		if i_found == false
			return i
		end
	end
end

def find_missing_positive_integer_optimized(a)
	a.sort!
	a_len = a.size
	counter = 0
	i = 0

	while i < a_len
		if a[i] > counter
			counter += 1
			if a[i] != counter
				return counter
			end
		end
		i += 1
	end
	return counter+1
end


test_data = {
	'0' => {
		'input_data' => [3, 4, -1, 1],
		'expected_result' => 2
	},
	'1' => {
		'input_data' => [1, 2, 0],
		'expected_result' => 3
	},
	'2' => {
		'input_data' => [-9, 8, -6, 4, 12, 4, 40, 3, -15, 5, 10, -7, 7, 1, 2, 0, 6],
		'expected_result' => 9
	}
}

test_data.each do |key, dataset|
	puts find_missing_positive_integer_bruteforce(dataset['input_data']) == dataset['expected_result']
	puts find_missing_positive_integer_optimized(dataset['input_data']) == dataset['expected_result']
end