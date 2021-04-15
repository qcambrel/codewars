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