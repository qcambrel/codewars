def check_tombola(sheet):
	columns = list(zip(*sheet))
	squares = [square for row in sheet for square in row]
	has_right_dimensions = len(sheet) == 3 and len(columns) == 9
	has_uniques = True
	for x in squares:
		if squares.count(x) > 1 and x != 0:
			has_uniques = False
	each_row_has_five = True
	for k in range(len(sheet)):
		if sheet[k].count(0) != 4:
			each_row_has_five = False
	each_column_ascends = True
	for column in columns: 
		if len(list(filter(lambda x: x != 0, column))) == 0 or list(filter(lambda x: x != 0, column)) != sorted(list(filter(lambda x: x != 0, column))):
			each_column_ascends = False
	dividers = [list(range(1,10)), list(range(10,20)), list(range(20,30)),
				list(range(30,40)), list(range(40,50)), list(range(50,60)),
				list(range(60,70)), list(range(70,80)), list(range(80,91))]
	each_column_fits_divider = True
	if has_right_dimensions:
		for k in range(len(columns)):
			for square in list(filter(lambda x: x != 0, columns[k])):
				if square not in dividers[k]:
					each_column_fits_divider = False
	return has_right_dimensions and has_uniques and each_row_has_five and each_column_ascends and each_column_fits_divider

if __name__ == "__main__":
	assert check_tombola([[0, 11, 20, 0, 44, 0, 60, 76, 0],
						  [0, 12, 0, 34, 45, 0, 63, 0, 82],
						  [2, 0, 27, 0, 48, 51, 66, 0,  0]]) == True
	assert check_tombola([[0, 16, 0, 37, 0, 54, 0, 75, 81],
						  [1, 0, 28, 0, 41, 59, 0, 0, 84],
						  [0, 19, 29, 0, 45, 0, 65, 0, 89]]) == True
	assert check_tombola([[0, 11, 0, 30, 0, 54, 0, 77, 83],
						  [8, 12, 0, 32, 0, 58, 0, 79, 0],
						  [0, 13, 29, 0, 40, 0, 67, 0, 90]]) == True
	assert check_tombola([[0, 0, 0, 35, 0, 55, 60, 72, 86],
						  [3, 0, 22, 0, 40, 58, 0, 79, 0],
						  [7, 0, 25, 0, 41, 0, 65, 0, 88]]) == False
	assert check_tombola([[0, 13, 0, 35, 0, 55, 0, 72, 86],
						  [3, 0, 21, 0, 40, 53, 0, 79, 0],
						  [7, 0, 29, 0, 41, 0, 65, 0, 88]]) == False
	assert check_tombola([[0, 11, 20, 0, 44, 0, 60, 76, 0],
						  [0, 12, 0, 34, 45, 0, 63, 0, 82],
						  [2, 0, 27, 0, 48, 51, 63, 0,  0]]) == False
	assert check_tombola([[0, 11, 24, 0, 41, 0, 65, 70, 0],
						  [0, 16, 0, 32, 48, 0, 67, 0, 89],
						  [0, 0, 0, 0, 0, 0, 67, 0, 89],
						  [1, 0, 27, 33, 0, 59, 0, 74, 0]]) == False
	assert check_tombola([[0, 13, 0, 35, 0, 55, 0, 72, 86],
						  [3, 0, 25, 0, 40, 58, 0, 79, 0],
						  [7, 0, 22, 0, 41, 0, 65, 0, 88]]) == False