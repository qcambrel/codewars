def find_missing_letter(chars):
	ints = [ord(char) for char in chars]
	for k in range(len(ints)):
		if ints[k + 1] > (ints[k] + 1):
			return str(unichr(ints[k] + 1))

if __name__ == "__main__":
	assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
	assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'