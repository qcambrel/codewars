## Kata: IQ Test

# Bob is preparing to pass IQ test. The most frequent task in this test is
# to find out which one of the given numbers differs from the others. Bob
# observed that one number usually differs from the others in evenness. 
# Help Bob — to check his answers, he needs a program that among the given
# numbers finds one that is different in evenness, and return a position of
# this number.

# Keep in mind that your task is to help Bob solve a real IQ test, which 
# means indexes of the elements start from 1 (not 0)

# Examples :

# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

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