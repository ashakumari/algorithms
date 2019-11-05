# Given 2 arrays a1,a2 and a target_sum, find the pair from the two arrays that produces a sum closest to the target_sum given

def closest_sum_pair_bruteforce(a1, a2, target_sum)
    
    closest_pair = nil
	closest_pair_diff_to_target = nil
	diff_to_target = nil

    for i in (0...a1.length)
    	for j in (0...a2.length)
    		diff_to_target = (target_sum - (a1[i] + a2[j])).abs()

    		if diff_to_target == 0
				return [ a1[i], a2[j] ]
			end

			if closest_pair_diff_to_target.nil? or diff_to_target < closest_pair_diff_to_target
				closest_pair = [ a1[i], a2[j] ]
				closest_pair_diff_to_target = diff_to_target
			end
    	end
    end

    return closest_pair
end

def time_for_bruteforce(a1, a2)
	return (a1.length * a2.length)
end

def closest_sum_pair_optimized(a1, a2, target_sum)

	a1_sorted = a1.sort
	a2_sorted = a2.sort

	closest_pair = nil
	closest_pair_diff_to_target = nil
	diff_to_target = nil

	i = 0
	j = a2_sorted.length - 1

    while i < a1_sorted.length && j >= 0

		diff_to_target = target_sum - (a1_sorted[i] + a2_sorted[j])

		if diff_to_target == 0
			return [ a1_sorted[i], a2_sorted[j] ]
		end

		if closest_pair_diff_to_target.nil? or diff_to_target.abs() < closest_pair_diff_to_target
			closest_pair = [ a1_sorted[i], a2_sorted[j] ]
			closest_pair_diff_to_target = diff_to_target.abs()
		end

		if diff_to_target > 0
			i += 1
		else
			j -= 1
		end	
    end

    return closest_pair
end

def time_for_optimized(a1, a2)
	return (a1.length + a2.length)
end

def find_closest_sum_pair(a1, a2, target_sum)
	print("\n\n Find closest sum pair for the following parameters: ")
	print("\n Array 1 " + a1.to_s)
	print("\n Array 2 " + a2.to_s)
	print("\n Target sum " + target_sum.to_s)

	print("\n\n Closest pair using bruteforce method : ")
	print(closest_sum_pair_bruteforce(a1, a2, target_sum))
	print("\n Time complexity : " + time_for_bruteforce(a1, a2).to_s)

	print("\n\n Closest pair using optimized method : ")
	print(closest_sum_pair_optimized(a1, a2, target_sum))
	print("\n Time complexity : " + time_for_optimized(a1, a2).to_s)
end

test_data = {
	0 => {
		'a1' => [-1, 3, 8, 2, 9, 5],
		'a2' => [4, 1, 2, 10, 5, 20],
		'target_sum' => 24
	},
	1 => {
		'a1' => [7, 4, 1, 10],
		'a2' => [4, 5, 8, 7],
		'target_sum' => 13
	},
	2 => {
		'a1' => [6, 8, -1, -8, -3],
		'a2' => [4, -6, 2, 9, -3],
		'target_sum' => 3
	},
	3 => {
		'a1' => [19, 14, 6, 11, -16, 14, -16, -9, 16, 13],
		'a2' => [13, 9, -15, -2, -18, 16, 17, 2, -11, -7],
		'target_sum' => -15
	}
}

test_data.each_value do | dataset|
	find_closest_sum_pair(dataset['a1'],  dataset['a2'], dataset['target_sum'])
end


