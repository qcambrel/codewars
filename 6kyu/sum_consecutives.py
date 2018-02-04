## Kata: Sum consecutives

# You are given a list/array which contains only integers (positive and 
# negative). Your job is to sum only the numbers that are the same and
# consecutive. The result should be one list.

# Extra credit if you solve it in one line. You can asume there is never
# an empty list/array and there will always be an integer.

# Same meaning: 1 == 1

# 1 != -1

# Examples:

# [1,4,4,4,0,4,3,3,1] # should return [1,12,0,4,6,1]

# """So as you can see sum of consecutives 1 is 1 
# sum of 3 consecutives 4 is 12 
# sum of 0... and sum of 2 
# consecutives 3 is 6 ..."""

# [1,1,7,7,3] # should return [2,14,3]
# [-5,-5,7,7,12,0] # should return [-10,14,12,0]

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