## Kata: Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

def find_missing_letter(chars):
	ints = [ord(char) for char in chars]
	for k in range(len(ints)):
		if ints[k + 1] > (ints[k] + 1):
			return str(unichr(ints[k] + 1))

if __name__ == "__main__":
	assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
	assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'