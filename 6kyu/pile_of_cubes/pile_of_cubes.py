def find_nb(m):
	n = 1
	while m > 0:
		m = m - n**3
		n = n + 1
	if m == 0:
		return n - 1
	else:
		return -1

if __name__ == "__main__":
	assert find_nb(4183059834009) == 2022
	assert find_nb(24723578342962) == -1
	assert find_nb(135440716410000) == 4824
	assert find_nb(40539911473216) == 3568
	assert find_nb(26825883955641) == 3218