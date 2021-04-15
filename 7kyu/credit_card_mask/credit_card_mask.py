def maskify(cc):
	return "#" * (len(cc) - 4) + cc[-4:]

if __name__ == "__main__":
	assert maskify('') == ''
	assert maskify('123') == '123'
	assert maskify('SF$SDfgsd2eA') == '########d2eA'