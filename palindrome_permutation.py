# Given a string, check if it is a permutation of palindrome string

# Time complexity O(N) but needs extra space to store the hash table
def is_palindrome_permutation(str):

	char_hash = {}
	odd_no_of_characters = 0
	str = str.lower()

	for c in str:
		if c == ' ':
			continue
		if char_hash.get(c) == None:
			char_hash[c] = 1
			odd_no_of_characters += 1
		else:
			char_hash[c] += 1			
			if char_hash[c] % 2 == 0:
				odd_no_of_characters -= 1
			else:
				odd_no_of_characters += 1
	
	return True if odd_no_of_characters == 1 or odd_no_of_characters == 0 else False


# Time complexity O(N) without additional data structure or huge space consumption using bit vector
def is_palindrome_permutation_optimized(str):
	
	checker = 0
	str_len = len(str)
	str = str.lower()

	for c in str:
		if c == ' ':
			continue

		bit_value = ord(c) - ord('a')
		mask = 1 << bit_value

		if (checker & mask) == 0:
			checker |= mask
		else:
			checker &= ~mask

	return True if checker & (checker - 1) == 0 else False

assert is_palindrome_permutation("damam") == True
assert is_palindrome_permutation("damdam") == True
assert is_palindrome_permutation("damdamam") == False
assert is_palindrome_permutation("Tact coa") == True

assert is_palindrome_permutation_optimized("damam") == True
assert is_palindrome_permutation_optimized("damdam") == True
assert is_palindrome_permutation_optimized("damdamam") == False
assert is_palindrome_permutation_optimized("Tact coa") == True