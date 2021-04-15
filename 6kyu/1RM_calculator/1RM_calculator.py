def calculate_1RM(weight, reps):
	if reps in [0, 1]:
		return reps * weight
	epley_max = weight * (1 + reps / 30)
	mcglothin_max = (100 * weight) / (101.3 - 2.67123 * reps)
	lombardi_max = weight * reps ** 0.10
	return round(max([epley_max, mcglothin_max, lombardi_max]))


assert calculate_1RM(135,20) == 282
assert calculate_1RM(200,8) == 253
assert calculate_1RM(270,2) == 289
assert calculate_1RM(360,1) == 360
assert calculate_1RM(400,0) == 0