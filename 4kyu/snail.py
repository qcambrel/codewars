## Kata: Snail

# Snail Sort

# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]

# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#         [8,9,4],
#         [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

# This image will illustrate things more clearly:
# http://www.haan.lu/files/2513/8347/2456/snail.png

# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as [[]]

def snail(matrix):
	contents = []
	while matrix:	# Each iteration is effectively edging off a square into a smaller square (n x n matrix)
		for item in matrix[0]:
			contents.append(item)
		matrix.pop(0)
		for row in matrix:
			if row:
				contents.append(row.pop(-1))
		if matrix:
			matrix[-1].reverse()
		if matrix:
			for item in matrix[-1]:
				contents.append(item)
		if matrix:
			matrix.pop(-1)
		matrix.reverse()
		for row in matrix:
			if row:
				contents.append(row.pop(0))
		matrix.reverse()
	return contents

# Note: Consider recursion and zip()

if __name__ == "__main__":
	assert snail([[1,2,3], [4,5,6], [7,8,9]]) == [1,2,3,6,9,8,7,4,5]
	assert snail([[1,2,3], [8,9,4], [7,6,5]]) == [1,2,3,4,5,6,7,8,9]

