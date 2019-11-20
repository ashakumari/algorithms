# Given two strings, check if one is the permutation of another

# Time complexity of this is O(N log N)
def are_strings_permutations(str1, str2):
	str1 = ''.join(sorted(str1))
	str2 = ''.join(sorted(str2))

	if str1 == str2:
		return True
	
	return False

# Tine complexity of this is O(N) but with extra space for the hash table
def are_strings_permutations_optimized(str1, str2):
	str_hash = {}
	
	for c in str1:
		if c in str_hash:
			str_hash[c] += 1
		else:
			str_hash[c] = 1

	for c in str2:
		if str_hash.get(c) == None:
			return False
		else:
			str_hash[c] -= 1
			if str_hash[c] == 0:
				str_hash.pop(c)

	return True if len(str_hash) == 0 else False

assert are_strings_permutations("dry", "cry") == False
assert are_strings_permutations("mad", "dam") == True
assert are_strings_permutations("gigantic", "cantigig") == True
assert are_strings_permutations("dramatic", "drama") == False

assert are_strings_permutations_optimized("dry", "cry") == False
assert are_strings_permutations_optimized("mad", "dam") == True
assert are_strings_permutations_optimized("gigantic", "cantigig") == True
assert are_strings_permutations_optimized("dramatic", "drama") == False