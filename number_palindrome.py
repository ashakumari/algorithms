# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

def is_number_palindrome(n):
	s = str(n)
	s_rev = s[::-1]

	if s == s_rev:
		return True
	else:
		return False

assert is_number_palindrome(121) == True
assert is_number_palindrome(-121) == False
assert is_number_palindrome(10) == False