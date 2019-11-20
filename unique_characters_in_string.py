# Determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Solution 1 : Bruteforce method is to compare each letter with every other letter in the string to check for duplicates. O(n2)

# Solution 2 : If no constraint of additional space or data structure, then use has List to keep track of each character already 
# visited while traversing through the string character by character and if the character already exists in the List, 
# return False. O(n)

# Solution 3 : sort the alphabets in the string. While traversing through the string character by character, if current character is same as 
# previous character, return False. O(n log n) - Because of sorting involved

# Solution 4 : Use a bit checker to set the corresponding bits for all 26 characters as visited and check if the bit is already set,
# to find the duplicate character. O(n) 

def has_all_unique_characters_bruteforce(str):
	str_len = len(str)

	for i in range(str_len-1):
		for j in range(i+1, str_len):
			if str[i] == str[j]:
				return False

	return True

def has_all_unique_characters(str):
	str = ''.join(sorted(str))
	str_len = len(str)

	for i in range(str_len-1):
		if str[i] == str[i+1]:
			return False

	return True

def has_all_unique_characters_optimized(str):
	checker = 0
	str_len = len(str)

	for i in range(str_len):

		bit_value = ord(str[i]) - ord('a')
		
		if (checker & (1 << bit_value)) > 0:
			return False

		checker |= (1 << bit_value)

	return True


assert has_all_unique_characters_bruteforce("abcd") == True
assert has_all_unique_characters_bruteforce("abccd") == False
assert has_all_unique_characters_bruteforce("aaaaaaaa") == False
assert has_all_unique_characters_bruteforce("abcdefghia") == False
assert has_all_unique_characters_bruteforce("abcdefghi") == True

assert has_all_unique_characters("abcd") == True
assert has_all_unique_characters("abccd") == False
assert has_all_unique_characters("aaaaaaaa") == False
assert has_all_unique_characters("abcdefghia") == False
assert has_all_unique_characters("abcdefghi") == True

assert has_all_unique_characters_optimized("abcd") == True
assert has_all_unique_characters_optimized("abccd") == False
assert has_all_unique_characters_optimized("aaaaaaaa") == False
assert has_all_unique_characters_optimized("abcdefghia") == False
assert has_all_unique_characters_optimized("abcdefghi") == True
