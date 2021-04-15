def square_to_rectangle(length, width):
	if length == width:
		return None
	length, width = sorted(length, width)
	

if __name__ == "__main__":
	assert sqInRect(5, 5) == None
	assert sqInRect(5, 3) == [3, 2, 1, 1]