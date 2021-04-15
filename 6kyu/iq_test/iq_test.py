def iq_test(numbers):
	numbers = numbers.split(" ")
	for k in range(len(numbers)):
		if int(numbers[k]) % 2 == 0:
			numbers[k] = "even"
		else:
			numbers[k] = "odd"
	if numbers.count("even") > 1:
		index = numbers.index("odd") + 1
	else:
		index = numbers.index("even") + 1
	return index

if __name__ == "__main__":
	assert iq_test("2 4 7 8 10") == 3
	assert iq_test("1 2 1 1") == 2