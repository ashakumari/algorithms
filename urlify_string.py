# Replace all spaces in a string with %20. Trailing spaces can be ignored as the length of the string would be provided

def urlify(str, len):
	return str.strip().replace(" ", "%20")


def urlify_brutal(str, len):
	new_str = "" 
	for i in range(len):
		if str[i] == " ":
			new_str += "%20"
		else:
			new_str += str[i]

	return new_str

assert urlify("Mr Johnson", 10) == "Mr%20Johnson"
assert urlify("Mr John Smith", 13) == "Mr%20John%20Smith"
assert urlify("Mr John Smith      ", 13) == "Mr%20John%20Smith"

assert urlify_brutal("Mr Johnson", 10) == "Mr%20Johnson"
assert urlify_brutal("Mr John Smith", 13) == "Mr%20John%20Smith"
assert urlify_brutal("Mr John Smith      ", 13) == "Mr%20John%20Smith"