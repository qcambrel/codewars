def sum_consecutives(ints):
	sums = []
	for k in range(len(ints)):
		if k == 0:
			sums.append(ints[k])
		elif ints[k] == ints[k - 1]:
			sums[-1] = sums[-1] + ints[k]
		else:
			sums.append(ints[k])
	return sums

if __name__ == "__main__":
	assert sum_consecutives([1,4,4,4,0,4,3,3,1]) == [1,12,0,4,6,1]
	assert sum_consecutives([1,1,7,7,3]) == [2,14,3]
	assert sum_consecutives([-5,-5,7,7,12,0]) == [-10,14,12,0]
	assert sum_consecutives([3,3,3,3,1]) == [12, 1] 