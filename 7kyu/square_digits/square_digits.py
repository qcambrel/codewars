def square_digits(num):
	digits = list(map(int, str(num)))
	squared_digits = [str(digits[k]**2) for k in range(len(digits))]
	return int(("").join(squared_digits))

if __name__ == "__main__":
	assert square_digits(9119) == 811181