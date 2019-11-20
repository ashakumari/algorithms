# There are 3 types of edits that can be performed on strings: insert a character, remove a character or replace a character.
# Given two string, write a function to check if they are one edit (or zero edits) away.

def is_one_away(str1, str2):

	if len(str1) > len(str2):
		return get_difference(str1, str2)
	else:
		return get_difference(str2, str1)
	

def get_difference(str1, str2):

	str_len = len(str1)
	str2_len = len(str2)

	if str_len - str2_len > 1:
		return False

	diff_counter = 0

	j = 0
	for i in range(str_len):
		
		if j == len(str2):
			diff_counter += 1
			if diff_counter > 1:
				return False
			break

		if str1[i] == str2[j]:
			j += 1
			continue

		diff_counter += 1
		if diff_counter > 1:
			return False
			
		if str1[i+1] != str2[j]:
			j += 1

	return True

assert is_one_away("pale", "ple") == True
assert is_one_away("pales", "pale") == True
assert is_one_away("pale", "bale") == True
assert is_one_away("pale", "bales") == False
assert is_one_away("pale", "bake") == False
assert is_one_away("pal", "plea") == False
assert is_one_away("apple", "plea") == False
assert is_one_away("apple", "apple") == True
assert is_one_away("apple", "pleap") == False
assert is_one_away("app", "apples") == False