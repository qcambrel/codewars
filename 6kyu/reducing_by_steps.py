## Kata: Reducing by steps

# Data: an array of integers, a function f of two variables and an init value.

# Example: a = [2, 4, 6, 8, 10, 20], f(x, y) = x + y; init = 0

# Output: an array of integers, say r, such that

# r = [r[0] = f(init, a[0]), r[1] = f(r[0], a[1]), r[2] = f(r[1], a[2]), ...]

# With our example: r = [2, 6, 12, 20, 30, 50]

# Task:

# Write the following functions of two variables

# som : (x, y) -> x + y
# mini : (x, y) -> min(x, y)
# maxi : (x, y) -> max(x, y)
# lcmu : (x, y) -> lcm(abs(x), abs(y) (see note for lcm)
# gcdi : (x, y) -> gcd(abs(x), abs(y) (see note for gcd)
# and

# function oper_array(fct, arr, init) (or operArray or oper-array) where

# fct is the function of to variables to apply to the array arr (fct will be one of som, mini, maxi, lcmu or gcdi)
# init is the initial value
# Examples:

# a = [18, 69, -90, -78, 65, 40]
# oper_array(gcd, a, a[0]) => [18, 3, 3, 3, 1, 1]
# oper_array(lcm, a, a[0]) => [18, 414, 2070, 26910, 26910, 107640]
# oper_array(sum, a, 0) => [18, 87, -3, -81, -16, 24]
# oper_array(min, a, a[0]) => [18, 18, -90, -90, -90, -90]
# oper_array(max, a, a[0]) => [18, 69, 69, 69, 69, 69]
# Notes:

# The form of the parameter fct in oper_array (or operArray or oper-array) changes according to the language. You can see each form according to the language in "Your test cases".
# AFAIK there are no corner cases, everything is as nice as possible.
# lcm and gcd see: https://en.wikipedia.org/wiki/Least_common_multiple https://en.wikipedia.org/wiki/Greatest_common_divisor
# you could google "reduce function (your language)" to have a general view about the reduce functions.

def gcdi(a, b):
	b, a = sorted([abs(a), abs(b)])
	quotient = a // b
	remainder = a % b
	while remainder > 0:
		a = b
		b = remainder
		quotient = a // b
		remainder = a % b
	return b

def lcmu(a, b):
	return abs(a * b) / gcdi(a, b)

def som(a, b):
	return a + b

def maxi(a, b):
	return max(a, b)

def mini(a, b):
	return min(a, b)

def oper_array(fct, arr, init): 
	r = []
	for k in range(len(arr)):
		if r:
			r.append(fct(r[k - 1],arr[k]))
		else:
			r.append(fct(init, arr[k]))
	return r

if __name__ == "__main__":
	a = [ 18, 69, -90, -78, 65, 40 ]
	print(oper_array(gcdi, a, a[0]))
	assert oper_array(gcdi, a, a[0]) == [18, 3, 3, 3, 1, 1]
	assert oper_array(lcmu, a, a[0]) == [18, 414, 2070, 26910, 26910, 107640]
	assert oper_array(som, a, 0) == [18, 87, -3, -81, -16, 24]
	assert oper_array(mini, a, a[0]) == [ 18, 18, -90, -90, -90, -90 ]
	assert oper_array(maxi, a, a[0]) == [18, 69, 69, 69, 69, 69]