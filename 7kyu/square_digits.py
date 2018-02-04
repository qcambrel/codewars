## Kata: Square Every Digit

# Welcome. In this kata, you are asked to square every digit of a number.

# For example, if we run 9119 through the function, 811181 will come out.

# Note: The function accepts an integer and returns an integer

def square_digits(num):
	digits = list(map(int, str(num)))
	squared_digits = [str(digits[k]**2) for k in range(len(digits))]
	return int(("").join(squared_digits))

if __name__ == "__main__":
	assert square_digits(9119) == 811181