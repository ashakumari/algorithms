# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def get_longest_substring(str, k):

	n = len(str)
	start = 0
	end = 0
	char_count_hash = {}
	longest_substr = ""

	for i in range(n):
		if str[i] in char_count_hash:
			char_count_hash[str[i]] = char_count_hash[str[i]] + 1
		else:
			char_count_hash[str[i]] = 1

		while len(char_count_hash) > k:
			remove_char = str[start]
			start += 1
			char_count_hash[remove_char] = char_count_hash[remove_char] - 1
			if char_count_hash[remove_char] == 0:
				char_count_hash.pop(remove_char)

		new_substr = str[start:i+1]
		if len(new_substr) > len(longest_substr):
			longest_substr = new_substr

	return len(longest_substr)

assert get_longest_substring("abcba", 2) == 3
assert get_longest_substring("aabcbcaac", 2) == 4
assert get_longest_substring("aabcbcaac", 4) == 9
assert get_longest_substring("aabcdbceaacded", 4) == 8
assert get_longest_substring("karappa", 2) == 4
assert get_longest_substring("aabbcc", 1) == 2
assert get_longest_substring("aabbcc", 2) == 4
assert get_longest_substring("aabbcc", 3) == 6
assert get_longest_substring("aaabbb", 3) == 6
assert get_longest_substring("abcbbbbcccbdddadacb", 2) == 10


