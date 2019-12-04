# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def remove_duplicates(nums):
	
	n = len(nums)

	if n == 0:
		return 0

	last_visited_num = nums[0]
	i = 1
	duplicate_count = 0

	while i < n:
		while nums[i] == last_visited_num:
			duplicate_count += 1
			if i < n-1:
				i += 1
			else:
				break

		last_visited_num = nums[i]
		if duplicate_count > 0:
			temp = nums[i]
			nums[i] = nums[i-duplicate_count]
			nums[i-duplicate_count] = temp
		i += 1

	print(nums)

	return n-duplicate_count

assert remove_duplicates([1,1,2]) == 2
assert remove_duplicates([0,0,1,1,1,2,2,3,3,4]) == 5
assert remove_duplicates([1,1]) == 1