## Kata: Consecutive strings

# You are given an array strarr of strings and an integer k. Your task is
# to return the first longest string consisting of k consecutive strings
# taken in the array.

# Example:

# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

def longest_consec(strings, k):
	if len(strings) == 0 or k > len(strings) or k <= 0:
		return ""
	consecutive_strings = []
	for i in range(len(strings)):
		consecutive_strings.append("".join(strings[i:(k + i)]))
	longest_string = ""
	for string in consecutive_strings:
		if len(string) > len(longest_string):
			longest_string = string
	return longest_string


if __name__ == "__main__":
	assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta"
	assert longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == "oocccffuucccjjjkkkjyyyeehh"
	assert longest_consec([], 3) == ""
	assert longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
	assert longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) == "wlwsasphmxxowiaxujylentrklctozmymu"
	assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == ""
	assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz"
	assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) == ""
	assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) == ""