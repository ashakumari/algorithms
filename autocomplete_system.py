# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

import re

def get_possible_query_strings(search_string, list_of_strings):
	matching_strings = []
	for str in list_of_strings:
		if re.match(search_string+".*", str):
			matching_strings.append(str)

	return matching_strings

assert get_possible_query_strings("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert get_possible_query_strings("de", ["dog", "deer", "ideal"]) == ["deer"]
assert get_possible_query_strings("abo", ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']) == ['abode', 'about', 'above']



