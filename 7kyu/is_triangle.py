## Kata: Is this a triangle?

# Implement a method that accepts 3 integer values a, b, c. The method
# should return true if a triangle can be built with the sides of given
# length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
	a, b, c = sorted([a, b, c])
	return a + b > c

if __name__ == "__main__":
	assert is_triangle(1, 2, 2) == True
	assert is_triangle(7, 2, 2) == False
	assert is_triangle(1, 2, 3) == False
	assert is_triangle(1, 3, 2) == False
	assert is_triangle(3, 1, 2) == False
	assert is_triangle(5, 4, 2) == True