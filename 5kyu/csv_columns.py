## Kata: Grab CSV Columns

# Write a function called csvColumns that takes a CSV (format shown below) 
# and an array of indices, which represents the columns of the CSV, and 
# return a CSV with only the columns specified in the indices array.

# CSV format: 
# The CSV passed in will be a string and will have one or more columns, 
# and one or more rows. The CSV will be of size NxM. Each row is separated
# by a new line character (\n). There will be no spaces in the CSV string.
# Example format of passed in CSV: "1,2,3\n4,5,6\n7,8,9\n10,11,12" 
# How it would look: 
# 1,2,3
# 4,5,6
# 7,8,9
# 10,11,12

# Indices Array info: 
# The indices will be zero based, so the first column will be represented
# as a 0 in the indices array. All values in the indices array will be 
# integers from 0 and up. All test cases will have an indices array of one
# or more integers. Ignore indices that map to a column that doesn't exist.
# If all the values in the indices array do NOT map to any existing column,
# return an empty string ("").

# Examples: 
# csvColumns( "1,2,3\n4,5,6" , [0, 1] ) => returns "1,2\n4,5" 
# csvColumns( "1,2\n3,4\n5,6" , [5, 6, 7] ) => returns "" 
# csvColumns( "a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j" , [1, 3, 5, 7] ) => returns "b,d\n2,4\ng,i"

def csv_columns(csv, indices):
	columns = csv.split("\n")
	output = []
	for k in range(len(columns)):
		column = columns[k].split(",")
		values = []
		for n in range(len(column)):
			if n in indices:
				values.append(str(column[n]))
		if values:
			output.append(values)
	if output:
		for k in range(len(output)):
			output[k] = (",").join(output[k])
		return ("\n").join(output)
	else:
		return ""

if __name__ == "__main__":
	assert csv_columns("1,2\n3,4\n5,6", [5, 6, 7]) == ""
	assert csv_columns("1,2,3\n4,5,6", [0, 1]) == "1,2\n4,5"
	assert csv_columns("a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j", [1, 3, 5, 7]) == "b,d\n2,4\ng,i"
	assert csv_columns("1\n2\n3\n4\n5", [0, 1]) == "1\n2\n3\n4\n5"
	assert csv_columns("1\n2\n3\n4\n5", [1]) == ""