def dbl_linear(n):
	u = [1]
	x1, x2 = (0, 0)
	for i in range(n):
		y = 2 * u[x1] + 1
		z = 3 * u[x2] + 1
		if y <= z:
			u.append(y)
			x1 += 1
			if y == z:
				x2 += 1
		else:
			u.append(z)
			x2 += 1
	return u[n]

# Hamming numbers

assert dbl_linear(10) == 22
assert dbl_linear(20) == 57
assert dbl_linear(30) == 91
assert dbl_linear(50) == 175
assert dbl_linear(100) == 447
