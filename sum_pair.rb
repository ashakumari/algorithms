# Given an array of size n and a number k, find if any two numbers in the array when added results in k or not

def is_sum_pair_exists_bruteforce(a, target_sum)

    for i in (0...a.length)
    	for j in (i+1...a.length)

    		if (a[i] + a[j] == target_sum)
    			return true
    		end
    	end
    end
    return false
end

def is_sum_pair_exists_optimized(a, target_sum)
	a.sort!()
	for i in (0...a.length)
    	for j in (i+1...a.length)

    		if (a[i] + a[j] == target_sum)
    			return true
    		end
    		if (a[i] + a[j] > target_sum)
    			break
    		end
    	end
    end
    return false
end

def is_sum_pair_exists_in_single_pass(a, target_sum)
	a_hash = Hash[a.collect { |number| [number, number ] } ]
	a_hash.each do |key, value|
		diff = target_sum - value
		if a_hash.has_key?(diff)
			return true
		end	
	end
	return false
end

def check_if_sum_pair_exists(a, target_sum)
	print("\n\n Check if a pair yielding the sum required exists for the following parameters: ")
	print("\n Array " + a.to_s)
	print("\n Required sum " + target_sum.to_s)

	print("\n\n Does the pair exists using bruteforce method? : ")
	print(is_sum_pair_exists_bruteforce(a, target_sum))

	print("\n Does the pair exists using optimized method? : ")
	print(is_sum_pair_exists_optimized(a, target_sum))

	print("\n Does the pair exists using single pass on hash method? : ")
	print(is_sum_pair_exists_in_single_pass(a, target_sum))
end

test_data = {
	0 => {
		'a' => [-1, 3, 8, 2, 9, 5],
		'k' => 13
	},
	1 => {
		'a' => [7, 4, 1, 10],
		'k' => 13
	},
	2 => {
		'a' => [6, 8, -1, -8, -3],
		'k' => 4
	},
	3 => {
		'a' => [19, 14, 6, 11, -16, 14, -16, -9, 16, 13],
		'k' => 3
	},
	4 => {
		'a' => [10, 15, 3, 7],
		'k' => 17
	}
}

test_data.each_value do | dataset|
	check_if_sum_pair_exists(dataset['a'], dataset['k'])
end