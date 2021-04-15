def get_sum(a, b):
	if a == b:
		return a
	if a > b:
		computed_sum = 0
		all_numbers = []
		while a >= b:
			all_numbers.append(a)
			a = a - 1
		for number in all_numbers:
			computed_sum = computed_sum + number
		return computed_sum
	if a < b:
		computed_sum = 0
		all_numbers = []
		while b >= a:
			all_numbers.append(b)
			b = b - 1
		for number in all_numbers:
			computed_sum = computed_sum + number
		return computed_sum

if __name__ == "__main__":
	assert get_sum(1, 0) == 1
	assert get_sum(1, 2) == 3
	assert get_sum(-1, 2) == 2