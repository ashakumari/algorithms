# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given 2 strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# eg: "waterbottle" is a rotation of "erbottlewat"

def is_string_rotation(s1, s2):
	
	new_string = s2 + s2
	substring_index = new_string.find(s1)
	s2_rotate = s2[substring_index:]+s2[0:substring_index]

	if s1 == s2_rotate:
		return True
	else:
		return False


def isSubstring(s1, s2):
	return s1.find(s2)

assert is_string_rotation("waterbottle", "erbottlewat") == True
assert is_string_rotation("waterbottle", "waterbottle") == True
assert is_string_rotation("erase", "seera") == True
assert is_string_rotation("waterbottle", "erbottlewa") == False
assert is_string_rotation("erase", "seerase") == False