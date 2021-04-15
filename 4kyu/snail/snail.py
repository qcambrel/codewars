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

