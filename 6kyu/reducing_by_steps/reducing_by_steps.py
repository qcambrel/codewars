def gcdi(a, b):
	b, a = sorted([abs(a), abs(b)])
	quotient = a // b
	remainder = a % b
	while remainder > 0:
		a = b
		b = remainder
		quotient = a // b
		remainder = a % b
	return b

def lcmu(a, b):
	return abs(a * b) / gcdi(a, b)

def som(a, b):
	return a + b

def maxi(a, b):
	return max(a, b)

def mini(a, b):
	return min(a, b)

def oper_array(fct, arr, init): 
	r = []
	for k in range(len(arr)):
		if r:
			r.append(fct(r[k - 1],arr[k]))
		else:
			r.append(fct(init, arr[k]))
	return r

if __name__ == "__main__":
	a = [ 18, 69, -90, -78, 65, 40 ]
	print(oper_array(gcdi, a, a[0]))
	assert oper_array(gcdi, a, a[0]) == [18, 3, 3, 3, 1, 1]
	assert oper_array(lcmu, a, a[0]) == [18, 414, 2070, 26910, 26910, 107640]
	assert oper_array(som, a, 0) == [18, 87, -3, -81, -16, 24]
	assert oper_array(mini, a, a[0]) == [ 18, 18, -90, -90, -90, -90 ]
	assert oper_array(maxi, a, a[0]) == [18, 69, 69, 69, 69, 69]