def pick_peaks(arr):
	points = list(enumerate(arr))
	result = {"pos": [], "peaks": []}
	plateaus = []
	for i, x in points:
		if i > 0 and i < len(points) - 1:
			if x > points[i - 1][1] and x > points[i + 1][1]:
				result["pos"].append(i)
				result["peaks"].append(x)
			if x > points[i - 1][1] and x == points[i + 1][1]:
				plateaus.append((i, x))
	for k in range(len(plateaus)):
		pos = plateaus[k][0]
		num = plateaus[k][1]
		for n in range(pos, len(points)):
			if points[n][1] != num:
				if pos not in result["pos"] and points[n][1] < num:
					result["pos"].append(pos)
					result["pos"].sort()
					index = result["pos"].index(pos)
					result["peaks"].insert(index, num)
				else:
					break
	return result

if __name__ == "__main__":
	assert pick_peaks([1,2,3,6,4,1,2,3,2,1]) == {"pos":[3,7], "peaks":[6,3]}
	assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]) == {"pos":[3,7], "peaks":[6,3]}
	assert pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]) == {"pos":[3,7,10], "peaks":[6,3,2]}
	assert pick_peaks([2,1,3,1,2,2,2,2,1]) == {"pos":[2,4], "peaks":[3,2]}
	assert pick_peaks([2,1,3,1,2,2,2,2]) == {"pos":[2], "peaks":[3]}