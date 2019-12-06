# Implement a method to perform basic string compression using the count of repeated characters.
# For eg: the string "aabcccccaaa" would become "a2b1c5a3". 
# If the compressed string doesn't become smaller than original string, return the original string

# Using List instead of Direct string concatenation as 
# multiple ongoing string concatenation is performance intensive as the string is rebuilt again and again with each concatenation
def compress_string(st):

	n = len(st)

	if n == 0:
		return st
	
	compressed_str = ""
	l = []
	counter = 0
	i = 0

	while i < n:
		l.insert(counter, st[i])
		counter += 1
		char_count = 1
		while i < n-1 and st[i] == st[i+1]:
			char_count += 1
			i += 1
		l.insert(counter, str(char_count))
		counter += 1
		i += 1

	compressed_str = "".join(l)
	return compressed_str if len(compressed_str) < n else st

assert compress_string("aabcccccaaa") == "a2b1c5a3"
assert compress_string("abcdefgh") == "abcdefgh"
assert compress_string("aabcdef") == "aabcdef"
assert compress_string("aaabbcccccbbde") == "a3b2c5b2d1e1"
assert compress_string("aaabbcccbbde") == "aaabbcccbbde"
assert compress_string("abbbccccaaa") == "a1b3c4a3"

